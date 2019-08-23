# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 10

Procesamiento de imágenes: escala de gris

Created on Fri Aug 23 08:30:26 2019
@author: E
"""



import cv2


img_filename = 'reaction.jpg'
nombre_ventana = "CV10_operaciones_con_imagen: escala de gris"

cv2.namedWindow(nombre_ventana)

img = cv2.imread(img_filename, cv2.IMREAD_UNCHANGED)
print('Dimensiones de la imagen:', img.shape)

while True: 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Img", img) 
    cv2.imshow("Gray Img", gray_img) 
    key = cv2.waitKey(1) 
    # si 'q' termina
    if key == ord('q'):
        break 
cv2.destroyAllWindows() 


