# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 02, Ejemplo 12

Procesamiento de imágenes: 
    .escala de gris
    .threshold
    .blur
    .negativo

Created on Fri Aug 23 08:54:12 2019
@author: E
"""



import cv2


img_filename = 'notnapoleon.jpg'
nombre_ventana = "CV12_operaciones_con_imagen: preprocesamiento"

cv2.namedWindow(nombre_ventana)
static_back = None

img = cv2.imread(img_filename, cv2.IMREAD_COLOR)
print('Dimensiones de la imagen:', img.shape)

show_no = 0

while True: 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blur_img = gray_img 
    blur_img = cv2.GaussianBlur(blur_img, (21, 21), 0) 
    nega_img = cv2.bitwise_not(gray_img)
    thresh_img = cv2.threshold(blur_img, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_img = cv2.dilate(thresh_img, None, iterations = 2)

    # show the one
    if (show_no == 0):
        cv2.imshow(nombre_ventana, img)
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
cv2.destroyAllWindows() 


