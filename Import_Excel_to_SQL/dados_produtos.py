import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values

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
    print(f'Erro! Não foi possivel conectar ao {db_name}: {e}')
    exit()

cur = conct.cursor()
# --------------------------------
csv_file = 'Dados/Produtos.csv'
# --------------------------------
table_name = 'produtos'
# --------------------------------

insert_query = sql.SQL(""" 
                       INSERT INTO {}(SKU, Produto, Marca, Tipo_do_Produto, Preco_Unitario, Custo_Unitario) VALUES %s;
                       """).format(sql.Identifier(table_name))
try:
    with open(csv_file, 'r') as f:
        next(f)  # Nao esquecer de atribuir para ignorar o head
        data = [line.strip().split(';') for line in f]
        execute_values(cur, insert_query, data, page_size=500)
    conct.commit()
    print(f"Sucesso! os dados de {table_name} foram inseridos.")
except Exception as e:
    conct.rollback()
    print(f"Erro! Não foi possivel inserir os dados de {table_name}: {e}")

finally:
    cur.close()
    conct.close()
