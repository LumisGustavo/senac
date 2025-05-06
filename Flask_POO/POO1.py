"""Classe - Programação Orientada a objetos"""

class Pessoa: #Em termos hierárquicos, a classe sempre virá primeiro
    def __init__(self, nome, idade):
        self.nome = nome # Criação de variável self.nome e atribuição ao nome
        self.idade = idade # Criação de variável self.idade e atribuição a idade

    def apresentar(self): # Todas as funções recebem o 'self'
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Isadora", 19) # Criando um objeto Pessoa e atribuindo uma variável
p2 = Pessoa("Isabela", 19)
p1.apresentar() # Utilizando o objeto criado para utilizar uma função da classe
p2.apresentar()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem/100)
        self.preco -= desconto

    def mostrar_produto(self):
        print(f"{self.nome} custa R${self.preco:.2f}")

produto = Produto("Monitor", 1200)
produto.mostrar_produto()
produto.aplicar_desconto(10)
produto.mostrar_produto()