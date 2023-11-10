from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, cpf, data_nascimento, pessoa):
        super().__init__(pessoa.nome, pessoa.endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.pessoa = pessoa