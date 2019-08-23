# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 02
Navegar por las coordenadas de una imágenes con openCV

Created on Thu Aug 22 21:12:29 2019
@author: E
"""

import cv2

nombre_ventana = "CV02_coordenadas_de_la_imagen"


def detecta_clics(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pos = (x, y)
        # draw a rectangle around the region of interest
        cv2.rectangle(img, mouse_pos, (mouse_pos[0]+5, mouse_pos[1]+5), (0, 255, 0), 2)
        cv2.imshow(nombre_ventana, img)
        print('Click en:', mouse_pos)
        

cv2.namedWindow(nombre_ventana)
cv2.setMouseCallback(nombre_ventana, detecta_clics)

img = cv2.imread('notnapoleon.jpg', cv2.IMREAD_UNCHANGED)
print('Dimensiones de la imagen:', img.shape)

while(True):
    cv2.imshow(nombre_ventana, img) 
    key = cv2.waitKey(1) 
    # si es 'q', termina el programa
    if key == ord('q'):
        break 
cv2.destroyAllWindows()






