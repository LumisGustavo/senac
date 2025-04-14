"""Exercício com while e break"""
def solicitar_idade():
    while True: # Início do loop condicional - "Enquanto for verdade"
        idade = int(input("Digite sua idade: "))

        if idade >= 0 and idade <= 120:
            print("Idade registrada: ", idade)
            break # Condição de parada
        else:
            print("Idade Inválida. Tente Novamente")

solicitar_idade()