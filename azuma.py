# signing a atzuma on www.atzuma.co.il (when site is open)
# uses a random name and email address
# the bot presses on the sign button
# (the site blocks the button after 5 times)

import pyautogui as pg
import time
import random
import string

"""
points the bot needs to press- might change on different displays
Point(x=488, y=495)
Point(x=472, y=552)
Point(x=474, y=672)
Point(x=1342, y=432)

for i in range(10): #loop to find positions on screen
    print(pg.position())
    time.sleep(1)
"""


def randomName():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(random.randint(3, 7)))


def name(x, y):
    pg.PAUSE = 0
    pg.click(x, y)
    pg.write(randomName() + " " + randomName())


def mail(x, y):
    pg.PAUSE = 0
    pg.click(x, y)
    pg.write(randomName() + "@gmail.com")


btn = None
while btn is None:
    btn = pg.locateCenterOnScreen('sign.png', confidence=0.8)
    if btn is None:
        print('searching')
print(btn)
name(488, 495)
time.sleep(0.1)
mail(472, 552)
time.sleep(0.1)
pg.click(474, 672)
btn = None
while btn is None:
    btn = pg.locateCenterOnScreen('ok.png', confidence=0.8)
    if btn is None:
        print('searching')
pg.click(1342, 432)
