import keyboard
import pyautogui as pg
import time

btn=None
def locate():
    btn=pg.locateCenterOnScreen('te.png',confidence=0.5)
    return btn
def scroll(x):
    print('searching')
    pg.scroll(x)
i=0
while keyboard.is_pressed('q') == False:
    btn=locate()
    if btn is None:
        scroll(-700)
        i=i+1
        if i>5:
            i=0
            scroll(9999)
    pg.click(btn)
    time.sleep(1)
    pg.click(btn)
    time.sleep(3)


