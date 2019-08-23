# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 01
Cargar y mostrar imágenes con openCV

Created on Thu Aug 22 20:47:37 2019
@author: E
"""

import cv2
 
img = cv2.imread('notnapoleon.jpg', cv2.IMREAD_UNCHANGED) #cv2.IMREAD_COLOR
print('Dimensiones de la imagen:', img.shape)

while(True):
    cv2.imshow("CV01_load_img.py", img)
    key = cv2.waitKey(1) 
    # cuando presione 'q' termina
    if key == ord('q'):
        break 
cv2.destroyAllWindows()
