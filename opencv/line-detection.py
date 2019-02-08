# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:39:39 2019

@author: S. Han
"""
import cv2
import numpy as np # import package

img = cv2.VideoCapture('test2.mp4') # import video
 
def region_of_interest(img, vertices, color_num3=(255,255,255), color_num1=255): # ROI 셋팅

    mask = np.zeros_like(img) # mask = same empty image as img
    # image + ROI image
    if len(img.shape) > 2: # if 3 channal :
        color = color_num3
    else: # if 1 channal(only white and black color) :
        color = color_num1
    
    cv2.fillPoly(mask, vertices, color)
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

while True:
    ret, orignal_frame = img.read()
    
    height, width = orignal_frame.shape[:2]
    blur = cv2.GaussianBlur(orignal_frame, (5, 5), 0)
    blur = cv2.medianBlur(orignal_frame, 5)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    canny = cv2.Canny(hsv, 100, 200) #can revise manually
    vertices = np.array([[(40,height),(width/3-5, height/2+25), (width/2-25, height/2+25), (width-50,height)]], dtype=np.int32) # can revise manually
    ROI_img = region_of_interest(canny, vertices) # canny
    hough = cv2.HoughLinesP(ROI_img, 1, np.pi/180, 90, maxLineGap=100) #ROI image
   
    if hough is not None:
        for line in hough:
            x1, y1, x2, y2 = line[0]
            cv2.line(blur, (x1, y1), (x2, y2), (250, 100, 255), 5) #blur / can revise manually (250, 100, 255 = color, 5 = line width)
            
    cv2.imshow("result", blur)
    cv2.imshow("edges", canny)
    cv2.imshow("ROI", ROI_img)
     
    key = cv2.waitKey(25)
    if cv2.waitKey(1) & 0xFF == ord('q'): # q = exit a program
        break
img.release()
cv2.destroyAllWindows()
