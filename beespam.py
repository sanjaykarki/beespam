import pyautogui as gui
import time

f = open('beescript.txt')

# this will create delay us
# so we have time to move curser away from terminal
time.sleep(4)

for word in f.read().split():
    gui.typewrite(word, interval= 0.07) # Change interval for speed of typing
    gui.press('return')
