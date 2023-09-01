import pandas as pd
import requests
import io


def load_data_from_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode('utf-8')
        # Substituir vírgulas por pontos para números decimais
        content = content.replace(',', '.')
        return pd.read_csv(io.StringIO(content), delimiter=';')
    except Exception as e:
        print("Erro ao carregar dados:", e)
        return None


def clean_whitespace(df):
    # Remover espaços em branco das colunas de texto (Client e Position)
    df['Client'] = df['Client'].str.strip()
    df['Position'] = df['Position'].str.strip()

    # Remover espaços em branco das colunas numéricas (Amount e Total Price BRL)
    df['Amount'] = df['Amount'].str.replace(' ', '').astype(float)
    df['Total Price BRL'] = df['Total Price BRL'].str.replace(
        ' ', '').str.replace(',', '.').astype(float)

    return df


def main():
    url = "https://drive.google.com/file/d/1XxeVOdtN6qmxQifSZDgSs5ftPBb8k1H-/view?usp=sharing"

    arquivo_dados = load_data_from_url(url)

    if arquivo_dados is not None:
        # Extraindo e calculando o volume negociado por cliente
        arquivo_dados_cleaned = clean_whitespace(arquivo_dados)
        vol_negociado = arquivo_dados.groupby("Client")["Amount"].sum()
        print("\n******************************************************************************")
        print(
            "*****                    Volume negociado por Cliente                    *****")
        print(
            "******************************************************************************")
        print(vol_negociado)
        print("-------------------------------------\n")

        # print(
        #     "******************************************************************************")
        # print(
        #     "*****        Volume negociado por Position(SELL - BUY) do cliente        *****")
        # print(
        #     "******************************************************************************")
        # positions = arquivo_dados.groupby(
        #     ["Client", "Position"])["Amount"].sum()
        # print(positions)
        # print("-------------------------------------\n")

        # print(
        #     "******************************************************************************")
        # print(
        #     "*****                      Media de Total Price BRL                      *****")
        # print(
        #     "******************************************************************************")
        # arquivo_dados["Total Price BRL"] = arquivo_dados["Total Price BRL"].str.replace(
        #     ",", ".").astype(float)
        # media = arquivo_dados.groupby("Position")["Total Price BRL"].mean()
        # print(media)
        # print("-------------------------------------\n")

        # print(
        #     "******************************************************************************")
        # print(
        #     "*****                Media de Total Price BRL por cliente                *****")
        # print(
        #     "******************************************************************************")
        # media_cliente = arquivo_dados.groupby(["Client", "Position"])[
        #     "Total Price BRL"].mean()
        # print(media_cliente)
        # print("-------------------------------------\n")


if __name__ == "__main__":
    main()
