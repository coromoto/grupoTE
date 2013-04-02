#-------------------------------------------------------------------------------
#Modulo: gravedad
#
#Contenido: algunas constantes y funciones sobre fisica gravitatoria
#
#Autor: Coromoto Leon
#
#Referencia: Introduccion a la programacion con Python. Marzal y Garcia. 2006
#
#-------------------------------------------------------------------------------
#Constantes:
# G: Constante de gravitacion universal
# M_Tierra: Masa de la Tierra en kilos
# R_Tierra: Radio de la Tierra en metros
# M_Luna: Masa de la Luna en kilos
# R_Luna: Radio de la Luna en metros
#
#Funciones:
#
# fuerza_gravitatoria: calcula la fuerza gravitatoria existente entre dos cuerpos
#   entrada:
#     M: masa de un cuerpo en kilogramos
#     m: masa de otro cuerpo en kilogramos
#     r: distancia entre ellos en metros
#   salida:
#     fuerza en Newtons
#
# distancia: calcula la distancia que separa dos cuerpos atraidos por una fuerza
#            gravitatoria determinada
#   entrada:
#     M: masa de un cuerpo en kilogramos
#     m: masa de otro cuerpo en kilogramos
#     F: fuerza gravitatoria experimentada en metros
#   salida:
#     distancia en metros
#
# velocidad_escape: calcula la velocidada necesaria para escapar de la atraccion
#                   gravitatoria de un cuerpo esferico
#   entrada:
#     M: masa de un cuerpo en kilogramos
#     R: radio del cuerpo en metros
#   salida:
#     velocidad en metros por segundo
#
#-------------------------------------------------------------------------------
#Historia:
#   * Creado el 01.12.2010
#   * Modificado el 15.12.2011:
#      - se incluyen estos comentarios
#      - se incluye la prueba del modulo
#-------------------------------------------------------------------------------

from math import sqrt

G = 6.67e-11
M_Tierra = 5.97e24
R_Tierra = 6.37e6
M_Luna = 7.35e22
R_Luna = 1.74e6

def fuerza_gravitatoria(M, m, r):
  return G * ((M * m) / (r ** 2))

def distancia(M, m, F):
  return sqrt(G * M * m / F)

def velocidad_escape(M, R):
  return sqrt(2 * G * M / R)

ve_Tierra = velocidad_escape(M_Tierra, R_Tierra)
ve_Luna = velocidad_escape(M_Luna, R_Luna)
