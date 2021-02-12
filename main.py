import time

import keyboard
import pyautogui

"""
X:  571 Y:  290 RGB: (194, 197, 237)
X:  634 Y:  290 RGB: (241, 241, 241)
X:  705 Y:  290 RGB: (255, 255, 255)
X:  781 Y:  289 RGB: (  0,   0,   0)
"""
def click(x, y):
    pyautogui.PAUSE=0
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown(x,y,)
    time.sleep(0.01)
    pyautogui.mouseUp()


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(580, 290)[0] == 0:
        click(581, 290)
    if pyautogui.pixel(640, 290)[0] == 0:
        click(640, 290)
    if pyautogui.pixel(706, 290)[0] == 0:
        click(706, 290)
    if pyautogui.pixel(781, 290)[0] == 0:
        click(781, 290)

