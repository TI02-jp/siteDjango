import mysql.connector

banco = None

try:
    # criar conexao ao banco de dados
    banco = mysql.connector.connect(
        host='localhost',
        database='cadastro_empresas',
        user='root',
        passwd='ti02@2025'
    )

    cursor = banco.cursor()

    # Comando SQL para alterar a coluna DataAberturaEmpresa para NOT NULL
    alterar_coluna_SQL = """
    ALTER TABLE tbl_empresas
    MODIFY COLUMN DataAberturaEmpresa VARCHAR(10) NOT NULL;
    """
    cursor.execute(alterar_coluna_SQL)

    # Comando SQL para adicionar a PRIMARY KEY (se ainda não existir)
    adicionar_pk_SQL = """
    ALTER TABLE tbl_empresas
    ADD PRIMARY KEY (IdEmpresas);
    """
    try:
        cursor.execute(adicionar_pk_SQL)
        print("Primary Key adicionada com sucesso.")
    except mysql.connector.Error as erro:
        if erro.errno == 1068:  # Código de erro do MySQL para "Primary key already exists"
            print("Primary Key já existe.")
        else:
            print("Erro ao adicionar Primary Key: {}".format(erro))

    banco.commit()
    print("Alterações realizadas com sucesso.")

except mysql.connector.Error as erro:
    print("Falha na operação com o MySQL: {}".format(erro))
finally:
    if banco.is_connected():
        cursor.close()
        banco.close()
        print("Conexao ao MySQL finalizada")
