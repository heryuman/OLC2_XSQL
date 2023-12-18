class TBL:
    def __init__(self,db_name,tbl_name):
        self._db_name=db_name
        self._tb_name=tbl_name
        self._columns=[]

    def insert_column(self,column):
        self._columns.append(column)
    
    def get_db_name(self):
        return self._db_name
    
    def get_tb_name(self):
        return self._tb_name
    
    