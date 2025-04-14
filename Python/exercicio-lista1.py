"""1 - Verificador de Acesso de Festa"""

def verificador():
    print("Validação de Maioridade")
    idade= int (input("Digite a sua idade: "))

    if idade >= 18:
        print("Acesso Aprovado")
    else:
        print("Acesso Negado")

verificador()

"""2 - Calculadora de Desconto"""

def desconto():
    print("Descontos de 10% em compras de mais de R$100,00!!!!")
    valor= int (input("Valor da compra: "))

    if valor > 100:
        print(valor-valor*0.1)

    else:
        print("Desconto Indisponível")

desconto()

"""3 - Avaliação de Nota Escolar"""
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

"""4 - Calculadora de Horas Trabalhadas"""
def trabalho():
    print("Calcule suas Horas Trabalhadas")
    print("Valor da hora: R$6.30")
    horas= float(input("Digite suas horas de jornada: "))

    horacalculada = (horas) * 6.3
    horaextra1 = 50.4
    horaextra2 = (horas) - 8

    if horas <= 8 and horas >= 0:
        print(f"Você recebeu: R${horacalculada}")

    elif horas >= 8.1:
        print(f"Você recebeu: R${horaextra1}")
        print(f"Suas horas extras {horaextra2} estão contabilizadas no banco de dados")

    else:
        print("Não foi possível realizar o cálculo")

trabalho()

"""5 - Classificador de Temperatura"""
def temperatura():
    print("Como está a temperatura?")
    celsius = int(input("Temperatura atual em Celsius: "))

    if celsius <= 18:
        print("Freezer")

    elif celsius >= 18 and celsius <= 25:
        print("Ta massa")

    elif celsius >= 25:
        print("Inferno")
        
temperatura()

"""6 - Verificador de Senha"""
def senha():
    senha = str(input("Digite sua senha: "))

    if senha == "senac123":
        print("Acesso Garantido")
    else:
        print("Acesso Negado")

senha()

"""7 - Conversor de Moedas"""
def moedas():
    print("Convertor de Real para Dólar")
    print("Valor do Dólar= R$5.20")
    moeda = float(input("Digíte um valor em real: "))

    real = moeda / 5.2

    if moeda >= 0:
        print(f"A conversão para Dólar é: ${real}")

    else:
        print("Conversão indisponível")

moedas()

"""8 - Calculadora de Média com Mensagem"""
def media():
    print("Média de Notas")
    soma = 0
    for i in range (3):
        nota = float (input(f"Digita a {i + 1}° nota: "))
        soma += nota
    media = soma / 3
    print("A média é: ", media)

    if media >= 7:
        print("Aprovado")

    elif media >= 5 and media <= 6.9:
        print("Cursando")

    elif media < 5:
        print("Reprovado")

media()

"""9 - Simulador de Caixa Eletrônico (versão básica)"""
def caixa_eletronico():
    print("- Bem vindo ao ATM -")
    print("Cédulas disponíveis para saque: R$100, R$50, R$20, R$10")
    valor = int(input("Digite um valor a ser sacado: "))

    cedula1 = 100
    cedula2 = 50
    cedula3 = 20
    cedula4 = 10

    if valor 


