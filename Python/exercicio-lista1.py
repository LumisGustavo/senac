"""Verificador de Acesso de Festa"""

def verificador():
    print("Validação de Maioridade")
    idade= int (input("Digite a sua idade: "))

    if idade >= 18:
        print("Acesso Aprovado")
    else:
        print("Acesso Negado")

verificador()

"""Calculadora de Desconto"""

def desconto():
    print("Descontos de 10% em compras de mais de R$100,00!!!!")
    valor= int (input("Valor da compra: "))

    if valor > 100:
        print(valor-valor*0.1)

    else:
        print("Desconto Indisponível")

desconto()

"""Avaliação de Nota Escolar"""
def nota():
    print("Avaliação de Boletim")
    avaliacao= int (input("Digite sua nota: "))