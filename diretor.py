from servidor import Servidor

class Diretor(Servidor):
    def __init__(self):
        super().__init__()
        self.listarNomes = ['Carlos Figueira']

    def listar(self):
        for i in self.listarNomes:
            print(i)
        return
