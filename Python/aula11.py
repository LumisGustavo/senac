"""Conjuntos"""
def conjunto_frutas():
    frutas = {"maçã", "banana", "laranja", "uva"}
    print("Essas são as frutas do meu conjunto: ")
    for fruta in frutas:
        print(f"- {fruta}")

conjunto_frutas()

"""Ênfase em Índices"""
def lista_de_produtos():
    produtos = {
        "notebook": 3500.00,
        "chinela": 50.00,
        "maçã": 8.50
    }

    print("Meus produtos: ")
    for produto in produtos.keys():
        print(f"- {produto}")

lista_de_produtos()

"""Dicionários"""
def produtos_com_mais_coisas():
    produtos = {
        "Notebook": ("LG", 3500.00, "Cartão em até 12x com acréscimos"),
        "Monitor": ("Samsung", 1400.00, "Cartão em até 6x sem juros"),
        "Teclado": ("Logitech", 122.00, "A vista")
    }

    print("Produtos Cadastros: ")
    for produto, detalhes, in produtos.items():
        marca, preco, pagamento = detalhes
        print(f"Produto: {produto}")
        print(f" - Marca: {marca}")
        print(f" - Preço: {preco:.2f}")
        print(f" - Formas de Pagamento: {pagamento}\n")

produtos_com_mais_coisas()