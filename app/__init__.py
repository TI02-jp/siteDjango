from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

# Configuração da URI para o banco MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:ti02@2025@localhost/cadastro_empresas')

# Outras configurações
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sua-chave-secreta-aqui')

# Proteção CSRF
csrf = CSRFProtect(app)

# Conexão com o banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
