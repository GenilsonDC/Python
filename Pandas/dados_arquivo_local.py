import pandas as pd

arquivo_dados = pd.read_csv("Dados/ClienteTransacao.csv", delimiter=';')
# Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL

# Extraindo e calculando o volume negociado por cliente
vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()
# vol_negociado = arquivo_dados.groupby("Client").sum(" ")    # Saida "Melhor" para o terminal, não imprime o tipo de dado
print()
print("******************************************************************************")
print("*****                    Volume negociado por Cliente                    *****")
print("******************************************************************************")

print(vol_negociado)
print("-------------------------------------\n")

print("******************************************************************************")
print("*****        Volume negociado por Position(SELL - BUY) do cliente        *****")
print("******************************************************************************")

positions = arquivo_dados.groupby(["Client", "Position"])["Amount"].sum()
print(positions)
print("-------------------------------------\n")

print("******************************************************************************")
print("*****                      Media de Total Price BRL                      *****")
print("******************************************************************************")

arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(
    ",", ".").astype(float)
media = arquivo_dados.groupby("Position")["Total Price BRL"].mean()
print(media)
print("-------------------------------------\n")
