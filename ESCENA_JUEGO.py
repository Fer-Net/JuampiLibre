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




class ESCENA_JUEGO():

    def guardar(self,cadena):
            root = Tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
            root.withdraw() #ahora se cierra
            file_path = tkFileDialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!
            #Ahora para guardar el directorio donde se encontraba el archivo seleccionado:
            match = re.search(r'/.*\..+', file_path)#matches name of file
            return file_path

    def __init__(self, SonidoAct,lista):
        self.sonidoAct = SonidoAct
        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False

        self.nombre = "ESCENA_JUEGO"

        self.fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.suni_logo = cargar_imagen("Recursos\\Imagenes\\suni_logo.png", True)

    #botones----------------------------------

        self.grupal = Boton(150,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)
        self.aleatorio = Boton(400,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)
        self.salir_ = Boton(650,500,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)

        self.grupal_txt = Texto("Grupal",80,480,NEGRO,30)
        self.aleatorio_txt = Texto("Aleatorio",310,480,NEGRO,30)
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

        self.conector1= Boton(110,120,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
        self.conector2 = Boton(310,120,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
        self.conector3 = Boton(510,120,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
        self.conector4 = Boton(110,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
        self.conector5 = Boton(310,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
        self.conector6 = Boton(510,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector7 = Boton(710,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)
##        self.conector8 = Boton(110,320,"Recursos\\Imagenes\\juego_conector.png","Recursos\\Imagenes\\juego_conector_presionado.png","",True)


        self.listaConectores =[self.conector1,self.conector2,self.conector3,self.conector4,self.conector5,self.conector6]

        self.listaSonidos = ["Recursos\\Sonidos\\" + "1" + ".wav",
        "Recursos\\Sonidos\\" + "2" + ".wav",
        "Recursos\\Sonidos\\" + "3" + ".wav",
        "Recursos\\Sonidos\\" + "4" + ".wav",
        "Recursos\\Sonidos\\" + "5" + ".wav",
        "Recursos\\Sonidos\\" + "6" + ".wav",


         ]

        self.of1 = Boton(120,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of2 = Boton(320,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of3 = Boton(520,60,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of4 = Boton(120,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)

        self.of5 = Boton(320,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
        self.of6 = Boton(520,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
##        self.of7 = Boton(520,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)
##        self.of8 = Boton(720,260,"Recursos\\Imagenes\\juego_on.png","Recursos\\Imagenes\\juego_off.png","",True)


        self.listaOf = [self.of1,self.of2,self.of3,self.of4,self.of5,self.of6]

        self.subir1 = Boton(150,180,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
        self.subir2 = Boton(350,180,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
        self.subir3 = Boton(550,180,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
        self.subir4 = Boton(150,380,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)

        self.subir5 = Boton(350,380,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
        self.subir6 = Boton(550,380,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
##        self.subir7 = Boton(550,380,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)
##        self.subir8 = Boton(750,380,"Recursos\\Imagenes\\juego_subir.png","Recursos\\Imagenes\\juego_subir.png","",True)


        self.listaSubir = [self.subir1, self.subir2, self.subir3, self.subir4, self.subir5, self.subir6]

        self.reloj1 = Boton(60,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj2 = Boton(260,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj3 = Boton(460,180,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj4 = Boton(60,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)

        self.reloj5 = Boton(260,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
        self.reloj6 = Boton(460,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
##        self.reloj7 = Boton(460,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)
##        self.reloj8 = Boton(660,380,"Recursos\\Imagenes\\juego_tiempo.png","Recursos\\Imagenes\\juego_tiempo.png","",True)


        self.listaReloj = [ self.reloj1, self.reloj2, self.reloj3, self.reloj4, self.reloj5, self.reloj6]

        self.tiempo1 = Texto("0",10,170,NEGRO,30)
        self.tiempo2 = Texto("0",210,170,NEGRO,30)
        self.tiempo3 = Texto("0",410,170,NEGRO,30)
        self.tiempo4 = Texto("0",10,370,NEGRO,30)

        self.tiempo5 = Texto("0",210,370,NEGRO,30)
        self.tiempo6 = Texto("0",410,370,NEGRO,30)
##        self.tiempo7 = Texto("0",410,370,NEGRO,30)
##        self.tiempo8 = Texto("0",610,370,NEGRO,30)


        self.listaTiempo = [self.tiempo1, self.tiempo2, self.tiempo3, self.tiempo4, self.tiempo5, self.tiempo6]

        self.tiempo1_cont = -1
        self.tiempo2_cont = -1
        self.tiempo3_cont = -1
        self.tiempo4_cont = -1
        self.tiempo5_cont = -1
        self.tiempo6_cont = -1
##        self.tiempo7_cont = -1
##        self.tiempo8_cont = -1


        self.listaTiempo_cont = [self.tiempo1_cont, self.tiempo2_cont, self.tiempo3_cont, self.tiempo4_cont, self.tiempo5_cont, self.tiempo6_cont]

        self.sonido= str(random.randrange(31))

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
                    if event.key == pygame.K_UP and self.listaOf[0].es_seleccionado() == False: #1

                        if(self.listaTiempo_cont[0] > int(self.listaTiempo[0].getTexto())*10 ):
                            self.listaTiempo_cont[0] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[0]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(0,1)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[0].cambiar(True)

    #--------------------------
                    if event.key == pygame.K_DOWN and self.listaOf[1].es_seleccionado() == False: #2
                        self.listaConectores[1].cambiar(True)
                        if(self.listaTiempo_cont[1] > int(self.listaTiempo[1].getTexto())*10 ):
                            self.listaTiempo_cont[1] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[1]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(0,1)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[1].cambiar(True)
    #--------------------------
                    if event.key == pygame.K_LEFT and self.listaOf[2].es_seleccionado() == False:#3
                        if(self.listaTiempo_cont[2] > int(self.listaTiempo[2].getTexto())*10 ):
                            self.listaTiempo_cont[2] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[2]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(0,1)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[2].cambiar(True)
    #--------------------------
                    if event.key == pygame.K_RIGHT and self.listaOf[3].es_seleccionado() == False:#4
                        if(self.listaTiempo_cont[3] > int(self.listaTiempo[3].getTexto())*10 ):
                            self.listaTiempo_cont[3] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[3]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(1,0)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[3].cambiar(True)
    #--------------------------
                    if event.key == pygame.K_SPACE and self.listaOf[4].es_seleccionado() == False:#5
                        if(self.listaTiempo_cont[4] > int(self.listaTiempo[4].getTexto())*10 ):
                            self.listaTiempo_cont[4] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[4]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(1,0)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[4].cambiar(True)
    #--------------------------
                    if event.key == pygame.K_s and self.listaOf[5].es_seleccionado() == False: #6
                        if(self.listaTiempo_cont[5] > int(self.listaTiempo[0].getTexto())*10 ):
                            self.listaTiempo_cont[5] = 0
                            if self.aleatorio.es_seleccionado() == True:
                                self.sonido= self.listaSonidos[5]
                            else:
                                self.sonido= str(random.randrange(31))
                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
                            if(self.grupal.es_seleccionado()==False):
                                effect = pygame.mixer.Sound(self.sonido)
                                channel = effect.play()
                                channel.set_volume(0,1)
                            else:
                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
                            self.listaConectores[5].cambiar(True)
##    #--------------------------
##                    if event.key == pygame.K_a and self.listaOf[6].es_seleccionado() == False: #7
##                        if(self.listaTiempo_cont[6] > int(self.listaTiempo[0].getTexto())*10 ):
##                            self.listaTiempo_cont[6] = 0
##                            if self.aleatorio.es_seleccionado() == True:
##                                self.sonido= self.listaSonidos[6]
##                            else:
##                                self.sonido= str(random.randrange(31))
##                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
##                            if(self.grupal.es_seleccionado()==False):
##                                effect = pygame.mixer.Sound(self.sonido)
##                                channel = effect.play()
##                                channel.set_volume(0,1)
##                            else:
##                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
##                            self.listaConectores[6].cambiar(True)
##    #--------------------------
##                    if event.key == pygame.K_w and self.listaOf[7].es_seleccionado() == False: #8
##                        if(self.listaTiempo_cont[7] > int(self.listaTiempo[7].getTexto())*10 ):
##                            self.listaTiempo_cont[7] = 0
##                            if self.aleatorio.es_seleccionado() == True:
##                                self.sonido= self.listaSonidos[7]
##                            else:
##                                self.sonido= str(random.randrange(31))
##                                self.sonido= "Recursos\\Sonidos\\" + self.sonido+ ".wav"
##                            if(self.grupal.es_seleccionado()==False):
##                                effect = pygame.mixer.Sound(self.sonido)
##                                channel = effect.play()
##                                channel.set_volume(0,1)
##                            else:
##                                winsound.PlaySound(self.sonido,winsound.SND_ASYNC)
##                            self.listaConectores[7].cambiar(True)

    #--------------------------
                if(self.aleatorio.es_click()):
                        if(self.aleatorio.es_seleccionado() == True):
                            self.aleatorio.cambiar(False)
                        else:
                            self.aleatorio.cambiar(True)

                if(self.grupal.es_click()):
                        if(self.grupal.es_seleccionado() == True):
                            self.grupal.cambiar(False)
                            for time in self.listaTiempo:
                                time.setTexto("10")
                        else:
                            self.grupal.cambiar(True)
                            for time in self.listaTiempo:
                                time.setTexto("0")

                if(self.aleatorio.es_pisado()):
                    self.descrip_seleccionado = 2
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

                for subir in self.listaSubir:
                        if (subir.es_pisado()):
                            self.descrip_seleccionado = 6
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

                for i in range (len(self.listaSubir)):
                    if(self.listaSubir[i].es_click()):
                        sound = self.guardar("")
                        if(sound != ""):
                            self.listaSonidos[i] = sound
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

            pantalla.blit(self.aleatorio.image,self.aleatorio.rect)
            pantalla.blit(self.salir_.image,self.salir_.rect)

            for conec in self.listaConectores:
                pantalla.blit(conec.image,conec.rect)
            for of in self.listaOf:
                    pantalla.blit(of.image,of.rect)
            for sub in self.listaSubir:
                    pantalla.blit(sub.image,sub.rect)
            for re in self.listaReloj:
                    pantalla.blit(re.image,re.rect)

            for tiempo in self.listaTiempo:
                tiempo.dibujar(pantalla)


            for i in range (len(self.listaTiempo_cont)):
                self.listaTiempo_cont[i] = self.listaTiempo_cont[i] +1

            self.grupal_txt.dibujar(pantalla)
            self.aleatorio_txt.dibujar(pantalla)
            self.salir_txt.dibujar(pantalla)
            self.descrip_txt[self.descrip_seleccionado].dibujar(pantalla)




