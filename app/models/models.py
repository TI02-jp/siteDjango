from app import db
from sqlalchemy.types import TypeDecorator, String
import json

class JsonString(TypeDecorator):
    impl = String

    def __init__(self, length=255, **kwargs):
        super().__init__(length=length, **kwargs)

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)
        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value)
        return None

class Empresa(db.Model):
    __tablename__ = 'tbl_empresas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NomeEmpresa = db.Column(db.String(100), nullable=False)
    CNPJ = db.Column(db.String(18), unique=True, nullable=False)
    AtividadePrincipal = db.Column(db.String(100))
    DataAbertura = db.Column(db.String(10), nullable=False)
    SocioAdministrador = db.Column(db.String(100))
    Tributacao = db.Column(db.String(50))
    RegimeLancamento = db.Column(db.Enum('CAIXA', 'COMPETENCIA'))
    SistemasConsultorias = db.Column(JsonString(500))
    SistemaUtilizado = db.Column(db.String(150))
    CodigoEmpresa = db.Column(db.String(100), nullable=False)

    