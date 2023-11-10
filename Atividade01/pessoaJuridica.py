from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social, data_abertura, pessoa):
        super().__init__(pessoa.nome, pessoa.endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data_abertura = data_abertura
        self.pessoa = pessoa