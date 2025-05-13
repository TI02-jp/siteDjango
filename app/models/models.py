import json
from app import db
from sqlalchemy.types import TypeDecorator, String

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

    IdEmpresas = db.Column(db.String(50), primary_key=True)
    CodigoEmpresa = db.Column(db.String(100), nullable=False)
    NomeEmpresa = db.Column(db.String(200), nullable=False)
    CNPJ = db.Column(db.String(14), nullable=False, unique=True)
    DataAbertura = db.Column(db.Date, nullable=False)
    SocioAdministrador = db.Column(db.String(200), nullable=False)
    Tributacao = db.Column(db.String(100), nullable=False)
    RegimeLancamento = db.Column(db.String(20), nullable=False)
    AtividadePrincipal = db.Column(db.String(200), nullable=False)
    SistemasConsultorias = db.Column(JsonString(500))
    SistemaAtualizado = db.Column(db.Boolean, default=False)
