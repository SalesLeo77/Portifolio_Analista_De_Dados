import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv("nascidos_vivos_2023.csv", sep=";")

# Exibir as primeiras linhas e informações básicas
print("Primeiras 5 linhas do dataset:")
print(df.head())
print("\nInformações do dataset:")
print(df.info())

# Limpeza e transformação inicial dos dados
# Converter a coluna 'Ano do nascimento' para string antes de filtrar
df["Ano do nascimento"] = df["Ano do nascimento"].astype(str)

# Remover a linha 'Total' se existir, pois já temos o total geral
df = df[df["Ano do nascimento"] != "Total"]

# Converter colunas de números para tipo numérico, ignorando a primeira coluna (Ano do nascimento)
for col in df.columns[1:]:
    # Verificar se a coluna é do tipo object (string) antes de tentar substituir vírgulas
    if df[col].dtype == "object":
        df[col] = df[col].str.replace(",", ".").astype(float)
    else:
        df[col] = df[col].astype(float) # Apenas garantir que é float

# Renomear a coluna 'Ano do nascimento' para 'Ano'
df = df.rename(columns={"Ano do nascimento": "Ano"})

# Análise Exploratória de Dados (EDA) e Visualizações

# 1. Total de nascidos vivos por Unidade da Federação
# Excluir a coluna 'Total' para a visualização por UF
df_uf = df.drop(columns=["Total"])

# Transpor o DataFrame para facilitar a plotagem
df_uf_transposed = df_uf.set_index("Ano").T
df_uf_transposed.columns = df_uf_transposed.columns.astype(str)

# Plotar o total de nascidos vivos por UF para o ano de 2023
# (Assumindo que o dataset contém apenas dados de 2023 ou que queremos focar em 2023)
# Se houver múltiplos anos, podemos somar ou escolher um ano específico

# Para este exemplo, vamos focar no total de nascidos vivos por UF em 2023
# A linha '2023' já contém os dados por UF

# Criar um DataFrame para o ano de 2023 (ou o ano disponível)
df_2023 = df[df["Ano"] == "2023"].drop(columns=["Ano", "Total"])

# Transpor para ter as UFs como índice e os valores como coluna
df_2023_plot = df_2023.T.reset_index()
df_2023_plot.columns = ["UF", "Nascidos Vivos"]

plt.figure(figsize=(12, 7))
sns.barplot(x="UF", y="Nascidos Vivos", data=df_2023_plot.sort_values(by="Nascidos Vivos", ascending=False))
plt.title("Total de Nascidos Vivos por Unidade da Federação (2023)")
plt.xlabel("Unidade da Federação")
plt.ylabel("Número de Nascidos Vivos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("nascidos_vivos_por_uf_2023.png")
plt.show()

# 2. Distribuição de nascidos vivos ao longo dos anos (se houver mais de um ano)
# Como o dataset atual é apenas de 2023, esta visualização seria mais relevante com dados de múltiplos anos.
# Se o dataset fosse de múltiplos anos, o código seria:
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='Ano', y='Total', data=df)
# plt.title('Total de Nascidos Vivos no Brasil ao Longo dos Anos')
# plt.xlabel('Ano')
# plt.ylabel('Número de Nascidos Vivos')
# plt.grid(True)
# plt.savefig('nascidos_vivos_total_anos.png')
# plt.show()

print("\nAnálise e visualizações concluídas. Verifique os arquivos de imagem gerados.")


