class Puntaje():
    def __init__(self,nivel):
        self.bandera=False
        self.nivel=nivel
        
    #pregunta al jugador si se quire retirar
    def retiro(self,acumulado):
        print("")
        print("")
        print("¿Quieres seguir o te retiras?")
        print("si sigues escribe s de lo contrario n")
        sigue=input()
        if sigue=='s':
            self.bandera=True
        else:
            self.bandera=False
        
