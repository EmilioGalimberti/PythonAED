#script to hold down a key automatically with python

import time
#py -m pip install pyautoguiaaaaaaaaaaaaaaaaaaaa
import pyautogui

pyautogui.FAILSAFE = False

while True:
    pyautogui.press('a')
    pyautogui.press('enter')
    time.sleep(0.1)