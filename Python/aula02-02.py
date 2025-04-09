def calculadora():
    print("Bem-Vindo a nossa calculadora!")
    print("Operações disponíveis: soma, subtracao, multiplicacao, divisao")
    operacao = input("Digite por extenso a operação: ").lower()
    numero1 = float(input("Digite o primeiro número:"))
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "soma":
        resultado = numero1+numero2
        print(f"O resultado é {resultado} ")
    elif operacao == "subtracao":
        resultado = numero1-numero2
        print(f"O resultado é {resultado} ")
    elif operacao == "multiplicacao":
        resultado = numero1*numero2
        print(f"O resultado é {resultado} ")
    elif operacao == "divisao":
        if numero2 != 0:
            resultado = numero1/numero2
            print(f"O resultado é {resultado} ")
        else:
            print("Operação Indefinida")
    else:
        print("Operação Inválida")