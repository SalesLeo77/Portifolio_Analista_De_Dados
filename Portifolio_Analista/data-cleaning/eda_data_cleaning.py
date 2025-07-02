import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os datasets
dirty_df = pd.read_csv("data_cleaning_project/people_dirty.csv")
cleaned_df = pd.read_csv("data_cleaning_project/people_cleaned.csv")

# Visualização 1: Comparação de valores ausentes
missing_dirty = dirty_df.isnull().sum()
missing_cleaned = cleaned_df.isnull().sum()

missing_data = pd.DataFrame({
    'Dirty': missing_dirty,
    'Cleaned': missing_cleaned
})

plt.figure(figsize=(10, 6))
sns.barplot(data=missing_data.T, palette='viridis')
plt.title('Valores Ausentes Antes e Depois da Limpeza')
plt.ylabel('Contagem de Valores Ausentes')
plt.xlabel('Colunas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('data_cleaning_project/missing_values_comparison.png')
plt.close()

# Visualização 2: Distribuição de 'title' antes e depois da limpeza (top 5)
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
dirty_df['title'].value_counts().nlargest(5).plot(kind='bar')
plt.title('Top 5 Cargos (Dirty Data)')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)
cleaned_df['title'].value_counts().nlargest(5).plot(kind='bar')
plt.title('Top 5 Cargos (Cleaned Data)')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('data_cleaning_project/job_title_distribution.png')
plt.close()

print("Visualizações geradas e salvas em data_cleaning_project/")


