from . import assistant_gui
shopping_list = [  ]
def  displayList():
	assistant_gui.engine_speak("shopping list")
	for i in shopping_list:
	    assistant_gui.engine_speak(i)

def addItem():
	item = record_audio("enter the item you wish to add to the shopping list")
	shopping_list.append(item)
	assistant_gui.engine_speak(item+"has been added to the shopping list")
 
def removeItem():
	item= record_audio("enter the item you wish to remove from the shopping list")
	shopping_list.remove(item)
	assistant_gui.engine_speak(item+"has been removed from the shopping list")

def checkItem():
	item= record_audio("what item would you like to check on the shopping list")
	if item in shopping_list:
	   assistant_gui.engine_speak("yes"+item +"is on the shopping list")
	else:
	    assistant_gui.engine_speak("No"+item +"is not on the shopping list")
def listLength():
    assistant_gui.engine_speak("there are", len(shopping_list), "items on the shopping list")
def clearList():
	shopping_list.clear()
	assistant_gui.engine_speak("the shopping list is now empty")

