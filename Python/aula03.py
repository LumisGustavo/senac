"""Variáveis"""
aluno = "Gustavo"
nota1 = 9.8

"""Funções"""
def calcular_media():
    print("Boletim Escolar")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 6:
        print(f"Sua média foi {media}, você foi aprovado")

    else:
        print(f"Sua média foi {media}, você está cursando")

calcular_media()

"""Estrutura de repetição"""
def contar_ate_dez():
    partida = int(input("Ponto de Partida: "))
    chegada = int(input("Ponto de chegada: "))
    for numero in range (partida ,chegada):
        print (numero)

contar_ate_dez()

def tabuada():
    print("Tabuada de 1 a 10")
    numero = int(input("Digite um número: "))

    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabuada()

def media_notas():
    soma = 0
    for i in range (4):
        nota = float (input(f"Digite a {i + 1} nota: "))
        soma += nota
    media = soma / 4
    print("A média é: ", media)

media_notas()