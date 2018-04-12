#-------------------------------------------------------------------------------
# Name:        EscenaJuego.py
# Purpose:     -
#
# Author:      "Proyecto Juega Juampi! "Fernando Torres y Eduardo Cachizumba
#
# Created:     12/04/2018
# Copyright:   (c) Fernando Torres
# Licence:     GNU General Public License v3.0
#-------------------------------------------------------------------------------


from collections import namedtuple
import pygame
from pygame.locals import *
TAMANNO_LETRA = 20
TAMANNO_LETRA_GRANDE = 40
TAMANNO_LETRA_ENORME = 80
FPS_inicial = 3
TIEMPO_MAX = 61

ANCHO = 800
ALTO = 600
COLOR_LETRAS = (20,200,20)
COLOR_FONDO = (0,0,0)
COLOR_TEXTO = (200,200,200)
COLOR_TIEMPO_FINAL = (200,20,10)
Punto = namedtuple('Punto','x y')


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (148,0,211)
ROSA = (233,150,122)
AMARILLO = (255,255,0)
NARANJA = (255,117,020)

def colorDeImagen(direccion):
    agarraCadenas = False
    color = ""
    for i in range(len(direccion)-1,0,-1):
        if (direccion[i] == "\\"):
            agarraCadenas = False

        if(agarraCadenas):
            color = direccion[i] + color

        if (direccion[i] == "."):
            agarraCadenas = True
    return color


#"Objetos\\Pictogramas\\Sonido\\auto.wav"  dirrecion[len(direccion)-1]
def nombreDeImagen(direccion):
    agarraCadenas = False
    nombre = ""
    for i in range(len(direccion)-1,0,-1):
        if (direccion[i] == "\\"):
            agarraCadenas = False

        if(agarraCadenas):
            nombre = direccion[i] + nombre

        if (direccion[i] == "."):
            agarraCadenas = True
    return nombre



def cargar_imagen(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image