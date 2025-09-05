from pynput import keyboard
import pyautogui
import time

# Auto Walking script
# Press w to start walking manually, and h to re-start the script

h = "Listener"

# Press h to start auto walking and w to pause it
def on_activate_h():
    pyautogui.keyDown('w') 

# Press i to stop auto walking and close the script
def on_activate_i():
    global h
    pyautogui.keyUp('w') 
    time.sleep(0.5) 
    print("Program stopped")
    h.stop()



with keyboard.GlobalHotKeys({
    'h': on_activate_h,
    'i': on_activate_i}) as h:
   h.join()
