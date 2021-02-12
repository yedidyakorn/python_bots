import random
import string
import time

import pyautogui

def randomName(n=7,m=3):
    letters = string.punctuation
    return (''.join(random.choice(letters) for i in range(random.randint(m,n))))

btn=None
while btn is None:
    btn=pyautogui.locateCenterOnScreen('beliba.png',confidence=0.8)
    if btn is None:
        print('searching')
print(btn)
pyautogui.click(btn)
time.sleep(0.25)
for i in range(50):
    pyautogui.PAUSE=0
    pyautogui.write(randomName(50,30))
    pyautogui.press('enter')
    time.sleep(0.1)