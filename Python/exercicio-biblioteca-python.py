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

while True:
    def simulador_dado():
        print("Role um dado e irá cair um número de 1 a 6: ")
        numero = random.randint(1, 6)
        print("O número é: ", numero)
