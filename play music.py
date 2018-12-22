# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:25:47 2018       
@author: Rebecca F

"""

from datetime import datetime as dt
import time

def day():
    while True:
        if dt.now().day == 19:
            print("now.day = 19")
        
        else:
            time.sleep(10)
            
        
        return True
            
        
def hour():
    while True:
        if dt.now().hour == 18:
            print("now.hour = 18")
        
        else:
            time.sleep(10)
        
        return True
            
            
def minute():
    while True:
        if dt.now().minute == 32: 
            print("now.minute = 32")   
            
        
        else:
            time.sleep(10)
    
        return True
    
def second():
    while True:
        if dt.now().second == 30:
            print("now.second() = 30")
        
        else:
            time.sleep(10)
            
        return True
        
    
def allTrue():
    while True:
        if day() == True and minute() == True and second() == True:
            print("Success!")
        
        return True
            
day() 
hour()
minute()
second()           
allTrue()

import pygame
from pygame import mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

def playMusic():
    if allTrue() == True:
        mixer.music.load('C:/Users/Daniel F/Desktop/Poopity New/Lift Yourself.wav')
        mixer.music.play()

playMusic()