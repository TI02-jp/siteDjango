from flask import render_template, redirect, url_for, flash
from app import app, db
from app.loginForms import LoginForm, RegistrationForm
from app.models.tables import User

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
        user = User(
            username=form.username.data,
            email=form.email.data,
            name=form.name.data
        )
        user.set_password(form.password.data)  # Agora usando hashing
        db.session.add(user)
        db.session.commit()
        flash('Parabéns, você agora é um usuário registrado!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/test')
def test():
    try:
        # Teste simples do banco de dados
        db.session.execute('SELECT 1')
        return "Teste bem-sucedido!"
    except Exception as e:
        return f"Erro no teste: {str(e)}", 500