class Premio():
    def __init__(self,nivel=0,acumulado=0, nombre="",correcto=False):
        self.nivel=nivel
        self.acumulado=acumulado
        self.nombre=nombre
        self.correcto=correcto
        
    #pregunta al jugador si se quire retirar
    def retiro(self):
        #si la pregunta fue contestada correctamente
        if self.correcto==True and self.nivel<5:
            print("")
            print("")
            print("¿Quieres seguir o te retiras?")
            print("si sigues escribe s de lo contrario n")
            sigue=input()
            if sigue=='s':
                self.puntaje()
                return 0
            else:
                #si se retira el jugador
                self.finalJuego()
                return 6
        #no responde bien
        else:
            self.finalJuego()
            return 6
    #mensaje de fin del juego
    def finalJuego (self):
        print("")
        print("")
        print("***************GAME OVER************************")
        print(self.nombre,"tu puntaje total es:",self.acumulado)
    #mensaje de puntos hasta el momento
    def puntaje (self):
        print("")
        print("")
        print(self.nombre,"tu puntaje actual es:",self.acumulado)
            
       
