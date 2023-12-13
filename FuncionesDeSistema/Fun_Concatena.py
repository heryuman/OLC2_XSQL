from typing import List

class Fun_Concatena:
    def __init__(self):
        self._result:str = None

    def getConcatena(self, a_concatenar: List[str])->str:

        self._result = ""
        for elemento in a_concatenar:
            self._result = self._result + elemento
        return self._result