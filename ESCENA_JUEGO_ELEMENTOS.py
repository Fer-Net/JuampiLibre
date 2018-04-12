#-------------------------------------------------------------------------------
# Name:        Principal
# Purpose:
#
# Author:      Fer Net
#
# Created:     09/03/2017
# Copyright:   (c) Fer Net 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import shutil
import Tkinter, tkFileDialog, re
import winsound
import pygame
from pygame.locals import *
import time
import random
from configuracion import*
from Objetos import*




class ESCENA_JUEGO_ELEMENTOS():

    def guardar(self,cadena):
            root = Tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
            root.withdraw() #ahora se cierra
            file_path = tkFileDialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!
            #Ahora para guardar el directorio donde se encontraba el archivo seleccionado:
            match = re.search(r'/.*\..+', file_path)#matches name of file
            return file_path

    def __init__(self, SonidoAct,lista):

        self.cant_selec = len(lista)
        self.sonidoAct = SonidoAct
        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False

        self.nombre = "ESCENA_JUEGO_ELEMENTOS"

        self.fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.suni_logo = cargar_imagen("Recursos\\Imagenes\\suni_logo.png", True)

    #botones----------------------------------

        self.grupal = Boton(150,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_4.png","",True)
##        self.aleatorio = Boton(400,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_4.png","",True)
        self.salir_ = Boton(650,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_4.png","",True)

        self.grupal_txt = Texto("Grupal",80,480,NEGRO,30)
##        self.aleatorio_txt = Texto("Aleatorio",310,480,NEGRO,30)
        self.salir_txt = Texto("Salir",600,480,NEGRO,30)


        self.descrip_txt =[
        Texto("",310,450,NEGRO,30),
        Texto("Permite tocar varios objetos al mismo tiempo!",70,550,NEGRO,20),
        Texto("Reproduce sonidos aleatorios de la biblioteca.",70,550,NEGRO,20),
        Texto("Adios!",340,550,NEGRO,20),
        Texto("           Enciende/apaga el conector.        ",70,550,NEGRO,20),
        Texto("Selecciona cada cuantos segundos se reproduce.",70,550,NEGRO,20),
        Texto("   Sube un archivo de audio para reproducir.  ",70,550,NEGRO,20)
        ]
        self.descrip_seleccionado = 0

##        self.conector1= Boton(210,120,"Recursos\\Imagenes\\MODO1_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector2 = Boton(410,120,"Recursos\\Imagenes\\MODO1_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector3 = Boton(610,120,"Recursos\\Imagenes\\MODO1_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector4 = Boton(210,320,"Recursos\\Imagenes\\MODO1_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector5 = Boton(410,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector6 = Boton(610,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)

        lista_pos = [(210,120),(410,120),(610,120),(210,320),(410,320),(610,320)]
        for i in range (len(lista)):
            x,y = lista_pos[i]
            lista[i].rect.centerx = x
            lista[i].rect.centery = y

        self.of1 = Boton(220,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of2 = Boton(420,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of3 = Boton(620,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of4 = Boton(220,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)

        self.of5 = Boton(420,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of6 = Boton(620,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)

        self.reloj1 = Boton(160,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj2 = Boton(360,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj3 = Boton(560,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj4 = Boton(160,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj5 = Boton(360,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj6 = Boton(560,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)

        self.tiempo1 = Texto("0",110,170,BLANCO,30)
        self.tiempo2 = Texto("0",310,170,BLANCO,30)
        self.tiempo3 = Texto("0",510,170,BLANCO,30)
        self.tiempo4 = Texto("0",110,370,BLANCO,30)
        self.tiempo5 = Texto("0",310,370,BLANCO,30)
        self.tiempo6 = Texto("0",510,370,BLANCO,30)

        self.tiempo1_cont = -1
        self.tiempo2_cont = -1
        self.tiempo3_cont = -1
        self.tiempo4_cont = -1
        self.tiempo5_cont = -1
        self.tiempo6_cont = -1


##        self.listaSonidos = ["Recursos\\Sonidos\\" + "1" + ".wav",
##        "Recursos\\Sonidos\\" + "2" + ".wav",
##        "Recursos\\Sonidos\\" + "3" + ".wav",
##        "Recursos\\Sonidos\\" + "4" + ".wav",
##        "Recursos\\Sonidos\\" + "5" + ".wav",
##        "Recursos\\Sonidos\\" + "6" + ".wav",
##         ]

        self.listaReloj = [ self.reloj1, self.reloj2, self.reloj3, self.reloj4, self.reloj5, self.reloj6]
        self.listaTiempo = [self.tiempo1, self.tiempo2, self.tiempo3, self.tiempo4, self.tiempo5, self.tiempo6]
        self.listaTiempo_cont = [self.tiempo1_cont, self.tiempo2_cont, self.tiempo3_cont, self.tiempo4_cont, self.tiempo5_cont, self.tiempo6_cont]
        self.listaOf = [self.of1,self.of2,self.of3,self.of4,self.of5,self.of6]
        self.listaConectores = lista



        for i in range(5,self.cant_selec-1,-1):
            self.listaReloj.pop(i)
            self.listaTiempo.pop(i)
            self.listaTiempo_cont.pop(i)
            self.listaOf.pop(i)



        self.sonido= str(random.randrange(31))

        self.teclas = [pygame.K_UP, pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_SPACE,pygame.K_s]

#    def set_idioma(self,idioma):
##        if (idioma == "Hispano"):
##            self.Texto_1.setTexto("Atras")
##            self.Texto_2.setTexto("Siguiente")
##
##        if (idioma == "English"):
##            self.Texto_1.setTexto("Previuos")
##            self.Texto_2.setTexto("Next")
##
##        if (idioma == "Portuguese"):
##            self.Texto_1.setTexto("Anterior")
##            self.Texto_2.setTexto("Seguindo")
##
##
##        if (idioma == "Italiano"):
##            self.Texto_1.setTexto("Precedente")
##            self.Texto_2.setTexto("Seguente")

    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def getNombre(self):
        return self.nombre

    def en_evento(self,event):
        if(self.accion == True):

                if event.type == pygame.KEYDOWN:
                    for conector in self.listaConectores:
                        conector.cambiar(False)
                    for i in range (len(self.listaConectores)):
                        if event.key == self.teclas[i] and self.listaOf[i].es_seleccionado() == False: #1
                            if(self.listaTiempo_cont[i] > int(self.listaTiempo[i].getTexto())*10 ):
                                self.listaTiempo_cont[i] = 0
                                self.sonido= self.listaConectores[i].getSonido()
                                if(self.grupal.es_seleccionado()==False):
                                    effect = pygame.mixer.Sound(self.sonido)
                                    channel = effect.play()
                                    channel.set_volume(0,1)
                                else:
                                    winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                                self.listaConectores[i].cambiar(True)


    #--------------------------
##                if(self.aleatorio.es_click()):
##                        if(self.aleatorio.es_seleccionado() == True):
##                            self.aleatorio.cambiar(False)
##                        else:
##                            self.aleatorio.cambiar(True)

                if(self.grupal.es_click()):
                        if(self.grupal.es_seleccionado() == True):
                            self.grupal.cambiar(False)
                            for time in self.listaTiempo:
                                time.setTexto("10")
                        else:
                            self.grupal.cambiar(True)
                            for time in self.listaTiempo:
                                time.setTexto("0")

##                if(self.aleatorio.es_pisado()):
##                    self.descrip_seleccionado = 2
                elif(self.grupal.es_pisado()):
                    self.descrip_seleccionado = 1
                elif(self.salir_.es_pisado()):
                    self.descrip_seleccionado = 3
                else:
                    self.descrip_seleccionado = 0

                for of in self.listaOf:
                        if (of.es_pisado()):
                            self.descrip_seleccionado = 4

                for reloj in self.listaReloj:
                        if (reloj.es_pisado()):
                            self.descrip_seleccionado = 5

##                for subir in self.listaSubir:
##                        if (subir.es_pisado()):
##                            self.descrip_seleccionado = 6
##                print(self.descrip_seleccionado)
##                elif(True):
##                    for of in self.listaOf:
##                        if (of.es_pisado()):
##                            self.descrip_seleccionado = 4
####                elif(True):
####                    for reloj in self.listaReloj:
####                        if (reloj.es_pisado()):
####                            self.descrip_seleccionado = 5
####                elif(True):
####                    for subir in self.listaSubir:
####                        if (subir.es_pisado()):
####                            self.descrip_seleccionado = 6
                for on in self.listaOf:
                    if(on.es_click()):
                        if(on.es_seleccionado() == True):
                            on.cambiar(False)
                        else:
                            on.cambiar(True)
                for i in range (len(self.listaReloj)):
                    if(self.listaReloj[i].es_click()):
                        tiempo_ =  int(self.listaTiempo[i].getTexto())
                        tiempo_ += 5
                        if(tiempo_ == 15):
                            tiempo_ = 0
                        self.listaTiempo[i].setTexto(str(tiempo_))

##                for i in range (len(self.listaSubir)):
##                    if(self.listaSubir[i].es_click()):
##                        sound = self.guardar("")
##                        if(sound != ""):
##                            self.listaSonidos[i] = sound
                if(self.salir_.es_click()):
                        return "MENU"

    def dibujo(self, pantalla):
        pantalla.blit(self.fondo,(0,0))

        if(self.fin_aparece == False):
            self.tiempo +=1
            pantalla.blit(self.suni_logo,(300,250))
            if(self.tiempo > 12):
                self.fin_aparece = True
                self.accion = True
        else:

            pantalla.blit(self.grupal.image,self.grupal.rect)

##            pantalla.blit(self.aleatorio.image,self.aleatorio.rect)
            pantalla.blit(self.salir_.image,self.salir_.rect)

            for conec in self.listaConectores:
                pantalla.blit(conec.image,conec.rect)
            for of in self.listaOf:
                    pantalla.blit(of.image,of.rect)
##            for sub in self.listaSubir:
##                    pantalla.blit(sub.image,sub.rect)
            for re in self.listaReloj:
                    pantalla.blit(re.image,re.rect)

            for tiempo in self.listaTiempo:
                tiempo.dibujar(pantalla)


            for i in range (len(self.listaTiempo_cont)):
                self.listaTiempo_cont[i] = self.listaTiempo_cont[i] +1

            self.grupal_txt.dibujar(pantalla)
##            self.aleatorio_txt.dibujar(pantalla)
            self.salir_txt.dibujar(pantalla)
            self.descrip_txt[self.descrip_seleccionado].dibujar(pantalla)




