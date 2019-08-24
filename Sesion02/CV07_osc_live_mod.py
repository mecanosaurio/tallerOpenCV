# -*- coding: utf-8 -*-
"""
interspecifics - taller OpenCV
Sesion 02, Ejemplo 06 MOD

Envía mensajes osc con información de los pixeles de 
la captura de video en vivo con openCV, 
    .de modo constante
    .por canales separados r,g,b

Created on Sat Aug 24 08:27:00 2019
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
nombre_ventana = "CV07_OSC_video_en_vivo: MOD"
nframe = 0;
ultimo_clic = [0,0]
pixel=[0,0,0]


def send_color(r, g, b):
    msg = OscMessageBuilder(address='/CV07/color/')
    #msg.add_arg(r, 'i')
    #msg.add_arg(g, 'i')
    msg.add_arg(b, 'i')
    m = msg.build()
    print(m.address, m.params)
    client.send(m)

def send_colors(r, g, b):
    msg = OscMessageBuilder(address='/CV07/color/r')
    msg.add_arg(r, 'i')
    m = msg.build()
    client.send(m)
    print(m.address, m.params)
    msg = OscMessageBuilder(address='/CV07/color/g')
    msg.add_arg(g, 'i')
    m = msg.build()
    client.send(m)
    print(m.address, m.params)
    msg = OscMessageBuilder(address='/CV07/color/b')
    msg.add_arg(b, 'i')
    m = msg.build()
    client.send(m)
    print(m.address, m.params)


def detecta_clics(event, x, y, flags, param):
    global ultimo_clic
    if event == cv2.EVENT_LBUTTONDOWN:
        ultimo_clic = [x, y]
        pixel= frame[y, x]
        print('Ultimo click en:', ultimo_clic)


cv2.namedWindow(nombre_ventana)
cv2.setMouseCallback(nombre_ventana, detecta_clics)

sleep(1)
check, frame = video.read() 
print('Dimensiones de la imagen:', frame.shape)

while(True):
    check, frame = video.read()
    if check:
        cv2.rectangle(frame, (ultimo_clic[0]-5, ultimo_clic[1]-5), (ultimo_clic[0]+5, ultimo_clic[1]+5), (255, 192, 32), 1)
        cv2.line(frame, (ultimo_clic[0], ultimo_clic[1]-10), (ultimo_clic[0], ultimo_clic[1]-2), (255, 127, 0), 1)
        cv2.line(frame, (ultimo_clic[0], ultimo_clic[1]+2), (ultimo_clic[0], ultimo_clic[1]+10), (255, 127, 0), 1)
        cv2.line(frame, (ultimo_clic[0]-10, ultimo_clic[1]), (ultimo_clic[0]-2, ultimo_clic[1]), (255, 127, 0), 1)
        cv2.line(frame, (ultimo_clic[0]+2, ultimo_clic[1]), (ultimo_clic[0]+10, ultimo_clic[1]), (255, 127, 0), 1)
        cv2.imshow(nombre_ventana, frame)
    if nframe%10==0:
        pixel = frame[ultimo_clic[1], ultimo_clic[0]]
        #print('\tColor de pixel:', pixel)
        send_colors(pixel[2], pixel[1], pixel[0])
    key = cv2.waitKey(1) 
    # si es 'q', termina el programa
    if key == ord('q'):
        break
    nframe+=1

video.release()
cv2.destroyAllWindows()






