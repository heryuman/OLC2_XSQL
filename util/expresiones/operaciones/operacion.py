from util.generic import *
from util.interfaces.expresion import Iexpresion

class OPERACION (Iexpresion):
    
    def __init__(self,exp1,exp2,sign_operador,linea,column):
        self._exp1=exp1
        self._exp2=exp2
        self._linea=linea
        self._col=column
        self._sign_operador=sign_operador
        self._operador=OPERADOR(sign_operador)._toperador

    def getTipo(controlador, tablaSimbolo):
        pass
    
    def getValor(controlador, tablaSimbolo):
        pass
    