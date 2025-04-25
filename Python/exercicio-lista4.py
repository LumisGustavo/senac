"""1 - Calculadora Científica Simples"""
import math

def calculadora_cientifica():
    numero = float(input("Digite um número: "))
    raiz = math.sqrt(numero)
    seno = math.sin(numero)
    cosseno = math.cos(numero)
    log = math.log(numero)

    print("A raiz quadrada do número é: ", raiz)
    print("O seno do número é: ", seno)
    print("O cosseno do número é: ", cosseno)
    print("O logaritmo natural do número é: ", log)

calculadora_cientifica()

"""2 - Simulador de Dado"""
import random

def simulador_dado():
    print("Role um dado e irá cair um número de 1 a 6")
    while True:
        dado = input("Deseja rolar o dado? Sim/Não:" )
        numero = random.randint(1, 6)

        if dado.lower() == "sim":
            print(numero)

        elif dado.lower() == "não":
            print("Até a próxima!")
            break

        else:
            print(f"Perdão, não reconheci oq foi dito.")


simulador_dado()

"""3 - Agenda Digital"""
from datetime import datetime

def agenda():
    agora = datetime.now()
    data = (agora.strftime("%d/%m/%Y"))
    horas = (agora.strftime("%H:%M:%S"))
    print(f"Hoje é dia {data} e agora são {horas}.")

    while True:
        agenda = input("Deseja agendar um compromisso? (Sim/Não): ")

        if agenda.lower() == "sim":
            compromisso = input("Digite seu compromisso: ")
            diacompromisso = input("Digite a data do seu compromisso: (escreva no formato dia/mês/ano): ")
            print(compromisso, diacompromisso)

        elif agenda.lower() == "não":
            print("Obrigado pela preferência!")
            break

        else:
            print("Não compreendi a mensagem.")

agenda()

"""4 - Cronômetro"""
import time

def cronometro():
    cronometro = int(input("Digite o tempo em segundos para ser cronometrado: "))

    for i in range(cronometro, 0, -1):
        segundos = i % 60
        minutos = int(i / 60) % 60
        print(f"{minutos:02}:{segundos:02}")
        time.sleep(1)

    print("Tempo encerrado!")

cronometro()

"""5 - Organizador de Pastas"""

"""6 - Analisador de Dados Numéricos"""
import statistics
def analise():
    numeros = []
    for i in range (5):
        numero = float(input(f"Digite o {i + 1}° número: "))
        numeros.append(numero)

    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    moda = statistics.mode(numeros)
    print(f"A média é: {media:.2f}")
    print("A mediana é: ",mediana)
    print("A moda é: ",moda)

analise()

"""7 - Descubra o Dia da Semana"""
import datetime

def descobrir_dia():
    data_desejada = input("Insira a data no formato AAAA/MM/DD: ")
    especificacao = data_desejada.split('/')
    ano = int(especificacao[0])
    mes = int(especificacao[1])
    dia = int(especificacao[2])
    data = datetime.date(ano, mes, dia)
    dia_semana = data.weekday()
    dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
    print(f"A data {data_desejada} é/foi: {dias[dia_semana]}")

descobrir_dia()
