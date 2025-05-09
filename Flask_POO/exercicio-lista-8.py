"""1 – Cadastro de Livros"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "livros.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LivroDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL
            )
    ''')
        
    def inserir_livro(self, titulo, autor):
        self.cursor.execute('''
            INSERT INTO livros (titulo, autor) VALUES (?, ?)
    ''', (titulo, autor))
        self.conexao.commit()
        print(f"Livro {titulo} inserido com sucesso!")

    def listar_livros(self):
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()
        print("Lista de livros: ")
        for livro in livros:
            print(f"ID: {livro[0]} - Título: {livro[1]} - Autor: {livro[2]}")

def menu():
    dao = LivroDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir livro")
        print("2 - Listar livros")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            dao.inserir_livro(titulo, autor)
        elif opcao == "2":
            dao.listar_livros()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""2 – Cadastro de Cursos com Nível"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "cursos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class CursosDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nivel TEXT NOT NULL
            )
    ''')
        
    def inserir_curso(self, nome, nivel):
        self.cursor.execute('''
            INSERT INTO cursos (nome, nivel) VALUES (?, ?)
    ''', (nome, nivel))
        self.conexao.commit()
        print(f"Curso {nome} inserido com sucesso!")

    def listar_cursos(self):
        self.cursor.execute('SELECT * FROM cursos')
        cursos = self.cursor.fetchall()
        print("Lista de livros: ")
        for curso in cursos:
            print(f"ID: {curso[0]} - Nome: {curso[1]} - Nível: {curso[2]}")

def menu():
    dao = CursosDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir curso")
        print("2 - Listar cursos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do curso: ")
            nivel = input("Digite o nivel do curso: ")
            dao.inserir_curso(nome, nivel)
        elif opcao == "2":
            dao.listar_cursos()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""3 – Inserção de Professores"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "professores.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class ProfessorDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            disciplina TEXT NOT NULL
            )
    ''')
        
    def inserir_professor(self, nome, disciplina):
        self.cursor.execute('''
            INSERT INTO professores (nome, disciplina) VALUES (?, ?)
    ''', (nome, disciplina))
        self.conexao.commit()
        print(f"Professor {nome} inserido na lista com sucesso!")

    def listar_professores(self):
        self.cursor.execute('SELECT * FROM professores')
        professores = self.cursor.fetchall()
        print("Lista de professores: ")
        for professor in professores:
            print(f"ID: {professor[0]} - Nome: {professor[1]} - Disciplína: {professor[2]}")

def menu():
    dao = ProfessorDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir nome de professor(a)")
        print("2 - Listar professores")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do professor(a): ")
            disciplina = input("Digite a disciplina do(a) professor(a): ")
            dao.inserir_professor(nome, disciplina)
        elif opcao == "2":
            dao.listar_professores()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""4 – Cadastro de Clientes"""
"""
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "clientes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class ClienteDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL
            )
    ''')
        
    def inserir_cliente(self, nome, email):
        self.cursor.execute('''
            INSERT INTO clientes (nome, email) VALUES (?, ?)
    ''', (nome, email))
        self.conexao.commit()
        print(f"Cliente {nome} inserido na lista com sucesso!")

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')
        clientes = self.cursor.fetchall()
        print("Lista de clientes: ")
        for cliente in clientes:
            print(f"ID: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]}")

def menu():
    dao = ClienteDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir nome de cliente")
        print("2 - Listar clientes")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            dao.inserir_cliente(nome, email)
        elif opcao == "2":
            dao.listar_clientes()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
"""

"""5 - Análise de Código (Criação de Tabela)"""
"""
Descrição:
Analise o trecho de código abaixo:
class AnimalDAO:
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE animais (
                nome TEXT,
                especie TEXT
            )
        ''')
Pergunta:
Quais dois erros ou problemas você consegue identificar nesse código?
(Dica: pense na estrutura da tabela e na classe)

R = Não possuir uma especificação de criação de tabela caso 'animais' não exista e não especificar que o texto pode ser nulo
"""

"""6 – Identifique o erro"""
"""
Descrição:
Veja o código abaixo e diga por que ele falha:
self.cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", "Carlos", 18)
Pergunta:
O que precisa ser corrigido nessa linha para que o comando funcione corretamente?

R = A especificação em forma de () de "Carlos", 18, representando, respectivamente, 'nome' e 'idade'
Correção = self.cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", ("Carlos", 18))
"""
