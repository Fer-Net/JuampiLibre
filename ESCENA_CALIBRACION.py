from Objetos import*


import pygame
from pygame.locals import *
from configuracion import *
from Objetos import *


class ESCENA_CALIBRACION():
    def __init__(self, SonidoAct):
        self.sonidoAct = SonidoAct
        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False

        self.suni_logo = cargar_imagen("Recursos\\Imagenes\\suni_logo.png", True)
        self.nombre = "ESCENA_CALIBRACION"
        self.contador_fondo = 0

        self.fondos = [
        cargar_imagen("Recursos\\Imagenes\\calibracion_fondo_1.png", False),
        cargar_imagen("Recursos\\Imagenes\\calibracion_fondo_2.png", False),
        cargar_imagen("Recursos\\Imagenes\\calibracion_fondo_3.png", False)
        ]

        self.fondo_selec = self.fondos[0]

        self.generico_textbox = Boton(400,550,"Recursos\\Imagenes\\generico_textbox1.png","Recursos\\Imagenes\\generico_textbox1.png","",False)
        self.calibracion_boton_sig = Boton(600,80,"Recursos\\Imagenes\\generico_boton.png","Recursos\\Imagenes\\generico_boton.png","",True)
        self.calibracion_boton_atras = Boton(200,80,"Recursos\\Imagenes\\generico_boton.png","Recursos\\Imagenes\\generico_boton.png","",True)

        self.Texto_boton_sig = Texto("Siguiente",520,55,BLANCO,30)

        self.Texto_boton_atras = Texto("Atras",150,55,BLANCO,30)


        self.parrafos =[
            [
            Texto("1- Asegurese de que la luz de Suni se encuentre encen-",15,460,BLANCO,20),
            Texto("   -dida",15,485,BLANCO,20),
            Texto("2- Inserte los conectores en sus entradas correspon-",15,515,BLANCO,20),
            Texto("   -dientes (mismo color).",15,540,BLANCO,20)
            ],

            [

            Texto("1- Con el otro extremo del conector, sujetelos en el ",15,460,BLANCO,20),
            Texto("   objeto con el o los objetos que va a interactuar. ",15,485,BLANCO,20),
            Texto("2- Asegurese que sean de una superficie no mayor que ",15,515,BLANCO,20),
            Texto("   (por ejemplo) la de una de una manzana.           ",15,540,BLANCO,20)
            ],

            [
            Texto("1- Toque uno a la vez los objetos que ha conectado.     ",15,460,BLANCO,20),
            Texto("   ",15,485,BLANCO,20),
            Texto("2- Corrobore que el programa emita un sonido al tocarlos.",15,515,BLANCO,20),
            Texto("De no funcionar repita los pasos anteriores.",15,540,BLANCO,20)
            ]
        ]

    def set_idioma(self,idioma):
        if (idioma == "Hispano"):
            self.Texto_1.setTexto("Atras")
            self.Texto_2.setTexto("Siguiente")

        if (idioma == "English"):
            self.Texto_1.setTexto("Previuos")
            self.Texto_2.setTexto("Next")

        if (idioma == "Portuguese"):
            self.Texto_1.setTexto("Anterior")
            self.Texto_2.setTexto("Seguindo")


        if (idioma == "Italiano"):
            self.Texto_1.setTexto("Precedente")
            self.Texto_2.setTexto("Seguente")


    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def getNombre(self):
        return self.nombre


    def en_evento(self,evento):
        if(self.accion == True):
            if(self.calibracion_boton_sig.es_click()):
                if(self.sonidoAct == True):
                    self.calibracion_boton_sig.reproducir()
                if(self.contador_fondo == 2):
                    self.contador_fondo = 0
                    return "JUEGO"
                else:
                    self.contador_fondo +=1
                    self.transicion()

            if(self.calibracion_boton_atras.es_click()):
                if(self.sonidoAct == True):
                    self.calibracion_boton_atras.reproducir()
                if(self.contador_fondo == 0):
                    return "MENU"
                else:
                    self.contador_fondo -=1
                    self.transicion()

            if(self.generico_textbox.es_click()):
                if(self.sonidoAct == True):
                    self.generico_textbox.reproducir()
                pass

            if(self.calibracion_boton_sig.es_pisado()):
                pass


            if(self.calibracion_boton_atras.es_pisado()):
                pass


            if(self.generico_textbox.es_pisado()):
                pass



    def dibujo(self, pantalla):
        pantalla.blit(self.fondos[self.contador_fondo],(0,0))

        if(self.fin_aparece == False):
            self.tiempo +=1
            pantalla.blit(self.suni_logo,(300,250))
            if(self.tiempo > 12):
                self.fin_aparece = True
                self.accion = True
        else:
            pantalla.blit(self.generico_textbox.image,self.generico_textbox.rect)
            pantalla.blit(self.calibracion_boton_sig.image,self.calibracion_boton_sig.rect)
            pantalla.blit(self.calibracion_boton_atras.image,self.calibracion_boton_atras.rect)

            self.Texto_boton_sig.dibujar(pantalla)
            self.Texto_boton_atras.dibujar(pantalla)

            for renglones in self.parrafos[self.contador_fondo]:
                renglones.dibujar(pantalla)




