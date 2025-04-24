from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import mysql

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    usuarios = cur.fetchall()
    return render_template('index.html', usuarios=usuarios)

@main.route('/add', methods=['POST'])
def add_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    mysql.connection.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>')
def edit_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE id = %s", (id,))
    usuario = cur.fetchone()
    return render_template('edit.html', usuario=usuario)

@main.route('/update/<int:id>', methods=['POST'])
def update_usuario(id):
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id = %s", (nome, email, senha, id))
    mysql.connection.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuario WHERE id = %s", (id,))
    mysql.connection.commit()
    return redirect(url_for('main.index'))