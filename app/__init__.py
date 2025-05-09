import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configurações do app
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Inicializações
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Rota onde o usuário será redirecionado se não estiver logado

# Importa o modelo User para o user_loader
from app.models.tables import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # busca o usuário pelo ID

@app.context_processor
def inject_now():
    from datetime import datetime
    return {'now': datetime.now}

# Importa os controladores (depois de tudo configurado)
from app.forms import *
from app.controllers import routes
