# searches for a chat on WhatsApp and sends a lot of messages to that number
# WhatsApp needs to be open and the conversation needs to be on the screen
import random
import string
import time

import pyautogui as pg


def randomName(n=7, m=3):
    letters = string.punctuation
    return ''.join(random.choice(letters) for i in range(random.randint(m, n)))


btn = None
while btn is None:
    btn = pg.locateCenterOnScreen('beliba.png', confidence=0.8)  # pic of the wanted conversation
    if btn is None:
        print('searching')
print(btn)
pg.click(btn)
time.sleep(0.25)
for i in range(50):  # number of messages
    pg.PAUSE = 0
    pg.write(randomName(50, 30))
    pg.press('enter')
    time.sleep(0.1)
