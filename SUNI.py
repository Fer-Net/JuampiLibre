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
import random
import webbrowser

from DIRECTOR_DE_ESCENAS import*
pygame.init()
dimensiones = [800,600]
pantalla = pygame.display.set_mode(dimensiones)#,pygame.FULLSCREEN
pygame.display.set_caption("Suni")

##if(random.randint(0,10)==10):
##webbrowser.open("http://www.python.org", new=2, autoraise=True)

director = DirectorJuego(pantalla)
while director.en_accion():
    director.accion()
pygame.quit()


#armar una biblioteca mas potente


#CUANDO HAGA CLICK EN LOS SONIDOS QUE SELECCIONA QUE SUENE


#animar todos los botones que faltan (como los de juego)
#la escena calibracion cambiarla por la escena.seleccion.rutina
#para completar "tutorial" hay qu tener todo listo
#hacer la clase paraffo para los textos


