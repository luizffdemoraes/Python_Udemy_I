"""
 * Criar variáveis para nome (str), idade (int),
 * altura (float) e peso (float) de uma pessoa
 * Criar variáveis com o ano atual (int)
 * Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
 * Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
 * Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome: str = 'Luiz'
idade: int = 32
ano_atual: int = 2019
altura: float = 1.8
peso: int = 80
imc: float = peso / (altura ** 2)
ano_nascimento: int = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')

