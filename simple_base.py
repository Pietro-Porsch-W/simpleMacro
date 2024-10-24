#base imports to be used when creating the Macros module
from pyautogui import *   # A lot of things
import pyautogui          # To locate pixels in the screen
import time               # To be able to give delay between actions
import keyboard           # To be able to Use the keyboard actions
import random             # To give random values, may have a more human apearance for certain actions that requiere it
import win32api, win32con # To be able to use the Mouse events of a windows API, faster than the Python API
# Could use pyautogui to click, but as said, Windows API is WAY faster

#Defines a "procedure" or a "function" to be called, receiving X and Y
def click(x,y):
    win32api.SetCursorPos(x,y)                            #set the cursor at X, Y coordinates
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # defines a event to happen, pressing the left button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   # defines a event to happen, unpressing the left button

time.sleep(0.1) # delay of 0,1s for the next action

# If coordinate in screen is black (0) click on the same position
#  command       coordinate - color(first spectrum of "XXX, XXX, XXX") is equal to 0 (black)
if pyautogui.pixel(581, 400)  [0] == 0:
    click(581, 400)

#============================================================================================================
#displays the mouse position

import pyautogui
pyautogui.displayMousePosition()


