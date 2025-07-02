import pandas as pd
import numpy as np

def clean_dataset(file_path):
    df = pd.read_csv(file_path)

    # 1. Tratar valores ausentes (NaNs)
    # Preencher valores ausentes em colunas de texto com 'Unknown'
    for col in ["email", "phone", "job_title"]:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # 2. Padronizar formatação inconsistente
    for col in ["first_name", "last_name"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # 3. Remover linhas duplicadas
    df.drop_duplicates(inplace=True)

    # 4. Corrigir tipos de dados incorretos
    if "phone" in df.columns:
        # Substituir 'N/A' por NaN e converter para tipo numérico, se possível
        df["phone"] = df["phone"].replace("N/A", np.nan)
        # Tentar converter para numérico, forçando erros para NaN
        df["phone"] = pd.to_numeric(df["phone"], errors='coerce')

    return df

if __name__ == "__main__":
    cleaned_df = clean_dataset("people_dirty.csv")
    cleaned_df.to_csv("people_cleaned.csv", index=False)
    print("Dataset 'people_cleaned.csv' criado com sucesso!")

