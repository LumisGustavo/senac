"""1 - Votação de Candidato"""
def votacao():
    ana = 0
    bruno = 0
    carla = 0

    print("Vote em um dos candidatos:")
    print("1 - Ana")
    print("2 - Bruno")
    print("3 - Carla")
    print("4 - Encerrar votação")

    for i in range(5):
        voto = int(input(f"{i+1}º Voto: "))
        if voto == 1:
            ana += 1
        elif voto == 2:
            bruno += 1
        elif voto == 3:
            carla += 1
        elif voto == 4:
            print("Votação encerrada")
            break
        else:
            print("Voto inválido e contabilizado como nulo")

    print("Resultado da votação:")
    print("Ana:", ana, "voto(s)")
    print("Bruno:", bruno, "voto(s)")
    print("Carla:", carla, "voto(s)")

votacao()

"""2 - Sistema de Avaliação"""
def media_aluno():
    print("Boletim Escolar")
    
    while True:
        aluno = []

        for i in range(5):
            nota = float(input(f"Digite sua {i + 1}ª nota: "))
            aluno.append(nota)

        media = sum(aluno) / 5

        if media >= 7:
            print(f"Sua média foi {media:.2f}, você foi aprovado")
        elif 5 <= media < 7:
            print(f"Sua média foi {media:.2f}, você está em recuperação")
        else:
            print(f"Sua média foi {media:.2f}, você foi reprovado")

        repetir = input("Deseja calcular a média de outro aluno? (s/n): ").lower()
        if repetir != 's':
            print("Encerrando o programa.")
            break

media_aluno()

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
