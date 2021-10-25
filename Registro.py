from openpyxl import load_workbook

class Registro():
    # guarda la informacion del jugador en historico
    def __init__(self,nombre="",nivel=0,acumulado=0):
        datos=[nombre,nivel,acumulado]
        archivo='historico.xlsx'
        wb = load_workbook(archivo)
        page = wb.active
        page.append(datos)
        wb.save(archivo)