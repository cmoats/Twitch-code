#!/usr/bin/env python3

import pyautogui
import keyboard
import time

def presslen(key, duration):
    ''' presses key down for a certain length of time'''

    startpress = time.perf_counter()
    
    while time.perf_counter() - startpress < duration:
       pyautogui.keyDown(key)
    
    pyautogui.keyUp(key)

def presslen2(keys, duration):
    ''' presses down multiple keys for a certain length of time'''

    startpress = time.perf_counter()

    while time.perf_counter() - startpress < duration:
       pyautogui.hotkey(*keys)

def press(key):
    pyautogui.press(key)

def double_press(keys):
    pyautogui.hotkey(*keys)

def rmouse_click():
    pyautogui.click(button='right')

def lmouse_click():
    pyautogui.click()

def turn_cameraL(move, seconds):
    pyautogui.moveRel(-abs(move), 0, seconds)

def turn_cameraR(move,seconds):
    pyautogui.moveRel(abs(move), 0, seconds)

def tilt_cameraD(move,seconds):
    pyautogui.moveRel(0,abs(move), seconds)

def tilt_cameraU(move, seconds):
    pyautogui.moveRel(0,-abs(move), seconds)

if __name__ == '__main__':

    

def main(message):
    
    # could also use a dictionary for this instead
    if message == 'up':
        presslen('w',2)

    if message == 'right':
        presslen('d', 2)

    if message == 'down':
        presslen('s',2)

    if message == 'left':
        presslen('a', 2)

    if message == 'lclick':
        lmouse_click()
    
    if message == 'rclick':
        rmouse_click()

    if message == 'shift':
        press('shift')

    if message == 'ctrl':
        press('ctrl')

    if message == 'space':
        press('space')

    if message == 'q':
        press('q')

    if message == 'r':
        press('r')

    if message == 'e':
        press('e')

    if message == 'turnl':
        turn_cameraL(500,0.5)
    
    if message == 'turnr':
        turn_cameraR(500,0.5)

    if message == 'turnu':
        tilt_cameraU(500,0.5)

    if message == 'turnd':
        tilt_cameraD(500,0.5)
