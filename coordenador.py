from servidor import Servidor

class Coordenador(Servidor):
    def __init__(self):
        super().__init__()
        self.listarNomes = ['Natalia Guimaraes']

    def listar(self):
        for i in self.listarNomes:
            print(i)
        return