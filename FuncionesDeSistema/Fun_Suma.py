from typing import List
from object.columna import COLUMNA;


class Fun_Suma:
    def __init__(self):
        self._result: str = None

    def getSuma (self, database:str, tablename:str, column: str)-> str:

        #objeto de tipo columna para validar el tipo de dato
        o_column = COLUMNA("col","decimal",None,None,None,None,None,None, None)

        self._result = 0.0

        if (o_column.tipo=='decimal' or o_column.tipo =='integer'):
            
            #recorremos todos los registros que cumplan la condicion

            self._result = 10.76

        

        

        return str(self._result)
