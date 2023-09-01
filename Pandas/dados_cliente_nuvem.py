import pandas as pd
import requests
import io


def main():
    url = "https://drive.google.com/file/d/1XxeVOdtN6qmxQifSZDgSs5ftPBb8k1H-/view?usp=sharing"

    try:
        response = requests.get(url)
        content = response.content.decode('utf-8')
        # Substituir vírgulas por pontos para números decimais
        content = content.replace(',', '.')

        file_like = io.StringIO(content)

        # Lê o arquivo usando o pandas
        arquivo_dados = pd.read_csv(file_like, delimiter=';')

        # Extraindo e calculando o volume negociado por cliente
        vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()
        # vol_negociado = arquivo_dados.groupby("Client").sum(" ")    # Saida "Melhor" para o terminal, não imprime o tipo de dado
        print()
        print(
            "******************************************************************************")
        print(
            "*****                    Volume negociado por Cliente                    *****")
        print(
            "******************************************************************************")

        print(vol_negociado)
        print("-------------------------------------")
        print()

        print(
            "******************************************************************************")
        print(
            "*****        Volume negociado por Position(SELL - BUY) do cliente        *****")
        print(
            "******************************************************************************")

        positions = arquivo_dados.groupby(
            ["Client", "Position"])["Amount"].sum()
        print(positions)
        print("-------------------------------------")
        print()

        print(
            "******************************************************************************")
        print(
            "*****                      Media de Total Price BRL                      *****")
        print(
            "******************************************************************************")

        arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(
            ",", ".").astype(float)
        media = arquivo_dados.groupby("Position")["Total Price BRL"].mean()
        print(media)
        print("-------------------------------------")
        print()

        # arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(",", ".").astype(float)

        print("******************************************************************************\n*****                Media de Total Price BRL por cliente                *****\n******************************************************************************")
        media_cliente = arquivo_dados.groupby(["Client", "Position"])[
            "Total Price BRL"].mean()
        print(media_cliente)
        print("-------------------------------------")
        print()

    except Exception as e:
        print("Erro ao carregar dados !", e)


if __name__ == "__main__":
    main()
