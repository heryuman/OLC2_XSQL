from FuncionesDeSistema.Fun_Suma import Fun_Suma
from Arbol.Arbol import Arbol
from Arbol.Nodo import Nodo

def trySuma():
    funcion = Fun_Suma()

    salida = funcion.getSuma("base1","tabla1", "columna1")

    print(salida)

def validarArbol():
    nodo1= Nodo('suma','+',0,1)
    arbol = Arbol(nodo1)
    
    nodo1_1 = Nodo('num','1',1,0)
    nodo2 = Nodo('multi','*',1,1)
    nodo2_1 = Nodo('num','5',1,1)
    nodo2_2 = Nodo('num','6',1,1)
    
    nodo1.addHijo(nodo1_1)
    nodo1.addHijo(nodo2)
    nodo2.addHijo(nodo2_1)
    nodo2.addHijo(nodo2_2)
    
    

    arbol.graficarAST()

def main():
    #print("Hola mundo2")
    #trySuma()
    validarArbol()







if __name__ == "__main__":
    main()