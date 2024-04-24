from sala import Sala
from aluno import Aluno
from professor import Professor
from curso import Curso
from disciplina import Disciplina
from servidor import Servidor
from diretor import Diretor
from coordenador import Coordenador



class Menu :

    def __init__(self):
        self.value=0
    def exibirMenu(self):
        aluno = Aluno()
        prof= Professor()
        curso= Curso()
        disci=Disciplina()
        sala= Sala()
        servidor= Servidor()
        diretor = Diretor()
        coord= Coordenador()
        while True:
            optionMenu = int(input("*** Bem vindo ao casdatro do Aluno da Uast ***\n"
                           "[ 1 ]- Cadastar Aluno\n"
                           "[ 2 ]- Listar Alunos\n"
                           "[ 3 ]-Buscar Aluno\n"
                           "[ 4 ]-Professores\n"
                           "[ 5 ]-Servidores\n"
                           "[ 6 ]-Diretor\n"
                           "[ 7 ]-Coordenador\n"
                           "[ 8 ]-Cursos\n"
                           "[ 9 ]-Disciplinas\n"
                           "[ 10 ]-Salas\n"
                           "[ 0 ]-Sair\n"
                           "Escolha uma opção:"))
            if optionMenu == 1:
                aluno.cadastrarAluno()
            elif optionMenu == 2:
                aluno.listarAlunos()
            elif optionMenu == 3:
                aluno.buscarAluno()
            elif optionMenu == 4:
                 prof.listar()
            elif optionMenu == 5:
                servidor.listar()
            elif optionMenu == 6:
                diretor.listar()
            elif optionMenu == 7:
                coord.listar()
            elif optionMenu == 8:
                curso.listCursos()
            elif optionMenu == 9:
                disci.listDisci()
            elif optionMenu == 10:
                sala.listSala()
            elif optionMenu == 0:
                break
            else:
                print("\n***Opção não disponivel!***\n")


adm=Menu()
adm.exibirMenu()