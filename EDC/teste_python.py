# Código para testar funcionamento do Python
import datetime

nome = input("Digite seu nome:")
ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atua = datetime.date.today().year
idade = ano_atua-ano_nasc

print("Olá, meu nome é {}, eu nasci em {} e tenho {} anos.".format(nome, ano_nasc, idade))