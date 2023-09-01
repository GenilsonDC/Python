import pandas as pd
import requests
import io


def main():
    try:
        # URL do arquivo na nuvem
        url = "https://drive.google.com/uc?id=1ynn2dtqFwQJt3ruH761WAt1ftEgoQ5YP"
        # CABECALHO: Cliente;Porduto;Valor unit R$;Quantidade
        # Obter o conteúdo do arquivo da URL
        response = requests.get(url)
        content = response.content.decode('utf-8')

        # Criar um objeto io.StringIO para simular um arquivo
        file_like = io.StringIO(content)

        # Lê o arquivo usando o pandas
        arquivo_nuvem = pd.read_csv(file_like, delimiter=';')

        # Converte a coluna "Quantidade" para valores numéricos
        arquivo_nuvem["Quantidade"] = pd.to_numeric(
            arquivo_nuvem["Quantidade"])

        arquivo_nuvem["TOTAL"] = arquivo_nuvem["Valor unit R$"] * \
            arquivo_nuvem["Quantidade"]

        cliente_desc = arquivo_nuvem.sort_values(
            by="Quantidade", ascending=False)

        print(
            "\n******************************************************************************")
        print(
            "*****         Cliente --- Produto --- Quantidade                         *****")
        print(
            "******************************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']} ---- {row['Porduto']} ---- {row['Quantidade']}")
        print(
            "----------------------------------------------------------------------------\n")

        print(
            "\n******************************************************************************")
        print(
            "*****         Cliente --- Produto --- Valor unit --- Quantidade          *****")
        print(
            "******************************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']} ---- {row['Porduto']} ---- {row['Valor unit R$']} ---- {row['Quantidade']}")
        print(
            "----------------------------------------------------------------------------\n")

        print(
            "\n**********************************************************************************")
        print(
            "*****         Cliente --- Produto --- Valor unit --- Quantidade --- TOTAL    *****")
        print(
            "**********************************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']} ---- {row['Porduto']} ---- {row['Valor unit R$']} ---- {row['Quantidade']} ---- {row['TOTAL']:.2f}")
        print(
            "-------------------------------------------------------------------------------------\n")

    except Exception as e:
        print("Erro ao carregar dados:", e)


if __name__ == "__main__":
    main()
