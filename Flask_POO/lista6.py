"""1. (Conceitual)
O que é uma classe em Python?
A) Um tipo especial de lista
B) Um bloco de código com variáveis globais
C) Um molde para criar objetos com características e comportamentos
D) Um tipo de função com múltiplos parâmetros

R = C

________________________________________
2. (Conceitual)
O que são objetos em Programação Orientada a Objetos?
A) Variáveis com nomes maiores
B) Instâncias criadas a partir de uma classe
C) Funções que não recebem parâmetros
D) Qualquer estrutura de repetição

R = B

________________________________________
3. (Prática)
Dada a classe abaixo:
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
Qual das opções cria corretamente um objeto dessa classe?
A) Pessoa = ("João")
B) pessoa = Pessoa.nome("João")
C) pessoa = Pessoa("João")
D) pessoa = Pessoa["João"]

R = C

________________________________________
4. (Prática)
Em uma classe, o que representa o self?
A) A classe como um todo
B) Um valor fixo definido no construtor
C) A própria instância (objeto) sendo criada ou manipulada
D) Um comando para sair do método

R = C
________________________________________
5. (Código - Preenchimento)
Complete o código abaixo para que ele funcione corretamente:
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

meu_carro = 
print(meu_carro.modelo)
________________________________________
6. (Conceitual)
Assinale a alternativa que melhor representa a diferença entre classe e objeto:
A) Objeto é a teoria, classe é a prática
B) Classe é a definição, objeto é a instância dessa definição
C) Ambos são exatamente a mesma coisa
D) Classe serve só para criar funções e não tem atributos

R = B
________________________________________
7. (Código - Compreensão)
O que será impresso ao executar o seguinte código?
class Animal:
    def __init__(self, nome):
        self.nome = nome

a = Animal("Cachorro")
print(a.nome)

R = 
________________________________________
8. (Prática)
Qual é a palavra-chave utilizada para definir uma classe em Python?
A) new
B) function
C) class
D) define
________________________________________
9. (Reflexão/Criação)
Explique com suas palavras o que significa instanciar uma classe.
Dê um exemplo prático com o nome de uma classe fictícia.________________________________________
10. (Análise de código com erro proposital)
Veja o código abaixo. Qual é o erro presente nele?
class Aluno:
    def __init__(nome, idade):
        nome = nome
        idade = idade
A) Está tudo certo
B) A classe deveria chamar ClasseAluno
C) Faltou o self nos parâmetros e nos atributos
D) O nome idade deveria ser string"""