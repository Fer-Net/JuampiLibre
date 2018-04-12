from Objetos import*


import pygame
from pygame.locals import *
from configuracion import *
from Objetos import *


class ESCENA_IDIOMA():
    def __init__(self, SonidoAct):
        self.sonidoAct = SonidoAct

        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False

        self.generico_fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.suni_logo = cargar_imagen("Recursos\\Imagenes\\suni_logo.png", True)

        self.menu_boton_1 = Boton(400,100,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.menu_boton_2 = Boton(400,250,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.menu_boton_3 = Boton(400,400,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.menu_boton_4 = Boton(400,550,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)





        self.tiempo = 0
        self.nombre = "ESCENA_IDIOMA"

        self.Texto_1 = Texto("Hispano",290,65,BLANCO,40)
        self.Texto_2 = Texto("English",290,225,BLANCO,40)
        self.Texto_3 = Texto("Portuguese",250,375,BLANCO,40)
        self.Texto_4 = Texto("Italiano",299,525,BLANCO,40)


    def transicion(self):
        self.fin_aparece = False
        self.accion = False
        self.tiempo = 0

    def set_idioma(idioma): pass

    def getNombre(self):
        return self.nombre

    def en_evento(self,evento):
        if(self.accion == True):

            if(self.menu_boton_1.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_1.reproducir()
                return "Hispano"
            if(self.menu_boton_2.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_2.reproducir()
                return "English"
            if(self.menu_boton_3.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_3.reproducir()
                return "Portuguese"
            if(self.menu_boton_4.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_4.reproducir()
                return "Italiano"

            if(self.menu_boton_1.es_pisado()):
                self.Texto_1.setColor(NEGRO)
            else:
                self.Texto_1.setColor(BLANCO)

            if(self.menu_boton_2.es_pisado()):
                self.Texto_2.setColor(NEGRO)
            else:
                self.Texto_2.setColor(BLANCO)

            if(self.menu_boton_3.es_pisado()):
                self.Texto_3.setColor(NEGRO)
            else:
                self.Texto_3.setColor(BLANCO)

            if(self.menu_boton_4.es_pisado()):
                self.Texto_4.setColor(NEGRO)
            else:
                self.Texto_4.setColor(BLANCO)


    def dibujo(self, pantalla):
        pantalla.blit(self.generico_fondo,(0,0))

        if(self.fin_aparece == False):
            self.tiempo +=1
            pantalla.blit(self.suni_logo,(300,250))
            if(self.tiempo > 12):
                self.fin_aparece = True
                self.accion = True
        else:

            pantalla.blit(self.menu_boton_1.image,self.menu_boton_1.rect)
            pantalla.blit(self.menu_boton_2.image,self.menu_boton_2.rect)
            pantalla.blit(self.menu_boton_3.image,self.menu_boton_3.rect)
            pantalla.blit(self.menu_boton_4.image,self.menu_boton_4.rect)



            self.Texto_1.dibujar(pantalla)
            self.Texto_2.dibujar(pantalla)
            self.Texto_3.dibujar(pantalla)
            self.Texto_4.dibujar(pantalla)

