# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 03
Navegar por las coordenadas de una imágenes con openCV
Y extraer el color de los pixeles

Created on Thu Aug 22 21:12:29 2019
@author: E
"""

import cv2

nombre_ventana = "CV03_pixeles_de_una_imagen"


def detecta_clics(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.imshow(nombre_ventana, img)
        mouse_pos = (x, y)
        pixel= img[y, x]
        print('Click en:', mouse_pos, '\tColor de pixel:', pixel)
        cv2.rectangle(img, (mouse_pos[0], mouse_pos[1]), (mouse_pos[0]+5, mouse_pos[1]+5), (0, 255, 0), 1)

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






