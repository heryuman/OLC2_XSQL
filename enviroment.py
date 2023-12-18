class enviroment:

    def __init__(self) -> None:
        self._rutaAST = "./Graficas"
        self._nameASTFile = "ast.dot"
        self.fullPath=self._rutaAST+"/"+self._nameASTFile
        self._comandoGraphviz = "dot -Tpng "+self.fullPath+" -o ast.png"
