from pessoa import pessoa

class pessoaJuridica (pessoa):

    def __int__(self, nome, endereco, cnpj, razao_social, data_abertura):
        super() .__init__(nome, endereco)
        self._cnpj = cnpj
        self._razao_social = razao_social
        self._data_abertura = data_abertura

