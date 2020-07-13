import time
import keyboard
import mouse


turnSpeed = 0.2 #How fast your turns are (neasured in seconds).
southpaw = True # I play with my left and right mouse buttons switched so I added this to easily toggle between the two


def walk(blocks):
    keyboard.press("w")
    x = blocks / 4.37
    time.sleep(x)
    keyboard.release("w")

def turn(deg):
    deg = (deg / 5.45454545 / turnSpeed) #It's not exact at all, a lot of trial and error is required.
    mouse.move(deg,0,absolute=False,duration=turnSpeed)

def jump(key):
    if key == "up":#you can jump forward or just jump normally
        keyboard.press("space")
        time.sleep(0.5)
        keyboard.release("space")
    elif key == "forward": 
        keyboard.press("w")
        keyboard.press("space")
        time.sleep(0.5)
        keyboard.release("space")
        keyboard.release("w")
    else:
        print("invalid direction")


def waitFor(hotkey): #assign a hotkey to trigger the movements.
    keyboard.wait(hotkey=hotkey, suppress=False, trigger_on_release=False)

def attack():#Self explanatory
    if southpaw == True:
        mouse.right_click()
    else:
        mouse.click()

def sendMessage(msg):#Self explanatory
    keyboard.press_and_release("t")
    time.sleep(0.3)
    keyboard.write(msg)
    keyboard.press_and_release("enter")

def runCommand(cmd):#Self explanatory
    keyboard.press_and_release("/")
    time.sleep(0.3)
    keyboard.write(cmd)
    keyboard.press_and_release("enter")
    




