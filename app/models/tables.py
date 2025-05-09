from app import db
from enum import Enum
from datetime import date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.set_password(password)
        self.name = name
        self.email = email

        
    def __repr__(self):
        return "<User %r>" % self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __init__(self, content, id_user):
        self.content = content
        self.id_user = id_user

    def __repr__(self):
        return "<Post %r>" % self.id
    
class RegimeLancamento(Enum):
    CAIXA = 'Caixa'
    COMPETENCIA = 'Competência'

class Empresa(db.Model):
    __tablename__ = 'tbl_empresas'  # Especificando o nome da tabela como tbl_empresas

    id = db.Column(db.Integer, primary_key=True)
    CodigoEmpresa = db.Column(db.String(100), nullable=False)
    NomeEmpresa = db.Column(db.String(200), nullable=False)
    CNPJ = db.Column(db.String(14), nullable=False, unique=True)
    DataAbertura = db.Column(db.Date, nullable=False)  # Tipo Date para armazenar data
    SocioAdministrador = db.Column(db.String(200), nullable=False)
    Tributacao = db.Column(db.String(100), nullable=False)
    RegimeLancamento = db.Column(db.String(20), nullable=False)
    AtividadePrincipal = db.Column(db.String(200), nullable=False)
    SistemasConsultorias = db.Column(db.String(200), nullable=False)
    SistemaAtualizado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Empresa {self.NomeEmpresa}>"
