class enviroment:

    def __init__(self) -> None:
        self._rutaAST = "./Graficas"
        self._nameASTFile = "ast.dot"
        self.fullPath=self._nameASTFile
        self._comandoGraphviz = "dot -Tpng "+str(self._nameASTFile)+" -o ast.png"
        self.useDB = "UseDB"
        self.dbNotFound = "No hay ninguna base de datos previamente selecionada."