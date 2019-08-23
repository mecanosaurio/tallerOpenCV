# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 04
Captura de video en vivo con openCV

Created on Thu Aug 22 21:12:29 2019
@author: E
"""

import cv2
from time import sleep

video = cv2.VideoCapture(0)

nombre_ventana = "CV04_captura_video_en_vivo"

cv2.namedWindow(nombre_ventana)

sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

while(True):
    check, frame = video.read() 
    cv2.imshow(nombre_ventana, frame)    
    key = cv2.waitKey(1) 
    # si es 'q', termina el programa
    if key == ord('q'):
        break 
video.release()
cv2.destroyAllWindows()






