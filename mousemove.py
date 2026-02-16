import importlib.util, subprocess, sys

for p in "pyautogui".split():
    if not importlib.util.find_spec(p):
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", p], check=True)

import pyautogui
import time
import random

pyautogui.FAILSAFE = False

print("Mouse mover started. Press Ctrl+C to stop.")

while True:
    dx = random.choice([-1, 1])
    pyautogui.moveRel(dx, 0)
    pyautogui.moveRel(-dx, 0)
    time.sleep(random.randint(30, 90))
