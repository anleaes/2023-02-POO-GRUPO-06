from datetime import date
from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from curso import Curso
from matricula import Matricula

pessoa = Pessoa(nome="Fulano", endereco="Rua XYZ")
pessoa2 = Pessoa(nome="Ciclano", endereco="Rua ABC")
#print(f"Nome: {pessoa.nome}, Endereço: {pessoa.endereco}")

pessoa_fisica = PessoaFisica(cpf="123.456.789-01", data_nascimento=date(1990, 1, 1), pessoa=pessoa)
#print(f"CPF: {pessoa_fisica.cpf}, Data de Nascimento: {pessoa_fisica.data_nascimento}, Nome: {pessoa_fisica.nome}")

pessoa_juridica = PessoaJuridica(cnpj="12.345.678/0001-90", razao_social="Empresa ABC", data_abertura=date(2000, 1, 1), pessoa=pessoa2)
#print(f"CNPJ: {pessoa_juridica.cnpj}, Razão Social: {pessoa_juridica.razao_social}, Nome: {pessoa_juridica.nome}")

curso = Curso(nome="Python Avançado", carga_horaria="40 horas")
#print(f"Curso: {curso.nome}, Carga Horária: {curso.carga_horaria}")

matricula = Matricula(numero_matricula=1, data_matricula=date.today(), curso=curso, aluno=pessoa_fisica, contratante=pessoa_juridica)
print(f"Matrícula Nº: {matricula.numero_matricula}, Data de Matrícula: {matricula.data_matricula}")
print(f"Curso: {matricula.curso.nome}, Aluno: {matricula.aluno.nome}, Contratante: {matricula.contratante.nome}")
