import pandas as pd

arquivo_dados = pd.read_csv("Pandas/Dados/ClienteTransacao.csv", delimiter=';') 
# Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL

# Extraindo e calculando o volume negociado por cliente
vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()    
# vol_negociado = arquivo_dados.groupby("Client").sum(" ")    # Saida "Melhor" para o terminal, não imprime o tipo de dado
print()
print("******************************************************************************\n*****                    Volume negociado por Cliente                    *****\n******************************************************************************")

print(vol_negociado)
print("-------------------------------------")
print()

print("******************************************************************************\n*****        Volume negociado por Position(SELL - BUY) do cliente        *****\n******************************************************************************")
positions = arquivo_dados.groupby(["Client", "Position"])["Amount"].sum()
print(positions)
print("-------------------------------------")
print()

print("******************************************************************************\n*****                      Media de Total Price BRL                      *****\n******************************************************************************")
arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(",", ".").astype(float)
media = arquivo_dados.groupby("Position")["Total Price BRL"].mean()
print(media)
print("-------------------------------------")
print()

# arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(",", ".").astype(float)

print("******************************************************************************\n*****                Media de Total Price BRL por cliente                *****\n******************************************************************************")
media_cliente = arquivo_dados.groupby(["Client","Position"])["Total Price BRL"].mean()
print(media_cliente)
print("-------------------------------------")
print()