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
import pygame
from pygame.locals import *

from ESCENA_PRESENTACION import*
from ESCENA_MENU import*
from ESCENA_TUTORIAL import*
from ESCENA_IDIOMA import*
from ESCENA_JUEGO import*
from ESCENA_CALIBRACION import*
from ESCENA_SELECCION_MODO import*
from ESCENA_SELECCION_ELEMENTOS import*
from ESCENA_CALIBRACION_FINAL import*
from ESCENA_JUEGO_ELEMENTOS import*
from ESCENA_SELECCION_MUSICA import*
from ESCENA_SELECCION_ELEMENTOS_MUSICA import*
from ESCENA_SELECCION_ELEMENTOS_LIBRE import*


class DirectorJuego():

    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()

##        #Configuraciones
##
##        listaConfig = cargarConfig() #DEVUELVE UNA LISTA CON LAS CONFIGURACIONES SETEADAS
        self.sonidoAct = True
        self.sonidoMusica = True
##        self.pantallaComp = listaConfig[2]
##
##
##
##        if(self.pantallaComp == True):
##            self.pantalla = pygame.display.set_mode([800,600],pygame.FULLSCREEN)
##        else:
##            self.pantalla = pygame.display.set_mode([800,600])
##
##
##        self.listaPicto = cargarPictogramasCnt(self.nroPictogramas,self.gruposSelec) #pictogramas y cantidad con los que se va a jugar!
##

        #Escenas
        self.ESCENA_PRESENTACION = ESCENA_PRESENTACION(self.sonidoAct)
        self.ESCENA_MENU = ESCENA_MENU(self.sonidoAct)
##        self.ESCENA_TUTORIAL = ESCENA_TUTORIAL(self.sonidoAct)
##        self.ESCENA_CONFIGURACIONES = ESCENA_CONFIGURACIONES(self.sonidoAct)
        self.ESCENA_IDIOMA = ESCENA_IDIOMA(self.sonidoAct)
        self.ESCENA_JUEGO = 0
        self.ESCENA_CALIBRACION = ESCENA_CALIBRACION(self.sonidoAct)
        self.ESCENA_SELECCION_MODO = ESCENA_SELECCION_MODO(self.sonidoAct)
        self.ESCENA_SELECCION_ELEMENTOS = 0
        self.ESCENA_SELECCION_ELEMENTOS_LIBRE = 0
        self.ESCENA_SELECCION_MUSICA = 0
        self.ESCENA_SELECCION_ELEMENTOS_MUSICA = 0

        self.ESCENA_CALIBRACION_FINAL = 0
        self.ESCENA_JUEGO_ELEMENTOS = 0
        #estado de escena y director
        self.escenaSelec = self.ESCENA_PRESENTACION
        self.enAccion = True
        #objetos comunes
##        self.cerrar=Boton(785,15,"Objetos\\Botones\\Cerrar\\Imagenes\\cerrar.png","Objetos\\Botones\\Cerrar\\Imagenes\\cerrar1.png","Objetos\\boton1.wav",True)
##        self.puntero = puntero()
        #seteo objetos comunes
##        self.puntero.setVisible(False)
##        self.cerrar.setVisible(False)
        #puntero mouse
##        pygame.mouse.set_visible(False)

    def seleccionarEscena(self,escena):
        self.escenaSelec = escena

    def en_accion(self): #boolean
        return self.enAccion

    def accion(self):
        Time = self.reloj.tick(60)
##        self.puntero.en_movimiento()#en vez de puntero, pincel!

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.enAccion = False
            self.orden(self.escenaSelec.en_evento(evento))#evento de escenas
        if(self.escenaSelec.getNombre()== "ESCENA_PRESENTACION"):
            self.orden(self.escenaSelec.en_evento(None))#arreglar este bug!
        self.escenaSelec.dibujo(self.pantalla)#dibujo escena
        self.dibujo()#encima dibujo elementos de director
        pygame.display.flip()
        self.reloj.tick(60)


    def dibujo(self): pass

##        if(self.cerrar.getVisible() == True):
##            self.pantalla.blit(self.cerrar.image,self.cerrar.rect)

##        if(self.puntero.getVisible()==True):
##            self.pantalla.blit(self.puntero.image,self.puntero.rect)

    def orden(self, orden):#ordenes que recibo de las escenas


        if(self.escenaSelec.getNombre() == "ESCENA_IDIOMA"):
                self.ESCENA_MENU.transicion()
                if(orden == "Hispano"):
                    self.ESCENA_MENU.set_idioma(orden)
                    self.seleccionarEscena(self.ESCENA_MENU)
                if(orden == "Italiano"):
                    self.ESCENA_MENU.set_idioma(orden)
                    self.seleccionarEscena(self.ESCENA_MENU)
                if(orden == "English"):
                    self.ESCENA_MENU.set_idioma(orden)
                    self.seleccionarEscena(self.ESCENA_MENU)
                if(orden == "Portuguese"):
                    self.ESCENA_MENU.set_idioma(orden)
                    self.seleccionarEscena(self.ESCENA_MENU)



        if(self.escenaSelec.getNombre() == "ESCENA_PRESENTACION" ): #si estoy en la escena...
            if(orden == "irMenu"):
                self.seleccionarEscena(self.ESCENA_MENU)
##                pygame.mixer.music.load("Escenas\\MenuInicio\\Sonidos\\musica.wav")
##                if(self.sonidoMusica == True):
##                    pygame.mixer.music.play(-1)

##
        if(self.escenaSelec.getNombre() =="ESCENA_MENU"):
            if(orden == "COMENZAR"):
                self.ESCENA_SELECCION_MODO.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_MODO)
            if(orden == "TUTORIAL"):
                self.seleccionarEscena(self.ESCENA_TUTORIAL)
            if(orden == "IDIOMA"):
                self.ESCENA_IDIOMA.transicion()
                self.seleccionarEscena(self.ESCENA_IDIOMA)
            if(orden == "SALIR"):
                self.enAccion = False
##
##        if(self.escenaSelec.getNombre() == "ESCENA_TUTORIAL" ):
##            if(orden == "FIN"):
##                self.seleccionarEscena(self.ESCENA_MENU)
##

        if(self.escenaSelec.getNombre() == "ESCENA_CALIBRACION" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)


        if(self.escenaSelec.getNombre() == "ESCENA_SELECCION_MODO" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden=="MODO1"):
                self.ESCENA_SELECCION_ELEMENTOS = ESCENA_SELECCION_ELEMENTOS(self.sonidoAct,0)
                self.ESCENA_SELECCION_ELEMENTOS.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS)
            if(orden=="MODO2"):
                self.ESCENA_SELECCION_ELEMENTOS = ESCENA_SELECCION_ELEMENTOS(self.sonidoAct,1)
                self.ESCENA_SELECCION_ELEMENTOS.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS)
            if(orden=="MODO3"):
                self.ESCENA_SELECCION_ELEMENTOS = ESCENA_SELECCION_ELEMENTOS(self.sonidoAct,2)
                self.ESCENA_SELECCION_ELEMENTOS.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS)
            if(orden=="MODO4"):
                self.ESCENA_SELECCION_ELEMENTOS = ESCENA_SELECCION_ELEMENTOS(self.sonidoAct,3)
                self.ESCENA_SELECCION_ELEMENTOS.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS)
            if(orden=="MODO5"):
                self.ESCENA_SELECCION_MUSICA = ESCENA_SELECCION_MUSICA(self.sonidoAct)
                self.ESCENA_SELECCION_MUSICA.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_MUSICA)
            if(orden=="MODO6"):
                self.ESCENA_SELECCION_ELEMENTOS_LIBRE = ESCENA_SELECCION_ELEMENTOS_LIBRE(self.sonidoAct)
                self.ESCENA_SELECCION_ELEMENTOS_LIBRE.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS_LIBRE)

        if(self.escenaSelec.getNombre() == "ESCENA_SELECCION_MUSICA" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden == "SELECCIONADO"):
                self.ESCENA_SELECCION_ELEMENTOS_MUSICA = ESCENA_SELECCION_ELEMENTOS_MUSICA(self.sonidoAct,self.ESCENA_SELECCION_MUSICA.lista_selec)
                self.ESCENA_SELECCION_ELEMENTOS_MUSICA.transicion()
                self.seleccionarEscena(self.ESCENA_SELECCION_ELEMENTOS_MUSICA)


        if(self.escenaSelec.getNombre() == "ESCENA_SELECCION_ELEMENTOS_MUSICA" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden == "SELECCIONADOS"):
                self.ESCENA_CALIBRACION_FINAL = ESCENA_CALIBRACION_FINAL(self.sonidoAct,self.ESCENA_SELECCION_ELEMENTOS_MUSICA.lista_selec)
                self.ESCENA_CALIBRACION_FINAL.transicion()
                self.seleccionarEscena(self.ESCENA_CALIBRACION_FINAL)






        if(self.escenaSelec.getNombre() == "ESCENA_SELECCION_ELEMENTOS" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden == "SELECCIONADOS"):
                self.ESCENA_CALIBRACION_FINAL = ESCENA_CALIBRACION_FINAL(self.sonidoAct,self.ESCENA_SELECCION_ELEMENTOS.lista_selec)
                self.ESCENA_CALIBRACION_FINAL.transicion()
                self.seleccionarEscena(self.ESCENA_CALIBRACION_FINAL)


        if(self.escenaSelec.getNombre() == "ESCENA_SELECCION_ELEMENTOS_LIBRE" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden == "SELECCIONADOS"):
                self.ESCENA_CALIBRACION_FINAL = ESCENA_CALIBRACION_FINAL(self.sonidoAct,self.ESCENA_SELECCION_ELEMENTOS_LIBRE.lista_selec)
                self.ESCENA_CALIBRACION_FINAL.transicion()
                self.seleccionarEscena(self.ESCENA_CALIBRACION_FINAL)




        if(self.escenaSelec.getNombre() == "ESCENA_CALIBRACION_FINAL" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
            if(orden == "OK"):
                self.ESCENA_JUEGO_ELEMENTOS = ESCENA_JUEGO_ELEMENTOS(self.sonidoAct,self.ESCENA_CALIBRACION_FINAL.seleccion_escogida)
                self.ESCENA_JUEGO_ELEMENTOS.transicion()
                self.seleccionarEscena(self.ESCENA_JUEGO_ELEMENTOS)
##
        if(self.escenaSelec.getNombre() == "ESCENA_JUEGO" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)
        if(self.escenaSelec.getNombre() == "ESCENA_JUEGO_ELEMENTOS" ):
            if(orden == "MENU"):
                self.ESCENA_MENU.transicion()
                self.seleccionarEscena(self.ESCENA_MENU)


