from flask import render_template, redirect, url_for, flash, session
from flask_login import current_user, login_required, login_user, logout_user
from app import app, db
from app.loginForms import LoginForm, RegistrationForm
from app.models.tables import User
from sqlalchemy import text
from app.forms import EmpresaForm
from datetime import datetime
from app.models.tables import Empresa, RegimeLancamento

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)  # <- ESSENCIAL
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
        # Capturando os dados do formulário
        codigo_empresa = form.codigo_empresa.data
        nome_empresa = form.nome_empresa.data
        cnpj = form.cnpj.data
        data_abertura = form.data_abertura.data
        socio_administrador = form.socio_administrador.data
        tributacao = form.tributacao.data
        regime_lancamento = form.regime_lancamento.data
        atividade_principal = form.atividade_principal.data
        sistemas_consultorias = form.sistemas_consultorias.data
        sistema_atualizado = form.sistema_atualizado.data

        # Criando uma nova empresa
        nova_empresa = Empresa(
            CodigoEmpresa=codigo_empresa,
            NomeEmpresa=nome_empresa,
            CNPJ=cnpj,
            DataAbertura=data_abertura,
            SocioAdministrador=socio_administrador,
            Tributacao=tributacao,
            RegimeLancamento=regime_lancamento,
            AtividadePrincipal=atividade_principal,
            SistemasConsultorias=sistemas_consultorias,
            SistemaAtualizado=sistema_atualizado
        )
        # Inserindo no banco de dados
        db.session.add(nova_empresa)
        db.session.commit()
        
        print("Empresa salva com sucesso:", nova_empresa)
        return redirect(url_for('sucesso'))  # Redireciona para a página de sucesso

    return render_template('empresas/cadastrar.html', form=form)

@app.route('/listar_empresas')
@login_required
def visualizar_empresas():
    empresas = Empresa.query.all()  # Buscar todas as empresas cadastradas
    print("Empresas encontradas:", empresas)
    return render_template('empresas/listar.html', empresas=empresas)

@app.route('/relatorios')
@login_required
def relatorios():
    # Implemente a lógica para gerar relatórios ou exibir dados específicos
    return render_template('relatorios.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login'))