from pessoa1 import Pessoa1
from pessoa2 import Pessoa2
from pessoa3 import Pessoa3


abacate = Pessoa1 (
                   input ("Digite seu nome:>>"),
                   input('Digite seu sobrenome:>>'),
                   input('Digite sua idade:>>'),
                   input('Digite seu peso:>>'),
                   input('Digite seu cpf:>>'),
                   input('Digite sua Altura:>>')
                   )
                                  
                   
laranja = Pessoa2()

moranguinho = Pessoa3()

laranja.Nome = abacate.Nome
laranja.Sobrenome = abacate.Sobrenome
laranja.Idade = abacate.Idade
laranja.Peso = abacate.Peso
laranja.Cpf = abacate.Cpf
laranja.Altura = abacate.Altura

moranguinho.Nome = laranja.Nome
moranguinho.Sobrenome = laranja.Sobrenome
moranguinho.Idade = laranja.Idade
moranguinho.Peso = laranja.Peso
moranguinho.Cpf = laranja.Cpf
moranguinho.Altura = laranja.Altura

print(moranguinho)







 


