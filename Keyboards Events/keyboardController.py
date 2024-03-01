from pynput.keyboard import Controller

def controlKeyboard():
    
    keyboard = Controller()
    keyboard.type("Hello World")
    
# * Function Call
controlKeyboard()
