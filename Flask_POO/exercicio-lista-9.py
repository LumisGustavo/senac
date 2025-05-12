"""1 - [Sistema da Cantina Escolar – Cadastro de Lanches]"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "lanches.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LancheDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lanches(
                            lanche TEXT NOT NULL,
                            preço TEXT NOT NULL
            )
    ''')
        
    def inserir_lanche(self, lanche, preço):
        self.cursor.execute('''
            INSERT INTO lanches (lanche, preço) VALUES (?, ?)
    ''', (lanche, preço))
        self.conexao.commit()
        print(f"Lanche {lanche} registrado com sucesso!")

    def listar_lanches(self):
        self.cursor.execute('SELECT * FROM lanches')
        lanches = self.cursor.fetchall()
        print("Lista de lanches: ")
        for lanche in lanches:
            print(f"Lanche: {lanche[0]} - Preço: {lanche[1]}")

def menu():
    dao = LancheDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir lanche")
        print("2 - Listar lanches")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lanche = input("Digite o nome do lanche: ")
            preço = input("Digite o preço do lanche: ")
            dao.inserir_lanche(lanche, preço)
        elif opcao == "2":
            dao.listar_lanches()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""2 - [Estação Gamer – Atualizando o Preço do PC]"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "produtos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class ProdutoDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
                            nome TEXT NOT NULL,
                            preco TEXT NOT NULL
            )
    ''')
        
    def inserir_produto(self, nome, preco):
        self.cursor.execute('''
            INSERT INTO produtos (nome, preco) VALUES (?, ?)
    ''', (nome, preco))
        self.conexao.commit()
        print(f"Produto {nome} registrado com sucesso!")

    def listar_produtos(self):
        self.cursor.execute('SELECT * FROM produtos')
        produtos = self.cursor.fetchall()
        print("Lista de produtos: ")
        for produto in produtos:
            print(f"Produto: {produto[0]} - Preço: {produto[1]}")

    def atualizar_preco(self, nome, novo_preco):
        self.cursor.execute('UPDATE produtos SET preco = ? WHERE nome = ?', (novo_preco, nome))
        self.conexao.commit()
        print(f"Preço de {nome} foi atualizado para {novo_preco}")

def menu():
    dao = ProdutoDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço do produto: ")
            dao.inserir_produto(nome, preco)
        elif opcao == "2":
            dao.listar_produtos()
        elif opcao == "3":
            nome = input("Digite o nome do produto que deseja alterar o preço: ")
            novo_preco = input("Digite o novo preço do produto: ")
            dao.atualizar_preco(nome, novo_preco)
        elif opcao == "4":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""3 - [Controle de Visitantes – Removendo os que já saíram]"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "visitantes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class VisitanteDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitantes(
                            visitante TEXT NOT NULL,
                            motivo TEXT NOT NULL
            )
    ''')
        
    def inserir_visitante(self, visitante, motivo):
        self.cursor.execute('''
            INSERT INTO visitantes (visitante, motivo) VALUES (?, ?)
    ''', (visitante, motivo))
        self.conexao.commit()
        print(f"Visitante {visitante} registrado com sucesso!")

    def listar_visitantes(self):
        self.cursor.execute('SELECT * FROM visitantes')
        visitantes = self.cursor.fetchall()
        print("Lista de visitantes: ")
        for visitante in visitantes:
            print(f"Visitante: {visitante[0]} - Motivo da visita: {visitante[1]}")

    def deletar_visitante(self, visitante):
        self.cursor.execute('DELETE FROM visitantes WHERE visitante = ?', (visitante, ))
        self.conexao.commit()
        print(f"Visitante {visitante} foi removido com sucesso.")

def menu():
    dao = VisitanteDAO()
    dao.criar_tabela()

    while True:
        print("1 - Registrar visitante")
        print("2 - Listar visitantes")
        print("3 - Deletar registro de visitante")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visitante = input("Digite o nome do visitante: ")
            motivo = input("Digite o motivo da visita: ")
            dao.inserir_visitante(visitante, motivo)
        elif opcao == "2":
            dao.listar_visitantes()
        elif opcao == "3":
            visitante = input("Digite o nome do visitante para ser excluido dos registros: ")
            dao.deletar_visitante(visitante)
        elif opcao == "4":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""4 - [Clube de Leitura – Buscar Livro pelo Título]"""
"""

"""
