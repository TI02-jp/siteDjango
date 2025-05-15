from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, BooleanField, SubmitField, SelectMultipleField, DateField
from wtforms.validators import DataRequired

class EmpresaForm(FlaskForm):
    codigo_empresa = StringField('Código da Empresa', validators=[DataRequired()])
    nome_empresa = StringField('Nome da Empresa', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    data_abertura = DateField('Data de Abertura', format='%d-%m-%Y', validators=[DataRequired()])
    socio_administrador = StringField('Sócio Administrador', validators=[DataRequired()])
    
    tributacao = RadioField('Tributação', choices=[('Simples Nacional', 'Simples Nacional'), 
                                                ('Lucro Presumido', 'Lucro Presumido'), 
                                                ('Lucro Real', 'Lucro Real')], 
                            validators=[DataRequired()])
    
    regime_lancamento = RadioField('Regime de Lançamento', choices=[('CAIXA', 'Caixa'), 
                                                                ('COMPETENCIA', 'Competência')], 
                                validators=[DataRequired()])
    
    atividade_principal = StringField('Atividade Principal', validators=[DataRequired()])
    
    sistemas_consultorias = RadioField('Sistemas e Consultorias', 
                                            choices=[('', 'Nenhum'),
                                                        ('IOB', 'IOB'), 
                                                        ('ACESSÓRIAS', 'ACESSÓRIAS'),
                                                        ('ACESSO AO SAT', 'ACESSO AO SAT'), 
                                                        ('ITC', 'ITC'), 
                                                        ('QUESTOR', 'QUESTOR'),
                                                        ('ECONET', 'ECONET'), 
                                                        ('QUESTOR NET', 'QUESTOR NET'), 
                                                        ('SIEG', 'SIEG'),
                                                        ('SIEG - Utiliza TAGs', 'SIEG - Utiliza TAGs')],
                                                    default='',
                                                    validators=[DataRequired()])
    
    sistema_atualizado = BooleanField('Sistema Atualizado')
    submit = SubmitField('Cadastrar Empresa')
