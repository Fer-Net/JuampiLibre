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
from Objetos import*
from configuracion import*

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([800,600],pygame.FULLSCREEN)
    salir=False
    reloj1=pygame.time.Clock()

    puede_jugar = True
    pos = (40,40)
    cambiarPos = False

    Texto1= Texto("",0,0,VIOLETA)

    COLOR_FONDO = AMARILLO
    Flecha_Tocada= False

    tecla = ""

    Texto_exp = Texto("F1,F2,F3,PARA CAMBIAR DE COLORES",500,550,NEGRO)
    Texto_exp.fuente = pygame.font.Font( "arial1.ttf", 10)
    Texto_exp1 = Texto("ESCAPE PARA SALIR",500,565,NEGRO)
    Texto_exp1.fuente = pygame.font.Font( "arial1.ttf", 10)
    Texto_exp2 = Texto("Proyecto Juega Juampi!",500,580,NEGRO)
    Texto_exp2.fuente = pygame.font.Font( "arial1.ttf", 10)

#--------------------------------------Aqui el ciclo de juego de entrada -----------------------------------------------------------------
    while salir!=True:
        for event in pygame.event.get():

            if(puede_jugar):
                if event.type == pygame.KEYDOWN:
                    Flecha_Tocada= False
                    tecla = ""
                    if event.key == pygame.K_BACKSPACE:
                        tecla ="-"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//BORRAR_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//BORRAR_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//BORRAR_BLANCA.png", True)

                    if event.key == pygame.K_RETURN:
                        tecla ="---"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//ENTER_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//ENTER_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//ENTER_BLANCA.png", True)


                    if event.key == pygame.K_ESCAPE:
                        salir= True
                        tecla ="ESCAPE"

                    if event.key == pygame.K_RALT:
                        tecla ="ALT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//ALT_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//ALT_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//ALT_BLANCA.png", True)

                    if event.key == pygame.K_LALT:
                        tecla ="ALT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//ALT_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//ALT_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//ALT_BLANCA.png", True)

                    if event.key == pygame.K_CAPSLOCK:
                        tecla ="MAYUS"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//MAYUS_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//MAYUS_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//MAYUS_BLANCA.png", True)

                    if event.key == pygame.K_SPACE:
                        tecla ="_"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//ESPACIO_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//ESPACIO_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//ESPACIO_BLANCA.png", True)


                    if event.key == pygame.K_RSHIFT:
                        tecla ="SHIFT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//SHIFT_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//SHIFT_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//SHIFT_BLANCA.png", True)

                    if event.key == pygame.K_LSHIFT:
                        tecla ="SHIFT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//SHIFT_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//SHIFT_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//SHIFT_BLANCA.png", True)


                    if event.key == pygame.K_RCTRL:
                        tecla ="CONTROL"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//CONTROL_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//CONTROL_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//CONTROL_BLANCA.png", True)

                    if event.key == pygame.K_LCTRL:
                        tecla ="CONTROL"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//CONTROL_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//CONTROL_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//CONTROL_BLANCA.png", True)

                    if event.key == pygame.K_TAB:
                        tecla ="TABULADOR"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//TAB_VERDE.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//TAB_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//TAB_BLANCA.png", True)


                    if event.key == pygame.K_0:
                         tecla ="0"
                         Texto1.setPos(-60,190)
                    if event.key == pygame.K_1:
                        Texto1.setPos(-60,190)
                        tecla ="1"
                    if event.key == pygame.K_2:
                        Texto1.setPos(-60,190)
                        tecla ="2"
                    if event.key == pygame.K_3:
                        Texto1.setPos(-60,190)
                        tecla ="3"
                    if event.key == pygame.K_4:
                        Texto1.setPos(-60,190)
                        tecla ="4"
                    if event.key == pygame.K_5:
                        Texto1.setPos(-60,190)
                        tecla ="5"
                    if event.key == pygame.K_6:
                        Texto1.setPos(-60,190)
                        tecla ="6"
                    if event.key == pygame.K_7:
                        Texto1.setPos(-60,190)
                        tecla ="7"
                    if event.key == pygame.K_8:
                        Texto1.setPos(-60,190)
                        tecla ="8"
                    if event.key == pygame.K_9:
                        Texto1.setPos(-60,190)
                        tecla ="9"


                    if event.key == pygame.K_a:
                        Texto1.setPos(-60,190)

                        tecla ="A"
                    if event.key == pygame.K_b:
                        Texto1.setPos(-60,190)
                        tecla ="B"
                    if event.key == pygame.K_c:
                        Texto1.setPos(-60,190)
                        tecla ="C"
                    if event.key == pygame.K_d:
                        Texto1.setPos(-60,190)
                        tecla ="D"
                    if event.key == pygame.K_e:
                        Texto1.setPos(-60,190)
                        tecla ="E"
                    if event.key == pygame.K_f:
                        Texto1.setPos(-60,250)
                        tecla ="F"
                    if event.key == pygame.K_g:
                        Texto1.setPos(-60,190)
                        tecla ="G"
                    if event.key == pygame.K_h:
                        Texto1.setPos(-60,190)
                        tecla ="H"
                    if event.key == pygame.K_i:
                        Texto1.setPos(-60,300)
                        tecla ="I"


                    if event.key == pygame.K_j:
                        Texto1.setPos(-60,190)
                        tecla ="J"
                    if event.key == pygame.K_k:
                        Texto1.setPos(-60,190)
                        tecla ="K"
                    if event.key == pygame.K_l:
                        Texto1.setPos(-60,190)
                        tecla ="L"
                    if event.key == pygame.K_m:
                        Texto1.setPos(-60,190)
                        tecla ="M"
                    if event.key == pygame.K_n:
                        Texto1.setPos(-60,190)
                        tecla ="N"
                    if event.key == pygame.K_o:
                        Texto1.setPos(-60,190)
                        tecla ="O"
                    if event.key == pygame.K_p:
                        Texto1.setPos(-60,190)
                        tecla ="P"
                    if event.key == pygame.K_q:
                        Texto1.setPos(-60,190)
                        tecla ="Q"
                    if event.key == pygame.K_r:
                        Texto1.setPos(-60,190)
                        tecla ="R"
                    if event.key == pygame.K_s:
                        Texto1.setPos(-60,190)
                        tecla ="S"
                    if event.key == pygame.K_t:
                        Texto1.setPos(-60,190)
                        tecla ="T"
                    if event.key == pygame.K_u:
                        Texto1.setPos(-60,190)
                        tecla ="U"
                    if event.key == pygame.K_v:
                        Texto1.setPos(-60,190)
                        tecla ="V"
                    if event.key == pygame.K_w:
                        Texto1.setPos(-60,190)
                        tecla ="W"
                    if event.key == pygame.K_x:
                        Texto1.setPos(-60,190)
                        tecla ="X"
                    if event.key == pygame.K_y:
                        Texto1.setPos(-60,190)
                        tecla ="Y"
                    if event.key == pygame.K_z:
                        Texto1.setPos(-60,190)
                        tecla ="Z"
                    if event.key == pygame.K_DELETE:
                        Texto1.setPos(-60,190)
                        tecla ="DELETE"
                    if event.key == pygame.K_KP0:
                        Texto1.setPos(-60,190)
                        tecla ="0"
                    if event.key == pygame.K_KP1:
                        Texto1.setPos(-60,190)
                        tecla ="1"
                    if event.key == pygame.K_KP2:
                        Texto1.setPos(-60,190)
                        tecla ="2"
                    if event.key == pygame.K_KP3:
                        Texto1.setPos(-60,190)
                        tecla ="3"
                    if event.key == pygame.K_KP4:
                        Texto1.setPos(-60,190)
                        tecla ="4"
                    if event.key == pygame.K_KP5:
                        Texto1.setPos(-60,190)
                        tecla ="5"
                    if event.key == pygame.K_KP6:
                        Texto1.setPos(-60,190)
                        tecla ="6"
                    if event.key == pygame.K_KP7:
                        Texto1.setPos(-60,190)
                        tecla ="7"
                    if event.key == pygame.K_KP8:
                        Texto1.setPos(-60,190)
                        tecla ="8"
                    if event.key == pygame.K_KP9:
                        Texto1.setPos(-60,190)
                        tecla ="9"

                    if event.key == pygame.K_UP:
                        tecla ="UP"
                        Flecha_Tocada= True
                        if(COLOR_FONDO== VERDE):
                            flecha= cargar_imagen("Imagenes//FLECHA_ARRIBA_VERDECLARO.png", True)
                        if (COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//FLECHA_ARRIBA_VIOLETA.png", True)
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//FLECHA_ARRIBA_BLANCA.png", True)

                    if event.key == pygame.K_DOWN:
                        tecla ="DOWN"
                        Flecha_Tocada= True
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//FLECHA_ABAJO_BLANCA.png", True)
                        if(COLOR_FONDO == VERDE):
                            flecha= cargar_imagen("Imagenes//FLECHA_ABAJO_VERDECLARO.png", True)
                        if(COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//FLECHA_ABAJO_VIOLETA.png", True)

                    if event.key == pygame.K_RIGHT:
                        tecla ="RIGHT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//FLECHA_DERECHA_BLANCA.png", True)
                        if(COLOR_FONDO == VERDE):
                            flecha= cargar_imagen("Imagenes//FLECHA_DERECHA_VERDECLARO.png", True)
                        if(COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//FLECHA_DERECHA_VIOLETA.png", True)

                    if event.key == pygame.K_LEFT:
                        tecla ="LEFT"
                        Flecha_Tocada= True
                        if(COLOR_FONDO == NEGRO):
                            flecha= cargar_imagen("Imagenes//FLECHA_IZQUIERDA_BLANCA.png", True)
                        if(COLOR_FONDO == VERDE):
                            flecha= cargar_imagen("Imagenes//FLECHA_IZQUIERDA_VERDECLARO.png", True)
                        if(COLOR_FONDO == AMARILLO):
                            flecha= cargar_imagen("Imagenes//FLECHA_IZQUIERDA_VIOLETA.png", True)


                    if event.key == pygame.K_F1:
                        Texto1.setColor(BLANCO)
                        COLOR_FONDO = NEGRO
                        tecla =""
                    if event.key == pygame.K_F2:
                        Texto1.setColor(VIOLETA)
                        COLOR_FONDO = AMARILLO
                        tecla =""

                    if event.key == pygame.K_F3:
                        Texto1.setColor(VERDECLARO)
                        COLOR_FONDO = VERDE

                        tecla =""


                    if(tecla !=""):
                        winsound.PlaySound("Sonidos teclas\\" + tecla + ".wav",winsound.SND_ASYNC)
                        Texto1.setTexto(tecla)

            if event.type ==pygame.QUIT:
                salir=True

        reloj1.tick(20)

#--------------------------------------Aqui se pinta todo -----------------------------------------------------------------
        pantalla.fill(COLOR_FONDO)
        if( Flecha_Tocada== True):

            pantalla.blit(flecha, (40,-60))
        else:
            Texto1.dibujar(pantalla)
        Texto_exp.dibujar(pantalla)
        Texto_exp1.dibujar(pantalla)
        Texto_exp2.dibujar(pantalla)


        pygame.display.update()

    pygame.quit()

main()

