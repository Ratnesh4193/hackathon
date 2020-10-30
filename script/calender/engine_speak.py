if True:
    from datetime import datetime
    from time import ctime
    import webbrowser,time
    import playsound
    import os
    import random
    from gtts import gTTS

def engine_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en',slow=False)
    filename=str(random.randint(1,100110))+"welcome.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
