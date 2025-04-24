"""Listas"""
def mostrar_nomes():
    nomes = ["Elis", "Clara", "Isabella", "Danilo", "Thiago", "João Verde", "Gustavo"]
    print("Lista de nomes: ")
    for nome in nomes:
        print(nome)

mostrar_nomes()

def media_notas():
    notas = [5.9, 8.5, 9.9, 9.7]
    media = sum(notas) / len(notas)
    print(f"As notas existentes são: {notas}")
    print(f"A média final é: {media: .2f}")
    print(f"A quantidade de itens na lista é: {len(notas)}")

media_notas()

def cadastrar_produtos():
    produtos = []
    while True:
        produto = input("Digite o nome do produto ou digite 'sair' para encerrar: ")
        if produto.lower() == "sair":
            break
        produtos.append(produto) #".append" é usado para acrescentar itens em uma lista na última posição

    print("Produtos cadastrados: ")
    print(produtos)

cadastrar_produtos()