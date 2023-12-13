from datetime import datetime

class Fun_Hoy:
    def __init__(self):
        self._result: str = None

    
    def getToday(self)-> str:
        self._result = ""
        formato = "%d-%m-%Y %H:%M:%S"
        today = datetime.now()

        self._result = today.strftime(formato)

        return self._result

