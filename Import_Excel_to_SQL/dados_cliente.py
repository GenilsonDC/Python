import pandas as pd
from sqlalchemy import create_engine

# Parâmetros de conexão com o banco de dados
db_params = {
    'dbname': 'praticas',
    'user': 'postgres',
    'password': '645711',
    'host': 'localhost',
    'port': '5432'
}

# Caminho do arquivo CSV
csv_file = 'Dados\Book1.csv'

# Nome da tabela no banco de dados
table_name = 'clientes_teste2'

# Lendo o arquivo CSV como um DataFrame do Pandas
df = pd.read_csv(csv_file, delimiter=';')

# Criando uma conexão com o banco de dados
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

# Salvando o DataFrame no banco de dados PostgreSQL com if_exists='append'
df.to_sql(table_name, engine, if_exists='append', index=False)

print('SUCESSO! - Dados importados')
