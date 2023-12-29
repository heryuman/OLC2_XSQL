
from util.interfaces.expresion import Iexpresion
from util.expresiones.operaciones.operacion import OPERACION
class ARITMETICAS(Iexpresion):
    
    def __init__(self,exp1,operador,expresion2,linea, columna):
        self._exp1=exp1
        self._operador=operador
        self._exp2=expresion2
        self._linea=linea
        self._columna=columna
        super().__init__(exp1,expresion2,operador,linea,columna)
        
    def getTipo(controlador, tablaSimbolo):
        return super().getTipo(tablaSimbolo)