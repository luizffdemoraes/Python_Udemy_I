nome = 'Luiz'
idade = 28
altura = 1.67
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
imc =  peso / (altura ** 2)

print(nome, 'tem', idade, ' anos de idade e seu imc é', imc)
print(f'{nome} tem {idade}, anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i}, anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
# 0, 1 e 2