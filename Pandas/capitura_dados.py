import pandas as pd

arquivo_dados = pd.read_csv("Pandas/Dados/ClienteTransacao.csv", delimiter=';')
# Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL

# Vamos extrair e calcular o volume negociado por Client
vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()
print("\n***** Volume negociado por Cliente *****")

print(f"{vol_negociado}")
print("****************************************")
print()

