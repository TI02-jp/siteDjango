from flask import render_template, redirect, url_for, flash
from app import app, db
from app.loginForms import LoginForm, RegistrationForm
from app.models.tables import User
from sqlalchemy import text  # Certifique-se de importar o 'text'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de autenticação do usuário
        user = User.query.filter_by(username=form.username.data).first()  # Busca o usuário pelo nome de usuário
        if user and user.check_password(form.password.data):  # Verifica se a senha está correta
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home'))  # Redireciona para a página inicial
        else:
            flash('Credenciais inválidas', 'danger')  # Se não encontrar ou senha errada
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Verifica se já existe um usuário com mesmo username ou email
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()
        if existing_user:
            flash('Usuário ou email já cadastrado.', 'warning')
            return redirect(url_for('register'))

        # Cria novo usuário
        user = User(
            username=form.username.data,
            email=form.email.data,
            name=form.name.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Parabéns, você agora é um usuário registrado!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/test_connection')
def test_connection():
    try:
        # Usando 'text()' para a consulta SQL
        result = db.session.execute(text('SELECT 1'))
        return "Conexão bem-sucedida com o banco de dados!"
    except Exception as e:
        return f"Erro na conexão: {str(e)}", 500
    
@app.route('/users')
def list_users():
    users = User.query.all()  # Busca todos os usuários
    return render_template('list_users.html', users=users)

