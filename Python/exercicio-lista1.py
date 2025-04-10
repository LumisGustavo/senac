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
    avaliacao = float (input("Digite sua nota: "))

    if avaliacao >= 7:
        print("Você foi aprovado")

    elif avaliacao >= 5 <=6.9:
        print("Você está de recuperação")

    else:
        print("Você foi reprovado")

nota()

"""Calculadora de Horas Trabalhadas"""
def trabalho():
    print("Calcule suas Horas Trabalhadas")
    print("Valor da hora: R$6.30")
    horas= float(input("Digite suas horas de jornada: "))

    horacalculada = (horas) * 6.3
    horaextra1 = 50.4
    horaextra2 = (horas) - 8

    if horacalculada <= 8:
        print(f"Você recebeu: R${horacalculada}")

    elif horacalculada >= 8.1:
        print(f"Você recebeu: R${horaextra1}")
        print(f"Suas horas extras {horaextra2} estão contabilizadas no banco de dados")

trabalho()
