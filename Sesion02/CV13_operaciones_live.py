# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 02, Ejemplo 13

Procesamiento de imágenes aplicado al video la camara: 
    .escala de gris
    .threshold
    .blur
    .negativo

@author: E
"""

import cv2
from time import sleep

video = cv2.VideoCapture(0)
nombre_ventana = "CV13_operaciones_con_video: preprocesamiento"
cv2.namedWindow(nombre_ventana)
#cv2.setMouseCallback(nombre_ventana, detecta_clics)

sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

show_no = 0

while True: 
    check, frame = video.read()
    if check:        
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        blur_img = gray_img 
        blur_img = cv2.GaussianBlur(blur_img, (21, 21), 0) 
        nega_img = cv2.bitwise_not(gray_img)
        thresh_img = cv2.threshold(blur_img, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_img = cv2.dilate(thresh_img, None, iterations = 2)

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

    # select image according to key
    key = cv2.waitKey(1) 
    if key == ord('0'): show_no = 0
    if key == ord('1'): show_no = 1
    if key == ord('2'): show_no = 2
    if key == ord('3'): show_no = 3
    if key == ord('4'): show_no = 4
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows() 


