from Objetos import*


import pygame
from pygame.locals import *
from configuracion import *
from Objetos import *

class ESCENA_TUTORIAL():
    def __init__(self):
        self.picto1 =  Boton(400,300,"Escenas\\Creditos\\fondo.png","Escenas\\Creditos\\fondo1.png","",False)
        self.tiempo = 0
        self.nombre = "ESCENA_TUTORIAL"



    def getNombre(self):
        return self.nombre


    def en_evento(self):
        pass


    def dibujo(self, pantalla):
        pantalla.blit(self.picto1.image,self.picto1.rect)
        self.tiempo  = self.tiempo + 1
        if(self.tiempo == 2):
            self.picto1.cambiar(True)
            return
        if(self.tiempo == 15):
            self.picto1.cambiar(False)
            return
        if(self.tiempo == 30):
            self.tiempo = 1
            return

