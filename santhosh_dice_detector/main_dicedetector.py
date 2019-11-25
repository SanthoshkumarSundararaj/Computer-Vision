#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:05:17 2018

@author: SanthoshKumar Sundararaj
"""

# Main file
import cv2
import numpy as np
from dicedetector import DiceDetector

# Selecting the camera 0 - default, 1 - USB secondary device
INDEX_CAMERA = 'black.avi'
img = cv2.imread('1.png')
#INDEX_CAMERA = 0

def videoCapture():
    # Video capture from the default camera
    videoCap = cv2.VideoCapture(INDEX_CAMERA)
    
    # Object declaration for the dice detector module 
    dice = DiceDetector(videoCap)
    
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    

    # Loop that captures the frame from the camera and display it
    #while(True):
        # Captures frame-by-frame
    ret, frame = videoCap.read()
    cv2.imwrite("rgbimage.png",img)
    
    fr = fgbg.apply(img)
    cv2.imwrite("back.png",fr)

    # If the capture is not successful
    #if ret == False:
    #    break
    # Resize frame to the pre-defined size
    resizedFrame = cv2.resize(img, (1936, 1216))
    # Convert from RGB image to grayscale 
    rgb2grayscaleFrame = dice.rgb2Grayscale(resizedFrame)
    cv2.imwrite("gray.png",rgb2grayscaleFrame)
    
    # Smooth operation
    
    grayscaleSmoothing = dice.smoothOperation(rgb2grayscaleFrame)
    cv2.imwrite("smooth.png",grayscaleSmoothing)
    # Canny edge detection
    cannyEdgeDetector = dice.edgeDetection(grayscaleSmoothing)
    cv2.imwrite("canny.png",cannyEdgeDetector)
    # Thickens the edges
    kernel = np.ones((5,5),np.uint8)
    
    dilatedImage = cv2.dilate(cannyEdgeDetector, kernel, iterations = 1)
    cv2.imwrite("dilate.png",dilatedImage)
    opening = cv2.morphologyEx(dilatedImage, cv2.MORPH_OPEN, kernel)

    #bg_img = cv2.GaussianBlur(dilatedImage, (5,5), 1)
    #ret1, thres = cv2.threshold(dilatedImage, 50, 50, 0)
    # Background subtraction
    #fr = fgbg.apply(thres)
    
    # Finding contours

    image, contoursDetected, hierarchy = cv2.findContours(dilatedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    approx = 0
    print (len(contoursDetected))
    for cnt in contoursDetected:
        area = cv2.contourArea(cnt)
        if(area > 2000 and area < 4000 and cv2.arcLength(cnt, True) < 1000 and cv2.arcLength(cnt, True) > 200):
            approx = cv2.approxPolyDP(cnt,5*cv2.arcLength(cnt,True),True)
    #cv2.imshow('', image)
            image = cv2.drawContours(img, cnt, -1, (0,255, 0), 3)
            cv2.imwrite("contour.png",image)
    #kernel = np.ones((5,5),np.uint8)
    #approx = cv2.approxPolyDP(cnt,epsilon,True)
          
    # Display frames in the display sequentially
    cv2.imshow('Dice Detector', image)
    
    # Wait till the key is pressed
    #if(cv2.waitKey(1) & 0xFF == ord('q')):
    #    break
    # Handle to the video capture object
    return videoCap

def main():
    # Invoking video capture function
    videoCap = videoCapture()
    # Release the handle to the videoCapture
    videoCap.release()
    
if __name__ == '__main__':
    main()
