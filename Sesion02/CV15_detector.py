# -*- coding: utf-8 -*-
"""

interspecifics - taller OpenCV
Sesion 02, Ejemplo 15

Procesamiento de imágenes aplicado al video la camara: 
    ->trackear blobs

Created on Sat Aug 24 08:57:04 2019
@author: E
"""

import cv2
from time import sleep

video = cv2.VideoCapture(0)
nombre_ventana = "CV15_detector_de_blobs"
cv2.namedWindow(nombre_ventana)
fondo_estatico = None
#cv2.setMouseCallback(nombre_ventana, detecta_clics)

# detector init
pp=cv2.SimpleBlobDetector_Params()
pp.minThreshold=208
pp.maxThreshold=255
pp.filterByArea=True
pp.minArea=50
pp.maxArea=10000
pp.filterByColor=True
pp.blobColor=255
pp.filterByCircularity=False
pp.filterByConvexity=False
pp.filterByInertia=False
detector = cv2.SimpleBlobDetector_create(pp)


sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

show_no = 0

while True: 
    check, frame = video.read()
    if check:        
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        if fondo_estatico is None: 
            fondo_estatico = gray_img
            continue
        diff_frame = cv2.absdiff(fondo_estatico, gray_img) 
        blur_img = diff_frame
        blur_img = cv2.GaussianBlur(blur_img, (21, 21), 0) 
        nega_img = cv2.bitwise_not(diff_frame)
        thresh_img = cv2.threshold(blur_img, 160, 255, cv2.THRESH_BINARY)[1]
        thresh_img = cv2.dilate(thresh_img, None, iterations = 2)
        # detectar
        keyPoints = detector.detect(thresh_img)
        for k in keyPoints:
            print (k)
        #kp_coo = [k.pt for k in keyPoints]

    # show the one
    if (show_no == 0):
        cv2.imshow(nombre_ventana, frame)
    elif(show_no==1):
        cv2.imshow(nombre_ventana, gray_img) 
    elif(show_no==2):
        cv2.imshow(nombre_ventana, blur_img) 
    elif(show_no==3):
        cv2.imshow(nombre_ventana, thresh_img) 
    elif(show_no==4):
        cv2.imshow(nombre_ventana, nega_img) 
    elif(show_no==5):
        cv2.imshow(nombre_ventana, diff_frame) 

    # select image according to key
    key = cv2.waitKey(1) 
    if key == ord('0'): show_no = 0
    if key == ord('1'): show_no = 1
    if key == ord('2'): show_no = 2
    if key == ord('3'): show_no = 3
    if key == ord('4'): show_no = 4
    if key == ord('5'): show_no = 5
    if key == ord('b'): fondo_estatico = None
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows() 


