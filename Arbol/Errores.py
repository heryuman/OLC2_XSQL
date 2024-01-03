class Errores:
    def __init__(self,descripcion,tipo, linea, columna):
        self._descripcion =descripcion
        if tipo== 1:
            self._tipo="Lexico"
        else:
            self._tipo="Sintáctico"
        self._linea=linea
        self._columna=columna