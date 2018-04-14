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
import winsound
from configuracion import*
import random

class Boton(pygame.sprite.Sprite):

    def __init__(self,x,y,imagen,imagenCambio,sonido,transparente):

        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen(imagen, transparente)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [0.5, -0.5]
        self.cambio = False
        self.estadoSonido = False
        self.imagen = imagen
        self.imagenCambio = imagenCambio
        self.sonido = sonido
        self.transparente = transparente
        self.visible = True
        self.nombre = nombreDeImagen(imagen)
        self.seleccionado = False

    def getNombre(self):
        return self.nombre

    def setVisible(self,valor):
        self.visible = valor

    def getVisible(self):
        return self.visible

    def es_click(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def estado(self,valor):

        if (valor == True):
            self.image = cargar_imagen(self.imagenCambio, self.transparente)

        else:
            self.image = cargar_imagen(self.imagen, self.transparente)

    def es_seleccionado(self):
        return self.seleccionado

    def es_pisado(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def cambiar(self,valor):
        self.seleccionado = valor
        if(valor == False):
            self.image = cargar_imagen(self.imagen, self.transparente)
            return
        if(valor):
            self.image = cargar_imagen(self.imagenCambio, self.transparente)
            return


    def reproducir(self):
        winsound.PlaySound(self.sonido,winsound.SND_ASYNC)



class Texto():

    def __init__(self,cadena,x,y,color):
        self.cadena= cadena
        self.posX= x
        self.posY= y
        self.color= color

        self.defaultFont= pygame.font.Font( "arial1.ttf", 500)
        self.defaultFontGRANDE= pygame.font.Font( "arial1.ttf", TAMANNO_LETRA_GRANDE)
        self.defaultFontENORME= pygame.font.Font( "arial1.ttf", TAMANNO_LETRA_ENORME)
        self.visible = True
        self.fuente = self.defaultFont


    def setVisible(self,valor):
        self.visible = valor

    def getVisible(self):
        return self.visible

    def setColor(self,color):
        self.color = color
    def setPos(self,posy,posx):
        self.posY = posy
        self.posX = posx
    def setTexto(self,texto):
        self.cadena = texto
    def getTexto(self):
        return self.cadena
    def setDimension(self,nro):
        if (nro == 1):
            self.fuente = self.defaultFont
        if (nro == 2):
            self.fuente = self.defaultFontGRANDE

        if (nro == 3):
            self.fuente = self.defaultFontENORME


    def reproducir(self):
        pass

    def dibujar(self,pantalla):
        pantalla.blit(self.fuente.render(self.cadena, 1, self.color), (self.posX,self.posY))


class Pictograma(pygame.sprite.Sprite):
    #clase pictograma deberia tener una lista de imagenes (coloreadas) para ir cambiando.
    def __init__(self,listaImagen,posx,posy,listaSonido,posDeimagenSelec,sonidoPicto):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen(listaImagen[posDeimagenSelec], False)
        print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"+ listaImagen[posDeimagenSelec])
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.speed = [0.5, -0.5]
        self.listaImagen = listaImagen
        self.listaSonido = listaSonido
        self.imagenSelec = listaImagen[posDeimagenSelec]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = posDeimagenSelec
        self.sonidoPicto = sonidoPicto
        self.cambio = False
        self.nombre= nombreDeImagen(sonidoPicto)
        self.visible = True


    def setVisible(self,valor):
        self.visible = valor

    def getVisible(self):
        return self.visible

    def getColor(self):
        return self.colorSelec

    def cambioRandom(self):
        numeroAleatorio=random.randrange(len(self.listaImagen))
        self.image = cargar_imagen(self.listaImagen[numeroAleatorio],False)
        self.imagenSelec = self.listaImagen[numeroAleatorio]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = numeroAleatorio

    def es_click(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def reproduce(self):
        winsound.PlaySound(self.listaSonido[self.posDeImagenSelec],winsound.SND_ASYNC)

    def reproducir(self):
        winsound.PlaySound(self.sonidoPicto,winsound.SND_ASYNC)

    def es_pisado(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def setRojo(self):
        self.image = cargar_imagen(self.listaImagen[0],False)
        self.imagenSelec = self.listaImagen[0]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 0

    def setAmarillo(self):
        self.image = cargar_imagen(self.listaImagen[1],False)
        self.imagenSelec = self.listaImagen[1]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 1

    def setVerde(self):
        self.image = cargar_imagen(self.listaImagen[2],False)
        self.imagenSelec = self.listaImagen[2]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec =2

    def setAzul(self):
        self.image = cargar_imagen(self.listaImagen[3],False)
        self.imagenSelec = self.listaImagen[3]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 3

    def setBlanco(self):
        self.image = cargar_imagen(self.listaImagen[4],False)
        self.imagenSelec = self.listaImagen[4]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 4

    def setVioleta(self):
        self.image = cargar_imagen(self.listaImagen[5],False)
        self.imagenSelec = self.listaImagen[5]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 5

    def setRosa(self):
        self.image = cargar_imagen(self.listaImagen[6],False)
        self.imagenSelec = self.listaImagen[6]
        self.colorSelec = colorDeImagen(self.imagenSelec)
        self.posDeImagenSelec = 6

    def getNombre(self):
        return self.nombre

    def cambiar(self,pantalla):
        if(self.cambio):
            return
        if(self.cambio==False):
            imagen = cargar_imagen("Objetos\\Pictogramas\\marco.png")
            pantalla.blit(imagen,(50,150) )
            self.cambio=True
            return


class senialador(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Objetos\\senialador\\senialador.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.centerx = x
        self.rect.centery = y
        self.speed = [0.3, -0.5]
        self.visible = True


    def setVisible(self,valor):
        self.visible = valor

    def getVisible(self):
        return self.visible

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def actualizar(self,pix):

        self.rect.centerx += self.speed[0] * 5
        if (self.rect.centerx > self.centerx + pix):
            self.rect.centerx = self.centerx


class puntero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Objetos\\Puntero\\puntero.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 0
        self.speed = [1.0, -0.5]
        self.visible = True


    def setVisible(self,valor):
        self.visible = valor

    def getVisible(self):
        return self.visible
    def en_movimiento(self):
        x,y=pygame.mouse.get_pos()
        self.rect.centerx = x +25
        self.rect.centery = y +60

