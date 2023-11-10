class Pessoa{
    - nome: String 
    - endereco: String
    + construtor(nome, endereco)
}

class PessoaFisica{
    - cpf: String
    - data_nascimento: Date 
    - pessoa: Pessoa
    + construtor(cpf, data_nascimento, pessoa)
}

class PessoaJuridica{
    - cnpj: String
    - razao_social: String
    - data_abertura: Date
    - pessoa: Pessoa
    + construtor(cnpj, data_abertura, pessoa)
}

class Matricula{
    -numero_matricula
    -data_matricula
    -curso: Curso
    -aluno: PessoaFisica
    -contratante: Pessoa 
    + construtor(numero_matricula, data_matricula, curso, aluno, contratante)
}

class Curso {
    -Nome String 
    -carga_horaria String
    + construtor(nome, carga_horaria)
}
