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

from Objetos import*
import time

import pygame
from pygame.locals import *
from configuracion import *
from Objetos import *


class ESCENA_PRESENTACION(): #llamar a reproducir
    def __init__(self,sonidoAct):
        self.sonidoAct = sonidoAct
        self.presentacion_logo =  Boton(400,300,"Recursos\\Imagenes\\presentacion_logo.jpg","Recursos\\Imagenes\\presentacion_logo.jpg","",False)
        self.tiempo = 0
        self.nombre = "ESCENA_PRESENTACION"
        self.fin = False


    def getNombre(self):
        return self.nombre


    def en_evento(self,evento):
        if(self.fin == True):
            return "irMenu"

    def dibujo(self, pantalla):
        pantalla.fill(BLANCO)
        pantalla.blit(self.presentacion_logo.image,self.presentacion_logo.rect)

        self.tiempo = self.tiempo + 1
        if(self.tiempo == 2):
            pass
##                pygame.mixer.music.load("Escenas\\Presentacion\\fondo1.wav")
##                pygame.mixer.music.play()
        if(self.tiempo == 50):
            self.fin = True