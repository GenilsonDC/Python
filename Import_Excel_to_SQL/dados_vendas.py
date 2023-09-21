
from database import import_csv_to_postgres

# Parâmetros de conexão com o banco de dados
db_params = {
    'dbname': 'ETL',
    'user': 'postgres',
    'password': '572711',
    'host': 'localhost',
    'port': '5432'
}

# Caminho do arquivo CSV
csv_file = './Dados/Vendas.csv'

# Nome da tabela no banco de dados
table_name = 'Vendas'

import_csv_to_postgres(csv_file, table_name, db_params)
print('\n \tSUCESSO! - Dados de Vendas importados')
