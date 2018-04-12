#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
#
# Created:     22/12/2016
# Copyright:   (c) fer 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Objetos import *
import webbrowser

class ESCENA_MENU():
    def __init__(self, SonidoAct):
        self.sonidoAct = SonidoAct

        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False
        self.generico_fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.suni_logo = cargar_imagen("Recursos\\Imagenes\\suni_logo.png", True)

        self.menu_boton_1 = Boton(160,100,"Recursos\\Imagenes\\generico_boton_2.png","Recursos\\Imagenes\\generico_boton_2.png","",True)
        self.menu_boton_2 = Boton(160,250,"Recursos\\Imagenes\\generico_boton_2.png","Recursos\\Imagenes\\generico_boton_2.png","",True)
        self.menu_boton_3 = Boton(160,400,"Recursos\\Imagenes\\generico_boton_2.png","Recursos\\Imagenes\\generico_boton_2.png","",True)
        self.menu_boton_4 = Boton(160,550,"Recursos\\Imagenes\\generico_boton_2.png","Recursos\\Imagenes\\generico_boton_2.png","",True)

        self.menu_boton_5 = Boton(580,530,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.Texto_5 = Texto("Explorar actividades",430,510,NARANJA,20)
       #poner la imagen de explorar actividades


        self.menu_imagen_1 = Boton(600,400,"Recursos\\Imagenes\\menu_imagen_1.png","Recursos\\Imagenes\\menu_imagen_1.png","",True)
        self.menu_imagen_2 = Boton(600,400,"Recursos\\Imagenes\\menu_imagen_2.png","Recursos\\Imagenes\\menu_imagen_2.png","",True)
        self.menu_imagen_3 = Boton(600,400,"Recursos\\Imagenes\\menu_imagen_3.png","Recursos\\Imagenes\\menu_imagen_3.png","",True)
        self.menu_imagen_4 = Boton(600,400,"Recursos\\Imagenes\\menu_imagen_4.png","Recursos\\Imagenes\\menu_imagen_4.png","",True)
        self.menu_imagen_5 = Boton(600,100,"Recursos\\Imagenes\\menu_imagen_5.png","Recursos\\Imagenes\\menu_imagen_5.png","",True)

        self.imagen_selec = self.menu_imagen_1

        self.tiempo = 0
        self.nombre = "ESCENA_MENU"

        self.Texto_1 = Texto("Comenzar",100,55,BLANCO,30)
        self.Texto_1.rotar(9)

        self.Texto_2 = Texto("Tutorial",100,205,BLANCO,30)
        self.Texto_2.rotar(9)

        self.Texto_3 = Texto("Idioma",120,360,BLANCO,30)
        self.Texto_3.rotar(9)

        self.Texto_4 = Texto("Salir",130,510,BLANCO,30)
        self.Texto_4.rotar(9)


        self.con = 0
    def set_idioma(self,idioma):
        if (idioma == "Hispano"):
            self.Texto_1.setTexto("Comenzar")
            self.Texto_2.setTexto("Tutorial")
            self.Texto_3.setTexto("Idioma")
            self.Texto_4.setTexto("Salir")
            self.Texto_5.setTexto("")
        if (idioma == "English"):
            self.Texto_1.setTexto("Start")
            self.Texto_2.setTexto("Tutorial")
            self.Texto_3.setTexto("language")
            self.Texto_4.setTexto("Exit")
            self.Texto_5.setTexto("Explore activities")
        if (idioma == "Portuguese"):
            self.Texto_1.setTexto("Comecar")
            self.Texto_2.setTexto("Tutorial")
            self.Texto_3.setTexto("Linguagem")
            self.Texto_4.setTexto("Sair")
            self.Texto_5.setTexto("Explore atividades")
        if (idioma == "Italiano"):
            self.Texto_1.setTexto("Inizio")
            self.Texto_2.setTexto("Lezione")
            self.Texto_3.setTexto("Lingua")
            self.Texto_4.setTexto("Vieni fuori")
            self.Texto_5.setTexto("Esplora le attivita")
        self.Texto_1.rotar(9)
        self.Texto_2.rotar(9)
        self.Texto_3.rotar(9)
        self.Texto_4.rotar(9)


    def getNombre(self):
        return self.nombre

    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def en_evento(self,evento):
        if(self.accion == True):
            if(self.menu_boton_1.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_1.reproducir()
                return "COMENZAR"
            if(self.menu_boton_2.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_2.reproducir()
                self.transicion()
    ##            return "TUTORIAL"
            if(self.menu_boton_3.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_3.reproducir()
                return "IDIOMA"
            if(self.menu_boton_4.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_4.reproducir()
                return "SALIR"


            if(self.menu_boton_5.es_click()):
                if(self.sonidoAct == True):
                    self.menu_boton_4.reproducir()
                webbrowser.open("http://www.python.org", new=2, autoraise=True)




            if(self.menu_boton_1.es_pisado()):
                self.menu_boton_1.rect.centerx = 175
                self.Texto_1.posX = 115

                self.imagen_selec = self.menu_imagen_1
            else:
                self.menu_boton_1.rect.centerx = 160
                self.Texto_1.posX = 100


            if(self.menu_boton_2.es_pisado()):
                self.menu_boton_2.rect.centerx = 175
                self.Texto_2.posX = 115

                self.imagen_selec = self.menu_imagen_2
            else:
                self.menu_boton_2.rect.centerx = 160
                self.Texto_2.posX = 100


            if(self.menu_boton_3.es_pisado()):
                self.menu_boton_3.rect.centerx = 175
                self.Texto_3.posX = 135

                self.imagen_selec = self.menu_imagen_3
            else:
                self.menu_boton_3.rect.centerx = 160
                self.Texto_3.posX = 120


            if(self.menu_boton_4.es_pisado()):
                self.menu_boton_4.rect.centerx = 175
                self.Texto_4.posX = 145

                self.imagen_selec = self.menu_imagen_4
            else:
                self.menu_boton_4.rect.centerx = 160
                self.Texto_4.posX = 130

            if (self.menu_boton_5.es_pisado()):
                self.menu_boton_5.rect.centery = 520
                self.Texto_5.posY = 500
            else:
                self.menu_boton_5.rect.centery = 530
                self.Texto_5.posY = 510



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

            pantalla.blit(self.imagen_selec.image,self.imagen_selec.rect)
            pantalla.blit(self.menu_boton_2.image,self.menu_boton_2.rect)
            pantalla.blit(self.menu_boton_3.image,self.menu_boton_3.rect)
            pantalla.blit(self.menu_boton_4.image,self.menu_boton_4.rect)
            pantalla.blit(self.menu_boton_5.image,self.menu_boton_5.rect)
            pantalla.blit(self.menu_imagen_5.image,self.menu_imagen_5.rect)


            self.Texto_1.dibujar(pantalla)
            self.Texto_2.dibujar(pantalla)
            self.Texto_3.dibujar(pantalla)
            self.Texto_4.dibujar(pantalla)
            self.Texto_5.dibujar(pantalla)

##    def aparece (self, pantalla):
##        self.tiempo = self.tiempo + 1
##        if(self.tiempo < 12):
##            self.menu_boton_1.rect.centery += 10
##            return
##        self.tiempo = 0
##        self.fin_aparece = True

##            self.Texto_1.posy += 10


