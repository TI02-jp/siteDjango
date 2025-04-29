from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Tamanho ajustado para o MySQL
    password = db.Column(db.String(120), nullable=False)  # Tamanho ajustado para o MySQL
    name = db.Column(db.String(100), nullable=False)  # Tamanho ajustado para o MySQL
    email = db.Column(db.String(120), unique=True, nullable=False)  # Tamanho ajustado para o MySQL

    def __init__(self, username, password, name, email):
        self.username = username
        self.set_password(password)  # Já criptografa aqui
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
