# reading tehilim on www.tehilimyahad.com (when site is open)
# the bot presses on "I read the chapter"
# (the site blocks the button after 15 times)

import keyboard
import pyautogui as pg
import time

btn = None


def locate():  # searches for the button
    btn = pg.locateCenterOnScreen('te.png', confidence=0.5)  # te.png is a pic of the wanted button
    return btn


def scroll(x):  # scrolls the window
    print('searching')
    pg.scroll(x)


i = 0
while not keyboard.is_pressed('q'):
    btn = locate()
    if btn is None:
        scroll(-700)
        i = i + 1
        if i > 5:
            i = 0
            scroll(9999)
    pg.click(btn)
    time.sleep(1)
    pg.click(btn)
    time.sleep(3)
