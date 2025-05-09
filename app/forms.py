from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, SelectMultipleField, DateField
from wtforms.validators import DataRequired

class EmpresaForm(FlaskForm):
    codigo_empresa = StringField('Código da Empresa', validators=[DataRequired()])
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    data_abertura = DateField('Data de Abertura', format='%Y-%m-%d', validators=[DataRequired()])
    socio_administrador = StringField('Sócio Administrador')
    tributacao = StringField('Tributação da Empresa')
    regime_lancamento = SelectField('Regime de Lançamento', 
                                    choices=[('CAIXA', 'Caixa'), 
                                             ('COMPETENCIA', 'Competência')], 
                                    validators=[DataRequired()])
    atividade_principal = StringField('Atividade Principal')
    sistemas_consultorias = SelectMultipleField('Sistemas/Consultorias', 
                                               choices=[('IOB', 'IOB'),
                                                        ('ACESSORIAS', 'Acessórias'),
                                                        ('ACESSO_SAT', 'Acesso ao SAT'),
                                                        ('ITC', 'ITC'),
                                                        ('QUESTOR', 'Questor'),
                                                        ('ECONET', 'Econet'),
                                                        ('SIEG', 'Sieg'),
                                                        ('QUESTOR_NET', 'Questor Net'),
                                                        ('SIEG_TAGS', 'Sieg utiliza TAGs')])
    sistema_atualizado = BooleanField('Sistema Atualizado na Empresa')
    submit = SubmitField('Cadastrar Empresa')