class Fun_Substraer:
    def __init__(self):
        self._result:str = None

    def getSubstraer(self, cadena:str, inicio:int, final:int)-> str:
        self._result =""
        if inicio < 0:
            inicio = 0
        if final > len(cadena):
            final = len(cadena)

        # Utilizar la notación de slices para extraer la subcadena
        self._result = cadena[inicio:final]

        return self._result