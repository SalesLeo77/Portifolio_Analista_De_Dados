import pandas as pd
import json

def extract_data(file_path):
    """Extrai os dados do arquivo CSV (que na verdade é um JSON)."""
    with open(file_path, "r") as f:
        data = json.load(f)
    # O CSV está dentro da chave "value"
    df = pd.DataFrame(data["value"])
    return df

def transform_data(df):
    """Transforma os dados: converte tipos, calcula média."""
    # Renomear colunas para facilitar o uso
    df = df.rename(columns={
        "cotacaoVenda": "cotacao_venda",
        "cotacaoCompra": "cotacao_compra",
        "dataHoraCotacao": "data_hora_cotacao"
    })

    # Converter a coluna de data/hora para o tipo datetime
    df["data_hora_cotacao"] = pd.to_datetime(df["data_hora_cotacao"])

    # Extrair apenas a data
    df["data"] = df["data_hora_cotacao"].dt.date

    # Calcular a média da cotação (venda + compra) / 2
    df["cotacao_media"] = (df["cotacao_venda"] + df["cotacao_compra"]) / 2

    # Selecionar as colunas relevantes para o output
    df_transformed = df[["data", "cotacao_venda", "cotacao_compra", "cotacao_media"]]

    return df_transformed

def load_data(df, output_file):
    """Carrega os dados transformados em um novo arquivo CSV."""
    df.to_csv(output_file, index=False)
    print(f"Dados processados salvos em {output_file}")

if __name__ == "__main__":
    input_file = "dolar_cotacao_2023.csv"
    output_file = "dolar_cotacao_processado.csv"

    print(f"Iniciando pipeline para {input_file}...")
    # Extração
    raw_data = extract_data(input_file)
    print("Dados extraídos. Primeiras 5 linhas:")
    print(raw_data.head())

    # Transformação
    transformed_data = transform_data(raw_data)
    print("\nDados transformados. Primeiras 5 linhas:")
    print(transformed_data.head())

    # Carga
    load_data(transformed_data, output_file)
    print("Pipeline concluído.")


