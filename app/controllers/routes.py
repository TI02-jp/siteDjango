from flask import render_template, redirect, url_for, flash, session
from flask_login import current_user, login_required, login_user, logout_user
from app import app, db
from app.loginForms import LoginForm, RegistrationForm
from app.models.tables import User
from sqlalchemy import text
from app.forms import EmpresaForm
from datetime import datetime
from app.models.tables import Empresa, RegimeLancamento
import uuid

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas', 'danger')
    return render_template('login.html', form=form)

# Rota do Dashboard (após o login)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

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
            name=form.name.data,
            password=form.password.data
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
        
        result = db.session.execute(text('SELECT 1'))
        return "Conexão bem-sucedida com o banco de dados!"
    except Exception as e:
        return f"Erro na conexão: {str(e)}", 500
    
@app.route('/users')
def list_users():
    users = User.query.all()
    print(users)
    return render_template('list_users.html', users=users)

@app.route('/cadastrar_empresa', methods=['GET', 'POST'])
def cadastrar_empresa():
    form = EmpresaForm()
    if form.validate_on_submit():
        try:
            nova_empresa = Empresa(
                CodigoEmpresa=form.codigo_empresa.data,
                NomeEmpresa=form.nome_empresa.data,
                CNPJ=form.cnpj.data,
                DataAbertura=form.data_abertura.data,
                SocioAdministrador=form.socio_administrador.data,
                Tributacao=form.tributacao.data,
                RegimeLancamento=form.regime_lancamento.data,
                AtividadePrincipal=form.atividade_principal.data,
                SistemasConsultorias=form.sistemas_consultorias.data,
                SistemaAtualizado=form.sistema_atualizado.data
            )

            db.session.add(nova_empresa)
            db.session.commit()
            flash('Empresa cadastrada com sucesso!', 'success')
            return redirect(url_for('listar_empresas'))

        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar empresa: {e}', 'danger')

    return render_template('empresas/cadastrar.html', form=form)

@app.route('/listar_empresas')
@login_required
def visualizar_empresas():
    empresas = Empresa.query.all()  # Buscar todas as empresas cadastradas

    # Garante que DataAbertura seja datetime (para evitar erro no template)
    for empresa in empresas:
        if empresa.DataAbertura and isinstance(empresa.DataAbertura, str):
            try:
                empresa.DataAbertura = datetime.strptime(empresa.DataAbertura, '%Y-%m-%d')
            except ValueError:
                empresa.DataAbertura = None

    print("Empresas encontradas:", empresas)
    return render_template('empresas/listar.html', empresas=empresas)

@app.route('/relatorios')
@login_required
def relatorios():
    # Implementa a lógica para gerar relatórios ou exibir dados específicos
    return render_template('relatorios.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login'))