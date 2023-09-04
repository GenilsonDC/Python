# By Genilson do Carmo on 04/09/2023

import pandas as pd
import matplotlib.pyplot as plt

arquivo_dados = pd.read_csv("Pandas/Dados/ClienteTransacao.csv", delimiter=';')
# Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL
arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(
    ",", ".").astype(float)
total_brl = arquivo_dados.groupby("Client")["Total Price BRL"].sum()

# Criando Graficos de Barra
plt.figure(figsize=(10, 8))
total_brl.plot(kind="bar")
plt.title("Valor Total em BRL por cliente")
plt.xlabel("Cliente")
plt.ylabel("Valor total em BRL")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
