from datetime import date
from curso import Curso

class Matricula:
    def __init__(self, numero_matricula, data_matricula, curso, aluno, contratante):
        self.numero_matricula = numero_matricula
        self.data_matricula = data_matricula
        self.curso = curso
        self.aluno = aluno
        self.contratante = contratante