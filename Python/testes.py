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