# Modelo de Documentação de Projeto

## Título do Projeto: Limpeza e Preparação de Dados de Pessoas

### 1. Visão Geral

*   **Descrição:** Este projeto demonstra habilidades em limpeza e preparação de dados, transformando um dataset simuladamente "sujo" em um formato limpo e consistente, pronto para análise.
*   **Problema de Negócio:** Dados do mundo real frequentemente contêm inconsistências, valores ausentes, duplicatas e erros de formatação que impedem análises precisas e a construção de modelos confiáveis. Este projeto aborda a necessidade de garantir a qualidade dos dados antes de qualquer etapa de análise.
*   **Relevância:** A limpeza de dados é uma etapa crucial no pipeline de análise de dados, garantindo a integridade e a confiabilidade dos insights gerados. Um dataset limpo economiza tempo, reduz erros e melhora a performance de modelos subsequentes.

### 2. Coleta e Preparação de Dados

*   **Fontes de Dados:** Um dataset base (`people.csv`) foi obtido de um repositório público (GitHub - lawlesst/vivo-sample-data). Para simular um cenário de dados "sujos", um script Python (`dirty_data.py`) foi utilizado para introduzir intencionalmente valores ausentes, inconsistências de formatação, duplicatas e tipos de dados incorretos no dataset original, gerando o arquivo `people_dirty.csv`.
*   **Limpeza e Transformação:** As seguintes etapas foram realizadas para limpar e preparar os dados:
    *   **Tratamento de Valores Ausentes:** Valores ausentes nas colunas de texto (`email`, `phone`, `job_title`) foram preenchidos com "Unknown".
    *   **Padronização de Formatação:** Nomes (`first_name`, `last_name`) foram padronizados para o formato de título (primeira letra maiúscula, restante minúscula) e espaços extras foram removidos.
    *   **Remoção de Duplicatas:** Linhas duplicadas foram identificadas e removidas para garantir a unicidade dos registros.
    *   **Correção de Tipos de Dados:** A coluna `phone` foi convertida para um tipo numérico, tratando valores não numéricos como ausentes (NaN) para permitir análises quantitativas.
*   **Ferramentas Utilizadas:** Python, com as bibliotecas Pandas e NumPy, foi a principal ferramenta utilizada para todas as etapas de coleta (simulada), introdução de sujeira e limpeza/transformação dos dados.

### 3. Análise Exploratória de Dados (EDA)

*   **Principais Descobertas:** (Esta seção será preenchida após a análise exploratória do dataset limpo, que será feita em uma etapa posterior, após a confirmação da limpeza.)
*   **Visualizações:** (Esta seção será preenchida após a análise exploratória do dataset limpo.)

### 4. Metodologia e Modelagem

*   **Abordagem:** O projeto focou em uma abordagem sistemática de pré-processamento de dados, aplicando técnicas de limpeza para melhorar a qualidade do dataset.
*   **Algoritmos:** Não foram utilizados algoritmos de modelagem preditiva ou de machine learning neste projeto, pois o foco principal foi a preparação dos dados.
*   **Implementação:** A implementação foi realizada através de um script Python (`clean_data.py`) que encapsula as funções de limpeza e transformação.

### 5. Resultados e Visualizações

*   **Resultados:** O principal resultado foi a transformação do `people_dirty.csv` em `people_cleaned.csv`, um dataset com maior integridade e consistência, pronto para análises futuras. A quantidade de valores ausentes foi reduzida, a formatação padronizada e as duplicatas eliminadas.
*   **Visualizações Finais:** (Esta seção será preenchida após a análise exploratória do dataset limpo.)
*   **Interpretação:** A limpeza de dados é fundamental para a confiabilidade de qualquer análise. Este projeto demonstra a capacidade de identificar e corrigir problemas comuns de qualidade de dados, resultando em um dataset mais robusto.

### 6. Análise Crítica e Próximos Passos

*   **Desafios:** O principal desafio foi a identificação e simulação de diversos tipos de "sujeira" de forma controlada, garantindo que o script de limpeza fosse abrangente o suficiente para lidar com esses problemas. A escolha de um dataset base adequado que permitisse a introdução de diferentes tipos de erros também foi um ponto importante.
*   **Aprendizados:** A importância da validação de dados em cada etapa do processo de limpeza, a flexibilidade necessária para lidar com diferentes tipos de inconsistências e a relevância de documentar cada etapa da transformação dos dados.
*   **Melhorias Futuras:** O projeto poderia ser expandido para incluir validações de dados mais complexas, como validação de e-mails ou números de telefone com expressões regulares, e a criação de um relatório automatizado de qualidade de dados antes e depois da limpeza.

### 7. Código Fonte e Recursos

*   **Repositório GitHub:** (Será adicionado um link para o repositório GitHub após a criação do mesmo.)
*   **Dashboard Interativo:** Não aplicável a este projeto.
*   **Artigo ou Apresentação:** Não aplicável a este projeto no momento.



### 3. Análise Exploratória de Dados (EDA)

Após a limpeza, foi realizada uma Análise Exploratória de Dados para verificar a eficácia das transformações e identificar padrões nos dados limpos.

*   **Principais Descobertas:**
    *   A comparação dos valores ausentes antes e depois da limpeza demonstra uma redução significativa, validando o processo de tratamento de dados. A maioria das colunas que apresentavam valores nulos no dataset "sujo" foram preenchidas ou tratadas no dataset limpo.
    *   A distribuição dos cargos (`title`) mostra uma padronização e contagem mais precisa após a limpeza, indicando que inconsistências de formatação foram corrigidas e duplicatas removidas, resultando em uma visão mais clara dos dados.

*   **Visualizações:**

    ![Comparação de Valores Ausentes](/home/ubuntu/data_cleaning_project/missing_values_comparison.png)
    *Gráfico 1: Comparação dos valores ausentes nas colunas antes (Dirty) e depois (Cleaned) do processo de limpeza.* 

    ![Distribuição de Cargos](/home/ubuntu/data_cleaning_project/job_title_distribution.png)
    *Gráfico 2: Distribuição dos 5 cargos mais frequentes antes (Dirty Data) e depois (Cleaned Data) da limpeza, demonstrando a padronização e correção de dados.*



