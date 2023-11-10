from pessoa import pessoa

class pessoaFisica(pessoa):

    def __int__(self, nome, endereco, cpf, data_nascimento):
        super() .__init__(nome, endereco)
        self._cpf = cpf
        self._data_nascimento = data_nascimento
