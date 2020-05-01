import pyautogui as gui

gui.click(1522, 936) # X and Y cordinate of screen

f = open('beescript.txt')

for word in f.read().split():
    gui.typewrite(word, interval= 0.07) # Change interval for speed of typing
    gui.press('return')
