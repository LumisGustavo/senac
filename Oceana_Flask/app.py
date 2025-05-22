import os
import re
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_gustavo'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

DATABASE = 'users.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def inicializar_banco():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   cpf TEXT UNIQUE NOT NULL,
                   senha TEXT NOT NULL
            );
        ''')
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']

        if len(cpf) < 11:
            return "CPF Inválido. Requisitos: 11 caracteres"
        
        if len(senha) < 8:
            return "Senha fraca. Requisitos: 8+ caracteres, 1 maiuscula, 1 número e 1 símbolo."
        
        db = get_db()
        try:
            db.execute('INSERT INTO usuarios (nome, cpf, email, senha) VALUES (?, ?, ?, ?)', (nome, cpf, email, senha))
            db.commit()
            return redirect(url_for('index_perfil'))
        except sqlite3.IntegrityError:
            return "Erro: CPF ou email já cadastrados."
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        usuario = db.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha)).fetchone()
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']
            return redirect(url_for('index_perfil'))
        else:
            return "Login inválido."
    return render_template('login.html')

@app.route('/index_perfil')
def index_perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('index_perfil.html', nome=session['usuario_nome'])

@app.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    usuario = db.execute('SELECT * FROM usuarios WHERE id=?', (session['usuario_id'],)).fetchone()
    
    return render_template('perfil.html', usuario=usuario)

@app.route('/excluir_conta', methods=['POST'])
def excluir_conta():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    db.execute('DELETE FROM usuarios WHERE id=?', (session['usuario_id'],))
    db.commit()
    
    session.clear()
    return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    inicializar_banco()
    app.run(debug=True)
