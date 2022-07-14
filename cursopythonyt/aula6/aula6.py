"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Luiz'
idade = 28
altura = 1.67
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
imc =  peso / (altura ** 2)

print(nome, 'tem', idade, ' anos de idade e seu imc é', imc)

print(idade * altura)

print(nome)
print(nome, type(nome))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
