from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class EmpresaForm(FlaskForm):
    id_empresa = StringField('ID da Empresa', validators=[DataRequired()])
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    data_abertura = StringField('Data de Abertura', validators=[DataRequired()])
    socio_administrador = StringField('Sócio Administrador')
    tributacao = StringField('Tributação da Empresa')
    regime_lancamento = SelectField('Regime de Lançamento', 
                                    choices=[('CAIXA', 'Caixa'), 
                                             ('COMPETENCIA', 'Competência')], 
                                    validators=[DataRequired()])
    atividade_principal = StringField('Atividade Principal')
    sistemas_consultorias = SelectMultipleField('Sistemas/Consultorias', 
                                             choices=[
                                                 ('IOB', 'IOB'),
                                                 ('ACESSORIAS', 'Acessórias'),
                                                 ('ACESSO_SAT', 'Acesso ao SAT'),
                                                 ('ITC', 'ITC'),
                                                 ('QUESTOR', 'Questor'),
                                                 ('ECONET', 'Econet'),
                                                 ('SIEG', 'Sieg'),
                                                 ('QUESTOR_NET', 'Questor Net'),
                                                 ('SIEG_TAGS', 'Sieg utiliza TAGs')
                                             ])
    sistema_atualizado = BooleanField('Sistema Atualizado na Empresa')
    submit = SubmitField('Cadastrar Empresa')