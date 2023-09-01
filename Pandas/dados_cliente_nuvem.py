import pandas as pd
import requests
import io


def main():
    try:
        # URL do arquivo na nuvem
        url = "https://drive.google.com/uc?id=17A0MYJRUGHsLjuJZJMzU045jhIh5I3lE"
        # Campos do cabeçalho: Client - Position - Currency - Amount - Total Price BRL

        # Obter o conteúdo do arquivo da URL
        response = requests.get(url)
        content = response.content.decode('utf-8')

        # Criar um objeto io.StringIO para simular um arquivo
        arquivo = io.StringIO(content)

        # Lê o arquivo usando o pandas
        arquivo_nuvem = pd.read_csv(arquivo, delimiter=';')
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.expand_frame_repr', False)

        # Converte a coluna "Quantidade" para valores numéricos
        arquivo_nuvem["Amount"] = pd.to_numeric(arquivo_nuvem["Amount"])

        arquivo_nuvem["Total Price BRL"] = arquivo_nuvem["Total Price BRL"].str.replace(
            ',', '.', regex=True).astype(float)

        Amount = arquivo_nuvem.groupby("Client")["Amount"].sum().reset_index()
        print()
        print(
            "******************************************************************************")
        print(
            "*****                    Volume negociado por Cliente                    *****")
        print(
            "******************************************************************************")
        for i, row in Amount.iterrows():
            print(f"\t{row['Client']:<25} {row['Amount']:<15}")
        print("------------------------------------------------------------------------------ \n")

        print(
            "******************************************************************************")
        print(
            "*****        Volume negociado por Position(SELL - BUY) por cliente        *****")
        print(
            "******************************************************************************")

        positions = arquivo_nuvem.groupby(
            ["Client", "Position"])["Amount"].sum()
        for (client, position), amount in positions.items():
            print(f"\t{client:<25} {position:<15} {amount:<10}")
        print("------------------------------------------------------------------------------ \n")

        print(
            "******************************************************************************")
        print(
            "*****                      Media de Total Price BRL                      *****")
        print(
            "******************************************************************************")

        media = arquivo_nuvem.groupby("Position")["Total Price BRL"].mean()
        for position, avg in media.items():
            print(f"\t{position:<25} {avg:<15.2f}")
        print("------------------------------------------------------------------------------  \n")

    except Exception as e:
        print("Erro ao carregar dados:", e)


if __name__ == "__main__":
    main()
