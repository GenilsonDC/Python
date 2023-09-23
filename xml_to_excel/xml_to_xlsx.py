import xmltodict as dic
import os
import json
import pandas as pd

todas_notas = os.listdir("./nfs")


def pegar_infos(arquivo, valores):
    with open(f'./nfs/{arquivo}', 'rb') as arquivo_XML:
        dic_arquivo = dic.parse(arquivo_XML)

        try:
            if "NFe" in dic_arquivo:
                infos_NF = dic_arquivo["NFe"]["infNFe"]
            else:
                infos_NF = dic_arquivo["nfeProc"]["NFe"]["infNFe"]

            numero_NF = infos_NF["@Id"]
            nome_emissor_NF = infos_NF["emit"]["xNome"]
            cnpj_emissor = infos_NF["emit"]["CNPJ"]
            cep_endereco_emissor = infos_NF["emit"]["enderEmit"]["CEP"]
            rua_emissor = infos_NF["emit"]["enderEmit"]["xLgr"]
            num_endereco_emissor = infos_NF["emit"]["enderEmit"]["nro"]
            bairro_endereco_emissor = infos_NF["emit"]["enderEmit"]["xBairro"]
            # -----------------------------------------------------------
            nome_cliente_NF = infos_NF["dest"]["xNome"]
            if "CNPJ" in infos_NF["dest"]:  # Atecao ao caminho do campo
                cpf_cnpj_cliente = infos_NF["dest"]["CNPJ"]
            else:
                cpf_cnpj_cliente = infos_NF["dest"]["CPF"]
            cep_endereco_cliente = infos_NF["dest"]["enderDest"]["CEP"]
            rua_cliente = infos_NF["dest"]["enderDest"]["xLgr"]
            num_endereco_cliente = infos_NF["dest"]["enderDest"]["nro"]
            bairro_endereco_cliente = infos_NF["dest"]["enderDest"]["xBairro"]

            valores.append([numero_NF, nome_emissor_NF, cnpj_emissor, cep_endereco_emissor,   rua_emissor, num_endereco_emissor, bairro_endereco_emissor,
                           nome_cliente_NF, cpf_cnpj_cliente, cep_endereco_cliente, rua_cliente, num_endereco_cliente, bairro_endereco_cliente])

        except Exception as e:
            print(f"Não foi possivel carregar os dados:{e}")
            print(json.dumps(dic_arquivo, indent=6))


colunas = ["numero_NF", "nome_emissor_NF", "cnpj_emissor", "cep_endereco_emissor", "rua_emissor", "num_endereco_emissor", "bairro_endereco_emissor",
           "nome_cliente_NF", "cpf_cnpj_cliente", "cep_endereco_cliente", "rua_cliente", "num_endereco_cliente", "bairro_endereco_cliente"]
linhas = []


for arquivo in todas_notas:
    pegar_infos(arquivo, linhas)

tabela = pd.DataFrame(columns=colunas, data=linhas)
tabela.to_excel("Dados_XML_NF.xlsx", index=False)
