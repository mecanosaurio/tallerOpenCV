# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 05

Analiza los colores de los pixeles de 
la captura de video en vivo con openCV
Created on Thu Aug 22 21:12:29 2019
@author: E
""" 

import cv2
from time import sleep

video = cv2.VideoCapture(0)
nombre_ventana = "CV05_pixeles_video_en_vivo"
nframe = 0;
ultimo_clic = [0,0]


def detecta_clics(event, x, y, flags, param):
    global ultimo_clic
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.imshow(nombre_ventana, img)
        ultimo_clic = [x, y]
        pixel= frame[y, x]
        pixel_b, pixel_g, pixel_r = pixel
        print('Ultimo click en:', ultimo_clic, '\tColor de pixel:', pixel)

cv2.namedWindow(nombre_ventana)
cv2.setMouseCallback(nombre_ventana, detecta_clics)

sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

while(True):
    check, frame = video.read() 
    cv2.rectangle(frame, (ultimo_clic[0], ultimo_clic[1]), (ultimo_clic[0]+5, ultimo_clic[1]+5), (0, 255, 0), 1)
    cv2.imshow(nombre_ventana, frame)
    key = cv2.waitKey(1) 
    # si es 'q', termina el programa
    if key == ord('q'):
        break
    nframe+=1
video.release()
cv2.destroyAllWindows()






