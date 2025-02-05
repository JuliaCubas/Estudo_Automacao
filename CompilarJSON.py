import json

def combinar_jsons(*arquivos_json, arquivo_saida="json_Resultados_combinados2.0.json"):
    """
    Combina múltiplos arquivos JSON em um único arquivo JSON.
    
    :param arquivos_json: Lista de caminhos para os arquivos JSON a serem combinados.
    :param arquivo_saida: Nome do arquivo de saída com os JSONs combinados.
    """
    dados_combinados = []

    for arquivo in arquivos_json:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

                if isinstance(dados, dict):
                    dados_combinados.append(dados)
                elif isinstance(dados, list):
                    dados_combinados.extend(dados)
                else:
                    raise ValueError(f"O conteúdo de {arquivo} não é um objeto JSON válido.")
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        json.dump(dados_combinados, f, ensure_ascii=False, indent=4)

    print(f"Arquivos combinados com sucesso em '{arquivo_saida}'.")

combinar_jsons(
    "AtaJSON/Resultado_1",
    "AtaJSON/Resultado_2",
    "AtaJSON/Resultado_3",
    "AtaJSON/Resultado_4"
)
