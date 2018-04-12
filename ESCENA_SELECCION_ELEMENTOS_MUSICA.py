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


class ESCENA_SELECCION_ELEMENTOS_MUSICA():
    def __init__(self, SonidoAct,selec):
        self.sonidoAct = SonidoAct

        self.tiempo = 0
        self.fin_aparece = False
        self.accion = False
        self.generico_fondo = cargar_imagen("Recursos\\Imagenes\\generico_fondo_1.jpg", False)
        self.tiempo = 0
        self.nombre = "ESCENA_SELECCION_ELEMENTOS_MUSICA"
        self.lista_selec = []

        self.salir_ = Boton(200,550,"Recursos\\Imagenes\\generico_boton_1.png","Recursos\\Imagenes\\generico_boton_1.png","",True)
        self.salir_txt = Texto("Salir",150,530,NEGRO,30)

        self.selecciones = [
        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_1.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_1_8.wav",False),
        ],

        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_2.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_2_8.wav",False),
        ],

        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_3.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_3_8.wav",False),
        ],
        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO4_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_4.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_4_8.wav",False),
        ],
        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_5.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_5_8.wav",False),
        ] ,

        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_6.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_6_8.wav",False),
        ]
        ,

        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_7.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_7_8.wav",False),
        ]
        ,

        [
        Boton(100,100,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_1.wav",False),
        Boton(300,100,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_2.wav",False),
        Boton(500,100,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_3.wav",False),
        Boton(700,100,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_4.wav",False),
        Boton(100,400,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_5.wav",False),
        Boton(300,400,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_6.wav",False),
        Boton(500,400,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_7.wav",False),
        Boton(700,400,"Recursos\\Imagenes\\MODO5_elementos_8.png","Recursos\\Imagenes\\juego_conector_presionado.png","Recursos\\Sonidos\\M5_8_8.wav",False),
        ]
        ]

        self.boton_ok = Boton(600,550,"Recursos\\Imagenes\\generico_boton_3.png","Recursos\\Imagenes\\generico_boton_3.png","",True)
        self.ok_txt = Texto("  Continuar",460,530,NEGRO,30)

        self.seleccion_escogida = self.selecciones[selec[0]]

        self.marcado = [False,False,False,False,False,False,False,False]

        self.marcado_pos_dim = [(10,10,180,180),(210,10,180,180),(410,10,180,180),(610,10,180,180),(10,310,180,180),(210,310,180,180),(410,310,180,180),(610,310,180,180) ]

        self.seleccion_texto_1 = Texto(" Seleccione hasta seis elementos.",50,230,NARANJA,30)

        self.cantidad_seleccionados = 0

    def getNombre(self):
        return self.nombre

    def transicion(self):
        self.fin_aparece = False
        self.tiempo = 0
        self.accion = False

    def en_evento(self,evento):
        if(self.accion == True):

            for i in range (len(self.seleccion_escogida)):
                if(self.seleccion_escogida[i].es_click()):

                    if(self.sonidoAct == True):
                        self.seleccion_escogida[i].reproducir()
                    if(self.marcado[i]==False):
                        if(self.cantidad_seleccionados<6):
                            self.marcado[i]= True
                            self.cantidad_seleccionados = self.cantidad_seleccionados  + 1
                    else:
                        self.marcado[i]= False
                        self.cantidad_seleccionados = self.cantidad_seleccionados  - 1
            if(self.boton_ok.es_click()):
                if(self.sonidoAct == True):
                    self.boton_ok.reproducir()
                if(self.cantidad_seleccionados > 0):
                    self.lista_selec = []
                    for e in range (len(self.marcado)):
                        if(self.marcado[e] == True):
                            self.lista_selec.append(self.seleccion_escogida[e])
                    return "SELECCIONADOS"

##            for i in range (len(self.seleccion_escogida)):
##                if(self.seleccion_escogida[i].es_pisado()):
##                    self.seleccion_escogida[i].centery = 175
##                    self.marcado_pos_dim[i] = (100,100,100,100)
##                else:
##                    self.seleccion_escogida[i].centery = 175
##                    self.marcado_pos_dim[i] = (100,100,100,100)
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

            self.seleccion_texto_1.dibujar(pantalla)

            for i in range (len(self.marcado)):
                if(self.marcado[i] == True):

                    pygame.draw.rect(pantalla, NARANJA, self.marcado_pos_dim[i])

            for seleccion in self.seleccion_escogida:
                pantalla.blit(seleccion.image,seleccion.rect)
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

