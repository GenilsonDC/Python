import pandas as pd

arquivo_dados = pd.read_csv("Pandas/Dados/ClienteTransacao.csv", delimiter=';') 
# Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL

# Extraindo e calculando o volume negociado por cliente
vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()    
# vol_negociado = arquivo_dados.groupby("Client").sum(" ")    # Saida "Melhor" para o terminal, não imprime o tipo de dado

print("\n***** Volume negociado por Cliente *****")
print(vol_negociado)
print("****************************************")
print()

print("\n***** Volume negociado por Position(SELL - BUY) do cliente *****")
positions = arquivo_dados.groupby(["Client", "Position"])["Amount"].sum()
print(positions)
print("****************************************")
print()