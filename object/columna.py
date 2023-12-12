class COLUMNA:
    def __init__(self,nombrecol, tipo, pk, nul_l, valor, tamanio, presicion, colreference,tablareference ):
        self.nombrecol=nombrecol
        self.tipo=tipo
        self.pk = pk
        self.nul_l = nul_l
        self.valor=valor
        self.tamanio = tamanio
        self.presicion = presicion
        self.referencia = colreference
        self.tablareference = tablareference