import pyautogui as gui
import time

f = open('beescript.txt')

# add delay to move curser away from terminal
# time is in second
time.sleep(4)

for word in f.read().split():
    # Change interval for speed of typing
    gui.typewrite(word, interval= 0.07) 
    gui.press('return')
