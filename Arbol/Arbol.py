from Arbol.Nodo import Nodo
from enviroment import enviroment
from pathlib import Path
import os, subprocess

class Arbol:
    
    def __init__(self, raiz: Nodo):
        self._raiz = raiz
        self._env = enviroment()

    
    def graficarAST(self):
        grafica_str:str = "digraph ast{\n"+self.graficaNodos(self._raiz,"0")+"\n}"
        self.generaGrafo(grafica_str)

    def graficaNodos(self, nodo:Nodo, i:str)->str:
        k:int=0
        r:str = ""
        nodoTerm:str =  nodo._lexema
        nodoTerm= nodoTerm.replace("\"", "")

        r = "node"+i+"[label =\""+nodoTerm +"\"];\n"

        for elemento in nodo._hijos:
            r = r +"node"+str(i)+" -> node"+str(i)+str(k)+"\n"

            r= r+ self.graficaNodos(elemento, str(i)+str(k))
            k=k+1

        
        
        return r
    
    def generaGrafo(self, stringTree:str):

        if os.path.exists(self._env._rutaAST):
            self.crearArchivo(self._env.fullPath, stringTree)
        else:
            nuevoDir =  Path(self._env._rutaAST)
            nuevoDir.mkdir()

            if os.path.exists(self._env._rutaAST):
                self.crearArchivo(self._env.fullPath, stringTree)
            
        
    def crearArchivo(self, path:str, body:str):
        with open(path, 'w') as archivo:
            archivo.write(body)
            
        
        result = subprocess.run(self._env._comandoGraphviz, shell=True)
            
        print(result)

        