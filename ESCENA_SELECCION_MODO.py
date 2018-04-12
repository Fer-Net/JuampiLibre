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


class ESCENA_SELECCION_MODO():
    def __init__(self, SonidoAct):
        self.sonidoAct = SonidoAct

        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False
        self.generico_fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.tiempo = 0
        self.nombre = "ESCENA_SELECCION_MODO"

        self.modo_boton_1 = Boton(600,50,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.modo_boton_2 = Boton(600,150,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.modo_boton_3 = Boton(600,250,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.modo_boton_4 = Boton(600,350,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.modo_boton_5 = Boton(600,450,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.modo_boton_6 = Boton(600,550,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)

        self.modo_imagen_1 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_1.png","Recursos\\Imagenes\\modo_imagen_1.png","",True)
        self.modo_imagen_2 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_2.png","Recursos\\Imagenes\\modo_imagen_2.png","",True)
        self.modo_imagen_3 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_3.png","Recursos\\Imagenes\\modo_imagen_3.png","",True)
        self.modo_imagen_4 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_4.png","Recursos\\Imagenes\\modo_imagen_4.png","",True)
        self.modo_imagen_5 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_5.png","Recursos\\Imagenes\\modo_imagen_5.png","",True)
        self.modo_imagen_6 = Boton(200,250,"Recursos\\Imagenes\\modo_imagen_6.png","Recursos\\Imagenes\\modo_imagen_6.png","",True)

        self.salir_ = Boton(200,550,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)
        self.salir_txt = Texto("Salir",150,530,NEGRO,30)

        self.imagen_selec = self.modo_imagen_1

        self.modo_texto_0 = [
        Texto("Frutas",530,30,BLANCO,30),
        Texto("Sentimientos",460,130,BLANCO,30),
        Texto("Colores",520,230,BLANCO,30),
        Texto("Direcciones",470,330,BLANCO,30),
        Texto("Musica",530,430,BLANCO,30),
        Texto("Modo libre",460,530,BLANCO,30)
        ]

        self.modo_texto_1 = [
        Texto("",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]
        self.modo_texto_2 = [
        Texto("J",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]
        self.modo_texto_3 = [
        Texto("",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]
        self.modo_texto_4 = [
        Texto("",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]
        self.modo_texto_5 = [
        Texto("",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]
        self.modo_texto_6 = [
        Texto("",150,150,NEGRO,20),
        Texto("",150,170,NEGRO,20),
        Texto("",150,200,NEGRO,20),
        Texto("",150,220,NEGRO,20),
        ]

        self.texto_selec = self.modo_texto_1

    def getNombre(self):
        return self.nombre

    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def en_evento(self,evento):
        if(self.accion == True):
            if(self.modo_boton_1.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_1.reproducir()
                return "MODO1"
            if(self.modo_boton_2.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_2.reproducir()
                self.transicion()
                return "MODO2"
            if(self.modo_boton_3.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_3.reproducir()
                return "MODO3"
            if(self.modo_boton_4.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_4.reproducir()
                return "MODO4"
            if(self.modo_boton_5.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_5.reproducir()
                return "MODO5"
            if(self.modo_boton_6.es_click()):
                if(self.sonidoAct == True):
                    self.modo_boton_6.reproducir()
                return "MODO6"

            if(self.salir_.es_click()):
                if(self.sonidoAct == True):
                    self.salir_.reproducir()
                return "MENU"


            if(self.modo_boton_1.es_pisado()):
                self.modo_boton_1.rect.centerx = 550
                self.texto_selec = self.modo_texto_1
                self.imagen_selec = self.modo_imagen_1
                self.modo_texto_0[0].setPos(30,480)
            else:
                self.modo_boton_1.rect.centerx = 600
                self.modo_texto_0[0].setPos(30,530)

            if(self.salir_.es_pisado()):
                self.salir_.rect.centery = 540
                self.salir_txt.setPos(520,150)
            else:
                self.salir_.rect.centery = 550
                self.salir_txt.setPos(530,150)


            if(self.modo_boton_2.es_pisado()):
                self.modo_boton_2.rect.centerx = 550
                self.texto_selec = self.modo_texto_2
                self.imagen_selec = self.modo_imagen_2
                self.modo_texto_0[1].setPos(130,410)
            else:
                self.modo_boton_2.rect.centerx = 600
                self.modo_texto_0[1].setPos(130,460)


            if(self.modo_boton_3.es_pisado()):
                self.modo_boton_3.rect.centerx = 550
                self.texto_selec = self.modo_texto_3
                self.imagen_selec = self.modo_imagen_3
                self.modo_texto_0[2].setPos(230,470)
            else:
                self.modo_boton_3.rect.centerx = 600
                self.modo_texto_0[2].setPos(230,520)


            if(self.modo_boton_4.es_pisado()):
                self.modo_boton_4.rect.centerx = 550
                self.texto_selec = self.modo_texto_4
                self.imagen_selec = self.modo_imagen_4
                self.modo_texto_0[3].setPos(330,420)
            else:
                self.modo_boton_4.rect.centerx = 600
                self.modo_texto_0[3].setPos(330,470)


            if(self.modo_boton_5.es_pisado()):
                self.modo_boton_5.rect.centerx = 550
                self.texto_selec = self.modo_texto_5
                self.imagen_selec = self.modo_imagen_5
                self.modo_texto_0[4].setPos(430,480)
            else:
                self.modo_boton_5.rect.centerx = 600
                self.modo_texto_0[4].setPos(430,530)


            if(self.modo_boton_6.es_pisado()):
                self.modo_boton_6.rect.centerx = 550
                self.texto_selec = self.modo_texto_6
                self.imagen_selec = self.modo_imagen_6
                self.modo_texto_0[5].setPos(530,410)
            else:
                self.modo_boton_6.rect.centerx = 600
                self.modo_texto_0[5].setPos(530,460)



    def dibujo(self, pantalla):
        pantalla.blit(self.generico_fondo,(0,0))

        if(self.fin_aparece == False):
            self.tiempo +=1
            if(self.tiempo > 12):
                self.fin_aparece = True
                self.accion = True
        else:
            pantalla.blit(self.imagen_selec.image,self.imagen_selec.rect)

            pantalla.blit(self.modo_boton_1.image,self.modo_boton_1.rect)
            pantalla.blit(self.modo_boton_2.image,self.modo_boton_2.rect)
            pantalla.blit(self.modo_boton_3.image,self.modo_boton_3.rect)
            pantalla.blit(self.modo_boton_4.image,self.modo_boton_4.rect)
            pantalla.blit(self.modo_boton_5.image,self.modo_boton_5.rect)
            pantalla.blit(self.modo_boton_6.image,self.modo_boton_6.rect)

            pantalla.blit(self.salir_.image,self.salir_.rect)
            self.salir_txt.dibujar(pantalla)
            for txt in self.texto_selec:
                txt.dibujar(pantalla)

            for txt in self.modo_texto_0:
                txt.dibujar(pantalla)


    def set_idioma(self,idioma):
        if (idioma == "Hispano"):
            self.modo_texto_1 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_2 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_3 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_4 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_5 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_6 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
        if (idioma == "English"):
            self.modo_texto_1 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_2 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_3 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_4 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_5 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_6 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
        if (idioma == "Portuguese"):
            self.modo_texto_1 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_2 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_3 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_4 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_5 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_6 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
        if (idioma == "Italiano"):
            self.modo_texto_1 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_2 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_3 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_4 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_5 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]
            self.modo_texto_6 = [
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30),
            ("Comenzar",100,55,BLANCO,30)
            ]

