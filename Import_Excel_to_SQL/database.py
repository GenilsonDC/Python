import pandas as pd
from sqlalchemy import create_engine


def import_csv_to_postgres(csv_file, table_name, db_params):
    df = pd.read_csv(csv_file, delimiter=';')

    engine = create_engine(
        f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

    df.to_sql(table_name, engine, if_exists='append', index=False)
