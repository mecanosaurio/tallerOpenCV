# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import cv2

static_back = None
video = cv2.VideoCapture(1)

while True: 
    check, frame = video.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) 
    # In first iteration we assign the value  
    # of static_back to our first frame 
    if static_back is None: 
        static_back = gray 
        continue
    diff_frame = cv2.absdiff(static_back, gray) 
    # If change in between static background and 
    # current frame is greater than 30 it will show white color(255) 
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 
    # Displaying image in gray_scale 
    cv2.imshow("Frame", frame) 
    cv2.imshow("Gray Frame", gray) 
    cv2.imshow("Difference Frame", diff_frame) 
    cv2.imshow("Threshold Frame", thresh_frame) 
    key = cv2.waitKey(1) 
    # if q entered whole process will stop 
    if key == ord('q'):
        break 
video.release()   
# Destroying all the windows 
cv2.destroyAllWindows() 
