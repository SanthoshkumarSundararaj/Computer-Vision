#!/usr/bin/dev python3

import cv2
import numpy as np

class DiceDetector:
    cap = 0
    
    def __init__(self, cap):
        print ('Dice Detector is running...')
        self.cap = cap
        
    def smoothOperation(self, frame):
        return cv2.medianBlur(frame, 5)
        
    def edgeDetection(self, frame):
        # Invokes canny edge detector
        return cv2.Canny(frame, 150, 100)
        
    def rgb2Grayscale(self, frame):
        # RGB to grayscale convertion
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        '''
        fra = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(fra) 
        #v.fill(255)
        #s.fill(255)
        #h.fill(255)
        hsv_1 = cv2.merge([h,s,v])
        fra = cv2.cvtColor(hsv_1, cv2.COLOR_HSV2BGR)
        '''
        return fra
    
    def contourDetection(self):
        return 1;

    def backgroundSubtraction(self):
        return 0;

    def point4Detection(self):
        return 1;
    
    def __del__(self):
        if self.cap != 0:
            del self.cap
        print ('Dice detector is exiting...')
