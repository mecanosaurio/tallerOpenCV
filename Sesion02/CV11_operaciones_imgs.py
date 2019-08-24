# -*- coding: utf-8 -*-

"""
interspecifics - taller OpenCV
Sesion 02, Ejemplo 11

Procesamiento de imágenes: 
    .escala de gris
    .threshold

Created on Fri Aug 23 08:51:47 2019
@author: E
"""



import cv2


img_filename = 'reaction.jpg'
nombre_ventana = "CV11_operaciones_con_imagen: threshold"

cv2.namedWindow(nombre_ventana)

img = cv2.imread(img_filename, cv2.IMREAD_UNCHANGED)
print('Dimensiones de la imagen:', img.shape)

while True: 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    thresh_img = cv2.threshold(gray_img, 30, 255, cv2.THRESH_BINARY)[1] 
    # Displaying image in gray_scale 
    cv2.imshow("Image", img) 
    cv2.imshow("Gray Img", gray_img) 
    cv2.imshow("Threshold Img", thresh_img) 
    key = cv2.waitKey(1) 
    # si 'q' termina
    if key == ord('q'):
        break 
cv2.destroyAllWindows() 


