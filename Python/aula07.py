"""Bibliotecas"""
"""Biblioteca math"""
import math

def operacoes_matematicas():
    numero = float(input("Digite um número: "))
    raiz = math.sqrt(numero)
    potencia = math.pow(numero, 2)

    print("A raiz quadrada do número é: ", raiz)
    print("A potência do número é: ", potencia)

operacoes_matematicas()

"""Biblioteca random"""
import random

def numero_da_sorte(): #(Vulgo Biscoitin Chines)
    print("Vamos sortear um número de 1 até 10: ")
    numero = random.randint(1, 10)
    print("O número da sorte é: ", numero)

numero_da_sorte()

from datetime import datetime

def mostrar_data_hora():
    agora = datetime.now()
    print("A data e hora de agora é: ")
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

mostrar_data_hora()