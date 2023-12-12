class COLUM:
    def __init__(self,cname,tipo,pk,col_ref,col_size,isNull):
        self._column_name=cname
        self._type=tipo
        self._pk=pk
        self._isNull=isNull
        self._col_fer=col_ref
        self._col_size=col_size