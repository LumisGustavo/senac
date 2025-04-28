"""1 - Cadastro de alunos"""
def cadastrar_produtos():
    alunos = []
    while True:
        aluno = input("Digite o nome do aluno ou digite 'sair' para encerrar: ")
        if aluno.lower() == "sair":
            break
        alunos.append(aluno)
    print("Alunos cadastrados: ")
    print(alunos)

cadastrar_produtos()

"""2 - Soma de números pares"""
def soma_numeros_pares():
    numeros = []
    pares = []
    while True:
        for i in range(6):
            numero = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)

        for par in numeros:
           if (par % 2) == 0:
              pares.append(par)

        soma_pares = sum(pares)
        soma_numeros = sum(numeros)
        print("Soma dos números: ",soma_numeros)
        print("Soma somente dos números pares: ",soma_pares)
        break

soma_numeros_pares()

"""3 - Procurar um nome na lista"""
def procurar_nomes():
    nomes = {"leah", "sebastian", "robin", "pierre", "abigail"}
    while True:
        nome = input("Digite o nome que deseja procura na lista, ou digite 'sair' para encerrar: ")

        if nome.lower() == "sair":
            break

        elif nome.lower() in nomes:
            print("O nome está presente na lista!")

        else:
            print("O nome não está na lista")

procurar_nomes()

"""4 - Média de notas de uma turma"""