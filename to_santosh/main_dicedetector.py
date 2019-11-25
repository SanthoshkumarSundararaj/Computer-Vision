#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:05:17 2018

@author: SantoshKumar Sundararaj
"""

# Main file
import cv2
import numpy as np
from dicedetector import DiceDetector

# Selecting the camera 0 - default, 1 - USB secondary device
INDEX_CAMERA = 'sa.avi'
#INDEX_CAMERA = 0

def videoCapture():
    # Video capture from the default camera
    videoCap = cv2.VideoCapture(INDEX_CAMERA)
    
    # Object declaration for the dice detector module 
    dice = DiceDetector(videoCap)

    # Loop that captures the frame from the camera and display it
    while(True):
        # Captures frame-by-frame
        ret, frame = videoCap.read()

        # If the capture is not successful
        if ret == False:
            break
        # Resize frame to the pre-defined size
        resizedFrame = cv2.resize(frame, (1936, 1216))
        # Convert from RGB image to grayscale 
        rgb2grayscaleFrame = dice.rgb2Grayscale(resizedFrame)
        
        # Smooth operation
        
        grayscaleSmoothing = dice.smoothOperation(rgb2grayscaleFrame)
        # Canny edge detection
        cannyEdgeDetector = dice.edgeDetection(grayscaleSmoothing)
        # Background subtraction
        #fgbg = cv2.createBackgroundSubtractorMOG2(64,cv2.THRESH_BINARY,1)
        #fr = fgbg.apply(cannyEdgeDetector)

        # Thickens the edges
        kernel = np.ones((5,5),np.uint8)
        
        dilatedImage = cv2.dilate(cannyEdgeDetector, kernel, iterations = 1)
        opening = cv2.morphologyEx(dilatedImage, cv2.MORPH_OPEN, kernel)

        #bg_img = cv2.GaussianBlur(dilatedImage, (5,5), 1)
        ret1, thres = cv2.threshold(dilatedImage, 50, 50, 0)
        # Finding contours
        image, contoursDetected, hierarchy = cv2.findContours(dilatedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        approx = 0
        for cnt in contoursDetected:
            area = cv2.contourArea(cnt)
        
        if(area > 100 and area < 500):
            approx = cv2.approxPolyDP(cnt,0.5*cv2.arcLength(cnt,True),True)
        #cv2.imshow('', image)
        image = cv2.drawContours(frame, cnt, -1, (0,255, 0), 3)
        #kernel = np.ones((5,5),np.uint8)
        #approx = cv2.approxPolyDP(cnt,epsilon,True)
              
        # Display frames in the display sequentially
        cv2.imshow('Dice Detector', thres)        
        
        # Wait till the key is pressed
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    # Handle to the video capture object
    return videoCap

def main():
    # Invoking video capture function
    videoCap = videoCapture()
    # Release the handle to the videoCapture
    videoCap.release()
    
if __name__ == '__main__':
    main()