"""4 - Classificador de Números"""
def classificar_numeros():
    positivos = 0
    negativos = 0
    zeros = 0

    for i in range (6):
        numero = float(input("Digite o número: "))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1

    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Zeros: {zeros}")

classificar_numeros()

"""5 - Verificador de Nome com Letra Inicial"""
def verificador_letra():
    for i in range (5):
        nome = input("Digite o nome: ")
        if nome.lower().startswith("a"):
            print(f"O nome {nome} começa com a letra A")
        else:
            print(f"O nome {nome} não começa com a letra A")

verificador_letra()

"""8 - Senha Repetitiva"""
def senha_loop():
    while True:
        senha = input("Digite a senha: ")
        if senha == "senac123":
            print("Acesso liberado")
            break
        else:
            print("Senha incorreta. Tente novamente: ")

senha_loop()

"""10 - Desafio da Tabuada Completa"""
def tabuada_completa():
    while True:
        numero = int(input("Digite um número para consultar a tabuada: "))
        print(f"Segue a tabuada do número {numero}")

        for i in range(1,11):
            print(f"{numero} x {i} = {numero * i}")

        repetir = input("Deseja realizar outra operação? (s/n)")
        if repetir.lower() != "s":
            print("Operação finalizada")
            break