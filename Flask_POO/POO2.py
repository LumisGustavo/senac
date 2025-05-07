# Fundamentos exemplificados de controle em POO
class ContaBancaria:
    def __init__(self,  titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor): # Ilustração de como uma estrutura de controle funciona dentro de uma classe
        if valor <= self.saldo: 
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"{self.titular} possui R$ {self.saldo} na conta")

conta = ContaBancaria("Mattheus", 500)
conta.exibir_saldo()
conta.depositar(200)
conta.exibir_saldo()
conta.sacar(100)
conta.exibir_saldo()
conta.sacar(800) # Simulação de tentativa com saldo insuficiente

# Demonstração do que podemos fazer: Menu interativo

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
        
    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"{self.nome} - Notas: {self.notas} - Média: {media}")

def menu_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)

    while True:
        print("1 - Adicionar nota")
        print("2 - Ver informações do aluno")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nota = float(input("Digite a nota"))
            aluno.adicionar_nota(nota)
        elif opcao == "2":
            aluno.exibir_informacoes()
        elif opcao == "3":
            break
        else:
            print("Opção inválida")

menu_aluno()