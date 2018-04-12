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
from Objetos import *


class ESCENA_CALIBRACION_FINAL():
    def __init__(self, SonidoAct,lista):
        self.sonidoAct = SonidoAct

        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False
        self.generico_fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.tiempo = 0
        self.nombre = "ESCENA_CALIBRACION_FINAL"

        self.salir_ = Boton(200,550,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)
        self.conec_imagen_1 = Boton(690,250,"Recursos\\Imagenes\\conec_imagen_1.png","Recursos\\Imagenes\\conec_imagen_1.png","",True)
        self.salir_txt = Texto("Salir",150,530,NEGRO,30)

        self.conectores = [
        Boton(80,200,"Recursos\\Imagenes\\conec_1.png","Recursos\\Imagenes\\conec_1.png","",True),
        Boton(140,296,"Recursos\\Imagenes\\conec_2.png","Recursos\\Imagenes\\conec_2.png","",True),
        Boton(280,200,"Recursos\\Imagenes\\conec_3.png","Recursos\\Imagenes\\conec_3.png","",True),
        Boton(340,296,"Recursos\\Imagenes\\conec_4.png","Recursos\\Imagenes\\conec_4.png","",True),
        Boton(480,200,"Recursos\\Imagenes\\conec_5.png","Recursos\\Imagenes\\conec_5.png","",True),
        Boton(540,296,"Recursos\\Imagenes\\conec_6.png","Recursos\\Imagenes\\conec_6.png","",True),
        ]

        self.boton_ok = Boton(600,550,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.ok_txt = Texto("  Continuar",460,530,NEGRO,30)
        lista_pos = [(100,100),(100,400),(300,100),(300,400),(500,100),(500,400)]
        for i in range (len(lista)):
            x,y = lista_pos[i]
            lista[i].rect.centerx = x
            lista[i].rect.centery = y

        self.seleccion_escogida = lista

        self.seleccion_texto_1 = Texto("seleccione seis",100,55,BLANCO,30)

    def getNombre(self):
        return self.nombre

    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def en_evento(self,evento):
        if(self.accion == True):

            if(self.boton_ok.es_click()):
                if(self.sonidoAct == True):
                    self.boton_ok.reproducir()
                return "OK"
##
##            for i in range (len(self.seleccion_escogida)):
##                if(self.seleccion_escogida[i].es_pisado()):
##                    self.seleccion_escogida[i].centery = 175
##                    self.conectores[i].centery = 175
##                else:
##                    self.seleccion_escogida[i].centery = 175
##                    self.conectores[i].centery = 175

            if(self.salir_.es_click()):
                if(self.sonidoAct == True):
                    self.salir_.reproducir()
                return "MENU"

            if(self.salir_.es_pisado()):
                self.salir_.rect.centery = 540
                self.salir_txt.setPos(520,150)
            else:
                self.salir_.rect.centery = 550
                self.salir_txt.setPos(530,150)

            if(self.boton_ok.es_pisado()):
                self.boton_ok.rect.centery = 540
                self.ok_txt.setPos(520,460)
            else:
                self.boton_ok.rect.centery = 550
                self.ok_txt.setPos(530,460)


    def dibujo(self, pantalla):
        pantalla.blit(self.generico_fondo,(0,0))

        if(self.fin_aparece == False):
            self.tiempo +=1
            if(self.tiempo > 12):
                self.fin_aparece = True
                self.accion = True
        else:

##            self.seleccion_texto_1.dibujar(pantalla)

            for i in range (len(self.seleccion_escogida)):
                pantalla.blit(self.conectores[i].image,self.conectores[i].rect)

            for seleccion in self.seleccion_escogida:
                pantalla.blit(seleccion.image,seleccion.rect)
            pantalla.blit(self.boton_ok.image,self.boton_ok.rect)
            pantalla.blit(self.conec_imagen_1.image,self.conec_imagen_1.rect)

            for i in range (len(self.seleccion_escogida)):
                pass
                #pygame.draw.lines(Surface, color, closed, pointlist, width=1)
            pantalla.blit(self.boton_ok.image,self.boton_ok.rect)
            pantalla.blit(self.salir_.image,self.salir_.rect)
            self.salir_txt.dibujar(pantalla)
            self.ok_txt.dibujar(pantalla)


    def set_idioma(self,idioma):
        if (idioma == "Hispano"):
             self.seleccion_texto_1.setTexto("seleccione seis")
        if (idioma == "English"):
             self.seleccion_texto_1.setTexto("select six")
        if (idioma == "Portuguese"):
             self.seleccion_texto_1.setTexto("Comecar")
        if (idioma == "Italiano"):
             self.seleccion_texto_1.setTexto("Inizio")

