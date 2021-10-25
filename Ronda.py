import random

class Ronda():

    def __init__(self,nivel,hoja):
        self.hoja=hoja
        self.nivel=nivel
        #escoge un numero al  azar entre 1 y 5
        self.aleatorio=random.randrange(1, 6, 1)
        #guarda la posicion de la fila de la pregunta aleatoria
        self.fila=(self.nivel-1)*5+self.aleatorio

    #escoge la pregunta
    def tomaPregunta(self):
        p=self.hoja.cell_value(self.fila, 2)
        return p
    #dependiendo de la pregunta toma las repuestas
   #incluyendo la corecta en la ultima posicion
    def tomaRespuestas(self):
        res=[]
        for i in range(3, 8, 1):
            r=self.hoja.cell_value(self.fila, i)
            res.append(r)
        return res
    #imprime pregunta
    def imprimirPregunta(self,pregunta=""):
        print(pregunta)
    #imprime posibles respuestas
    
    def imprimirRespuestas(self,respuestas=[]):
        res=['1','2','3','4']
        for i in range(0,4):
            print(res[i],".",respuestas[i])

        
        
        
        
        