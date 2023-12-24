from abc import ABC, abstractmethod

class Expresion(ABC):

    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
        self.trueLbl = ''
        self.falseLbl = ''

    @abstractmethod
    def compilar(self, tree, table):
        pass

    def getTrueLbl(self):
        return self.trueLbl
    
    def getFalseLbl(self):
        return self.falseLbl
    
    def setTrueLbl(self, trueLbl):
        self.trueLbl = trueLbl
    
    def setFalseLbl(self, falseLbl):
        self.falseLbl = falseLbl