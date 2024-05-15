
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values

db_name = 'ETL'
db_host = 'localhost'
db_port = '5432'
db_user = 'postgres'
db_passw = '00000'

try:
    conct = psycopg2.connect(
        dbname=db_name,
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_passw
    )
except psycopg2.Error as e:
    print(f"Erro! Não foi possivel conectar ao {db_name}: {e}")
    exit()

cur = conct.cursor()
# --------------------------------
csv_file = 'Dados/Vendas.csv'
# --------------------------------
table_name = 'vendas'
# --------------------------------

insert_query = sql.SQL("""
INSERT INTO {}(SKU, Qtd_Vendida, Loja, Data_da_Venda, Codigo_Cliente) VALUES %s;                       
""").format(sql.Identifier(table_name))

try:
    with open(csv_file, 'r') as f:
        next(f)
        data = [line.strip().split(';') for line in f]
        execute_values(cur, insert_query, data, page_size=500)
    conct.commit()
    print(f"Sucesso! Os dados de  {table_name} foram inseridos")
except Exception as e:
    conct.rollback()
    print(f"Erro! Não foi possivel inserir os novos dados: {e}")
finally:
    cur.close()
    conct.close()
