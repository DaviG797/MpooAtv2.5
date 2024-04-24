from servidor import Servidor

class Professor(Servidor):
    def __init__(self):
        super().__init__()
        self.listasProf = ['Joao Bento']
    def listar(self):
        for i in self.listasProf:
            print(i)
        return