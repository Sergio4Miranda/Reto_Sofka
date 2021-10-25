from Contenido import *
from Ronda import *
from Premio import *
from Registro import *
import time
import os


def main():            
    
    #inicio de juego
    print("........Bienvenido al juego reto matemático..........")
    print("")
    print("")
    print("El reto se compone de 5 preguntas")
    print("a medida que respondas bien la dificultad aumenta")
    print("y mayores serán tus puntos")
    print("")
    print("")
    print("Buena suerte")
    print("")
    print("")
    time.sleep(6)
    print("**********************************************")
    print("Ingrese su nickname")
    nombre=input();
    acumulado=0
    contenido=Contenido()
    #contenido de la prueba
    hoja=contenido.hoja
    # nivel de ficultal, maximo 5
    nivel=1
    i=1
    while i<6:
        print("")
        print("")
        print("Pregunta", nivel)
        #carga pregunta, posibles respuestas y repuesta correcta
        ronda=Ronda(nivel,hoja)
        pregunta=ronda.tomaPregunta()
        #imprime pregunta
        ronda.imprimirPregunta(pregunta)
        respuestas=ronda.tomaRespuestas()
        #imprime posibles respuestas
        ronda.imprimirRespuestas(respuestas)
        #jugador ingresa posible respuesta
        print("")
        print("Escriba el numero de su respuesta, por ejemplo 1:")
        respuestaJugador=int(input())
        correcto=False
        # si reponde bien
        puntos=0
        if respuestas[4]==respuestas[respuestaJugador-1] :
            correcto=True
            puntos=100*nivel
        acumulado+=puntos;
        premio=Premio(nivel,acumulado,nombre,correcto)
        i+=premio.retiro()
        if i>5:
           Registro(nombre,nivel,acumulado) 
        nivel+=1     
    

if __name__=="__main__":
    main()