# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 01, Ejemplo 06

Envía mensajes osc con información de los pixeles de 
la captura de video en vivo con openCV

Created on Thu Aug 22 21:12:29 2019
@author: E
"""

import cv2
from time import sleep
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
PORT = 8000
client = udp_client.UDPClient(IP, PORT)

video = cv2.VideoCapture(0)
nombre_ventana = "CV06_OSC_video_en_vivo"
nframe = 0;
ultimo_clic = [0,0]


def send_color(r, g, b):
    msg = OscMessageBuilder(address='/CV06/pixel')
    msg.add_arg(r, 'i')
    msg.add_arg(g, 'i')
    msg.add_arg(b, 'i')
    m = msg.build()
    print(m.address, m.params)
    client.send(m)


def detecta_clics(event, x, y, flags, param):
    global ultimo_clic
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.imshow(nombre_ventana, img)
        ultimo_clic = [x, y]
        pixel= frame[y, x]
        pixel_b = pixel[0]
        pixel_g = pixel[1]
        pixel_r = pixel[2]
        print('Ultimo click en:', ultimo_clic, '\tColor de pixel:', pixel)
        send_color(pixel_r, pixel_g, pixel_b)


cv2.namedWindow(nombre_ventana)
cv2.setMouseCallback(nombre_ventana, detecta_clics)

sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

while(True):
    check, frame = video.read() 
    cv2.rectangle(frame, (ultimo_clic[0]-5, ultimo_clic[1]-5), (ultimo_clic[0]+5, ultimo_clic[1]+5), (255, 192, 32), 1)
    cv2.line(frame, (ultimo_clic[0], ultimo_clic[1]-10), (ultimo_clic[0], ultimo_clic[1]+10), (255, 127, 0), 1)
    cv2.line(frame, (ultimo_clic[0]-10, ultimo_clic[1]), (ultimo_clic[0]+10, ultimo_clic[1]), (255, 127, 0), 1)
    cv2.imshow(nombre_ventana, frame)
    key = cv2.waitKey(1) 
    # si es 'q', termina el programa
    if key == ord('q'):
        break
    nframe+=1
video.release()
cv2.destroyAllWindows()






