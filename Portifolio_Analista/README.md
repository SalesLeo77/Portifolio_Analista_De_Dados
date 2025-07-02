# 📊 Portfólio de Analista de Dados

<div align="center">

![Data Analysis](https://img.shields.io/badge/Data-Analysis-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-green?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)

**Demonstrando habilidades em análise de dados através de projetos práticos com dados brasileiros**

[🚀 Ver Projetos](#-projetos) • [🛠️ Tecnologias](#️-tecnologias) • [📞 Contato](#-contato)

</div>

---

## 👨‍💻 Sobre Este Portfólio

Bem-vindo ao meu portfólio de analista de dados! Este repositório demonstra minhas competências em **análise de dados**, **visualização** e **engenharia de dados** através de projetos práticos desenvolvidos com dados reais brasileiros.

### 🎯 Objetivo
Apresentar de forma prática e profissional as habilidades essenciais para a área de análise de dados, incluindo limpeza de dados, visualização e construção de pipelines ETL.

---

## 🚀 Projetos

### 1. 🧹 [Data Cleaning e Preparação](./data-cleaning/)

<table>
<tr>
<td width="60%">

**Demonstração completa de técnicas de limpeza de dados**

- 🔧 **Tecnologias:** Python, Pandas, Matplotlib, Seaborn
- 📊 **Dataset:** Dados sintéticos com problemas intencionais
- 🎯 **Técnicas:** Tratamento de valores ausentes, remoção de duplicatas, padronização
- 📈 **Resultado:** 100% dos problemas identificados e corrigidos

**Destaques:**
- Criação controlada de "dados sujos" para demonstração
- Análise exploratória antes/depois da limpeza
- Visualizações comparativas de qualidade dos dados

</td>
<td width="40%">

```python
# Exemplo do projeto
import pandas as pd
import matplotlib.pyplot as plt

# Análise de valores ausentes
missing_data = df.isnull().sum()
plt.figure(figsize=(10, 6))
missing_data.plot(kind='bar')
plt.title('Valores Ausentes por Coluna')
```

</td>
</tr>
</table>

**[📖 Ver Projeto Completo →](./data-cleaning/)**

---

### 2. 📊 [Visualização de Dados](./data-visualization/)

<table>
<tr>
<td width="60%">

**Criação de visualizações informativas de dados de saúde pública**

- 🔧 **Tecnologias:** Python, Matplotlib, Seaborn
- 📊 **Dataset:** Nascidos Vivos 2023 (DATASUS)
- 🎯 **Técnicas:** Gráficos de barras, análise exploratória, design de visualização
- 📈 **Resultado:** Insights sobre distribuição demográfica brasileira

**Destaques:**
- Dados oficiais do Ministério da Saúde
- Análise de 27 estados brasileiros
- Visualizações profissionais e informativas

</td>
<td width="40%">

```python
# Exemplo do projeto
import seaborn as sns
import matplotlib.pyplot as plt

# Visualização por UF
plt.figure(figsize=(12, 8))
sns.barplot(data=df, x='nascidos', y='uf')
plt.title('Nascidos Vivos por UF - 2023')
plt.xlabel('Número de Nascimentos')
```

</td>
</tr>
</table>

**[📖 Ver Projeto Completo →](./data-visualization/)**

---

### 3. 🔄 [Pipeline de Dados](./data-pipeline/)

<table>
<tr>
<td width="60%">

**Desenvolvimento de pipeline ETL para dados financeiros**

- 🔧 **Tecnologias:** Python, Pandas, APIs REST
- 📊 **Dataset:** Cotações do Dólar (Banco Central do Brasil)
- 🎯 **Técnicas:** Extração via API, transformação, carregamento, automação
- 📈 **Resultado:** Pipeline funcional processando 365 dias de dados

**Destaques:**
- Integração com API oficial do Banco Central
- Pipeline ETL completo e automatizado
- Tratamento de erros e validação de dados

</td>
<td width="40%">

```python
# Exemplo do projeto
import requests
import pandas as pd

# Extração via API
url = "https://api.bcb.gov.br/dados/serie/"
response = requests.get(url)
data = response.json()

# Transformação
df = pd.DataFrame(data)
df['data'] = pd.to_datetime(df['data'])
```

</td>
</tr>
</table>

**[📖 Ver Projeto Completo →](./data-pipeline/)**

---

## 🛠️ Tecnologias

### 💻 Linguagens e Bibliotecas
<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge)

</div>

### 🔧 Ferramentas e Conceitos
- **APIs REST** - Integração com fontes de dados externas
- **ETL** - Extract, Transform, Load
- **EDA** - Análise Exploratória de Dados
- **Git/GitHub** - Controle de versão e colaboração
- **Jupyter Notebooks** - Desenvolvimento interativo

---

## 📊 Competências Demonstradas

<div align="center">

| 🧹 **Data Cleaning** | 📊 **Visualização** | 🔄 **Pipeline ETL** |
|:---:|:---:|:---:|
| Identificação de problemas | Gráficos informativos | Extração de dados |
| Tratamento de valores ausentes | Design de visualização | Transformação |
| Remoção de duplicatas | Análise exploratória | Carregamento |
| Padronização de dados | Comunicação de insights | Automação |

</div>

### 🎯 Habilidades Técnicas
✅ **Manipulação de Dados** - Pandas, NumPy  
✅ **Visualização** - Matplotlib, Seaborn  
✅ **APIs** - Requests, JSON  
✅ **Dados Governamentais** - DATASUS, Banco Central  
✅ **Documentação** - Markdown, Git  

### 🤝 Habilidades Interpessoais
✅ **Comunicação** - Apresentação clara de insights  
✅ **Organização** - Estruturação lógica de projetos  
✅ **Resolução de Problemas** - Abordagem estruturada  
✅ **Atenção aos Detalhes** - Qualidade e precisão  

---

## 📈 Destaques dos Resultados

<div align="center">

| Projeto | Dados Processados | Visualizações | Insights |
|:---:|:---:|:---:|:---:|
| **Data Cleaning** | 110 → 100 registros | 2 gráficos | Qualidade 100% |
| **Visualização** | 27 estados | 1 dashboard | Padrões demográficos |
| **Pipeline ETL** | 365 dias | Pipeline automatizado | Dados financeiros |

</div>

---

## 🎯 Diferenciais

### 🇧🇷 **Foco em Dados Brasileiros**
- Uso de fontes oficiais (DATASUS, Banco Central)
- Relevância para o mercado nacional
- Conhecimento de dados governamentais

### 📚 **Projetos Completos**
- Código funcional e testado
- Documentação profissional
- Dados reais e resultados práticos

### 🔍 **Qualidade Técnica**
- Boas práticas de programação
- Código limpo e comentado
- Estrutura organizada

---

## 📞 Contato

<div align="center">

Interessado em discutir oportunidades em análise de dados? Vamos conversar!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/leonardoosales)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:salesleonardo777@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/salesleo77)

</div>

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

**⭐ Se este portfólio foi útil, considere dar uma estrela no repositório!**

*Última atualização: Julho 2025*

</div>

