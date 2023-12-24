class COLUM:
    def __init__(self,cname,tipo,pk,col_ref,tab_ref,col_size,valor,isNull,presicion):
        self._column_name=cname
        self._type=tipo
        self._pk=pk
        self._isNull=isNull
        self._valor=valor
        self._col_size=col_size
        self._presicion=presicion
        self._col_fer=col_ref
        self._tab_refernce=tab_ref