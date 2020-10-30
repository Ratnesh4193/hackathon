import datetime
from .calc_setup import get_calendar_service
from . import engine_speak
def list_event():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of 10 events')
    events_result = service.events().list(
    calendarId='primary', timeMin=now,
    maxResults=10, singleEvents=True,
    orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        engine_speak.engine_speak('No upcoming events found.')
    else:
        for event in events:
            engine_speak.engine_speak(event)
            start = event['start'].get('dateTime', event['start'].get('date'))
            engine_speak.engine_speak(start, event['summary'])

if __name__ == '__main__':
   list_event()