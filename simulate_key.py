#!/usr/bin/env python3

import pyautogui
import time
import math

def presslen(key, duration):
    ''' presses key down for a certain length of time'''

    startpress = time.perf_counter()
    
    while time.perf_counter() - startpress < duration:
       pyautogui.keyDown(f"{key}")
    
    pyautogui.keyUp(f"{key}")



def presslen2(key, duration):
    ''' presses down multiple keys for a certain length of time'''

    startpress = time.perf_counter()

    while time.perf_counter() - startpress < duration:
       pyautogui.hotkey(*key)
   

def turn_cameraL(move, seconds):
    pyautogui.moveRel(-abs(move), 0, seconds)

def turn_cameraR(move,seconds):
    pyautogui.moveRel(abs(move), 0, seconds)

def tilt_camera_down(move,seconds):
    pyautogui.moveRel(0,abs(move), seconds)

def tilt_camera_up(move, seconds):
    pyautogui.moveRel(0,-abs(move), seconds)


def main(message):
    
    if message == 'up':
        presslen('w',2)

    if message == 'right':
        presslen('d', 2)

    if message == 'down':
        presslen('s',2)

    if message == 'left':
        presslen('a', 2)




if __name__ == '__main__':

    time.sleep(5)
    pyautogui.click()
