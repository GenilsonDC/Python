import pandas as pd
import requests
import io


def main():
    try:
        # URL do arquivo na nuvem
        url = "https://drive.google.com/uc?id=1ynn2dtqFwQJt3ruH761WAt1ftEgoQ5YP"
        # CABECALHO: Cliente ---  Porduto --- Valor unit R$  ---  Quantidade
        # Obter o conteúdo do arquivo da URL
        response = requests.get(url)
        content = response.content.decode('utf-8')

        # Criar um objeto io.StringIO para simular um arquivo
        arquivo = io.StringIO(content)

        # Lê o arquivo usando o pandas
        arquivo_nuvem = pd.read_csv(arquivo, delimiter=';')

        # Converte a coluna "Quantidade" para valores numéricos
        arquivo_nuvem["Quantidade"] = pd.to_numeric(
            arquivo_nuvem["Quantidade"])
        arquivo_nuvem["TOTAL"] = arquivo_nuvem["Valor unit R$"] * \
            arquivo_nuvem["Quantidade"]

        cliente_desc = arquivo_nuvem.sort_values(
            by="Quantidade", ascending=False)

        print(
            "\n******************************************************************")
        print(
            "*****      CLIENTE               PRODUTO       QUANTIDADE    *****")
        print(
            "******************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']:<25} {row['Porduto']:<15} {row['Quantidade']:<12}")
        print(
            "-----------------------------------------------------------------")

        print(
            "\n****************************************************************************************")
        print(
            "*****      CLIENTE               PRODUTO      VALOR UNIT. R$      QUANTIDADE       *****")
        print(
            "****************************************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']:<25} {row['Porduto']:<15} {row['Valor unit R$']:<17}  {row['Quantidade']:<12}")
        print(
            "-----------------------------------------------------------------------------------------")

        print(
            "\n************************************************************************************************")
        print(
            "*****      CLIENTE               PRODUTO      VALOR UNIT. R$      QUANTIDADE      TOTAL    *****")
        print(
            "************************************************************************************************")

        for i, row in cliente_desc.iterrows():
            print(
                f"\t{row['Cliente']:<25} {row['Porduto']:<15} {row['Valor unit R$']:<17}  {row['Quantidade']:<12} {row['TOTAL']:.2f}")
            print(
                "---------------------------------------------------------------------------------------------")

    except Exception as e:
        print("Erro ao carregar dados:", e)


if __name__ == "__main__":
    main()
