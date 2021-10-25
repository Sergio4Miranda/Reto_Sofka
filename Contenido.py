import xlrd

class Contenido():
    #carga el contenido que son preguntas, nivel y respuestas
    #
    def __init__(self):
        wb=xlrd.open_workbook('Preguntas_respuestas.xlsx') 
        self.hoja = wb.sheet_by_index(0)
    
