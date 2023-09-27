import psycopg2
from psycopg2.extras import execute_values
from psycopg2 import sql

db_name = 'ETL'
db_host = 'localhost'
db_port = '5432'
db_user = 'postgres'
db_passw = '572711'

try:
    conct = psycopg2.connect(
        dbname=db_name,
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_passw
    )

except psycopg2.Error as e:
    print(f"\n\tErro! Não foi possívelconectar ao {db_name}: {e}")
    exit()

cur = conct.cursor()
# --------------------------------
csv_file = 'Dados/Clientes.csv'
# --------------------------------
table_name = "clientes"
# --------------------------------

insert_query = sql.SQL(""" 
INSERT INTO{}(Codigo_Cliente, Nome_Cliente, Sobrenome, Sexo, Qtdd_Filhos) VALUES %s;
""").format(sql.Identifier(table_name))

try:
    with open(csv_file, 'r') as f:
        next(f)  # basicamente pula/ignora o cabecalho
        data = [line.strip().split(';') for line in f]
        # pode aumentar dependendo do tamanho da base
        execute_values(cur, insert_query, data, page_size=500)
    conct.commit()
    print(f"\n\tSucesso! Todos os dados de {table_name} foram inseridos.")
except Exception as e:
    conct.rollback()
    print(f"\n\tErro! Não foi possivel inserir os dados: {e}.")

finally:
    cur.close()
    conct.close()
