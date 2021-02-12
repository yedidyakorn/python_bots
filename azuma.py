import pyautogui
import time
import random
import string

"""
Point(x=488, y=495)
Point(x=472, y=552)
Point(x=474, y=672)
Point(x=1342, y=432)

for i in range(10):
    print(pyautogui.position())
    time.sleep(1)
"""


def randomName():
    letters = string.ascii_lowercase
    return (''.join(random.choice(letters) for i in range(random.randint(3,7))))

def name(x, y):
    pyautogui.PAUSE=0
    pyautogui.click(x,y)
    pyautogui.write(randomName()+ " "+ randomName())

def mail(x,y):
    pyautogui.PAUSE = 0
    pyautogui.click(x, y)
    pyautogui.write(randomName() + "@gmail.com")

btn=None
while btn is None:
    btn=pyautogui.locateCenterOnScreen('aa.png',confidence=0.8)
    if btn is None:
        print('searching')
print(btn)
name(488,495)
time.sleep(0.1)
mail(472,552)
time.sleep(0.1)
pyautogui.click(474, 672)
btn=None
while btn is None:
    btn=pyautogui.locateCenterOnScreen('bb.png',confidence=0.8)
    if btn is None:
        print('searching')
pyautogui.click(1342, 432)
