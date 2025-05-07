"""

1. (Conceitual)
O que é um atributo em uma classe Python?
A) Uma função especial
B) Uma variável que pertence a um objeto
C) Uma estrutura de repetição interna
D) Um parâmetro usado fora do __init__

R = B
________________________________________
2. (Conceitual)
Qual a diferença entre método e função comum em Python?
A) Não há diferença
B) Método sempre retorna True
C) Método é uma função definida dentro de uma classe e acessa atributos via self
D) Função tem self, método não

R = C
________________________________________
3. (Código - Interpretação)
O que esse código imprime?
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print(f"Olá, {self.nome}!")

p = Pessoa("Lucas")
p.saudacao()

R = Olá, Lucas!
________________________________________
4. (Prática)
O que acontece se você tentar acessar um atributo que não existe em um objeto?
A) O Python ignora e segue o código
B) Ele cria o atributo automaticamente
C) Ocorre um erro: AttributeError
D) O atributo é definido como None

R = C
________________________________________
5. (Código - Completar)
Complete o método abaixo para que ele imprima a idade do aluno:
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_idade(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Gustavo", 19)
p1.apresentar()
________________________________________
6. (Código - Análise de erro)
Qual o erro no código abaixo?
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar():
        print(f"{self.nome} custa R${self.preco}")
A) Faltou ponto e vírgula
B) O método mostrar() não recebe self
C) Atributos estão errados
D) print deveria estar fora da classe

R = B
________________________________________
7. (Criação de método personalizado)
Crie um método chamado desconto() dentro de uma classe Produto que reduza o preço em 10%.

R = class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem/100)
        self.preco -= desconto

    def mostrar_produto(self):
        print(f"{self.nome} custa R${self.preco:.2f}")

produto = Produto("Feijão", 8)
produto.mostrar_produto()
produto.aplicar_desconto(10)
produto.mostrar_produto()
________________________________________
8. (Conceitual)
O que o método especial __init__ faz?
A) Remove atributos do objeto
B) É o construtor da classe, chamado na criação do objeto
C) Serve apenas para criar métodos
D) Executa o método principal do Python

R = B
________________________________________
9. (Código com método que retorna valor)
Qual a saída do código?
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

c = Circulo(2)
print(c.area())

R = 12,56
________________________________________
10. (Reflexiva/aberta)
Explique com suas palavras a diferença entre um atributo e um método.
Dê um exemplo de cada dentro de uma mesma classe.

R = Atributo é a denominação de uma variável dentro de um objeto, enquanto um método denomina-se como uma função dentro deste objeto e como ela deve ser realziada
Ex: class Pessoa: # Objeto 'Pessoa'
    def __init__(self, nome, idade): # Atributos 'nome' e 'idade'
        self.nome = nome
        self.idade = idade

    def apresentar(self): # Método, função atribuida ao objeto que pode ser chamada pelo 'self'
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Gustavo", 19) # Atribuição de informações (Gustavo, 19) ao objeto
p1.apresentar() # Fechamento do método

"""