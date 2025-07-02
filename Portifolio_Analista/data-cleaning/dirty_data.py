import pandas as pd
import numpy as np

def dirty_dataset(file_path):
    df = pd.read_csv(file_path)

    # 1. Introduzir valores ausentes (NaNs)
    for col in ["email", "phone", "job_title"]:
        if col in df.columns:
            df.loc[df.sample(frac=0.1).index, col] = np.nan

    # 2. Introduzir formatação inconsistente (mixed case, extra spaces)
    for col in ["first_name", "last_name"]:
        if col in df.columns:
            df.loc[df.sample(frac=0.1).index, col] = df[col].astype(str).str.upper()
            df.loc[df.sample(frac=0.1).index, col] = df[col].astype(str).apply(lambda x: x + "  ")

    # 3. Introduzir linhas duplicadas
    duplicate_rows = df.sample(n=5, random_state=42)
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    # 4. Introduzir tipos de dados incorretos (números como strings)
    # Assumindo que 'phone' deveria ser numérico, mas pode vir como string
    # Vamos introduzir alguns valores não numéricos para simular isso
    if "phone" in df.columns:
        df.loc[df.sample(frac=0.05).index, "phone"] = "N/A"

    return df

if __name__ == "__main__":
    dirty_df = dirty_dataset("people.csv")
    dirty_df.to_csv("people_dirty.csv", index=False)
    print("Dataset 'people_dirty.csv' criado com sucesso!")

