# Título do Projeto: Pipeline de Dados de Cotação do Dólar

## 1. Introdução

Este projeto demonstra a construção de um pipeline de dados simples (Extração, Transformação e Carga - ETL) utilizando dados de cotação do dólar comercial (venda e compra) fornecidos pelo Banco Central do Brasil. O objetivo é automatizar a coleta, processamento e armazenamento desses dados para análises futuras.

## 2. Fonte de Dados

Os dados foram obtidos através da API de Dados Abertos do Banco Central do Brasil, especificamente o endpoint de cotações diárias do dólar comercial. O dataset contém informações sobre a cotação de compra e venda do dólar, juntamente com a data e hora da cotação.

## 3. Metodologia (ETL)

### 3.1. Extração (Extract)

A etapa de extração envolve a leitura do arquivo CSV (que na verdade é um JSON retornado pela API) contendo as cotações do dólar. Utiliza-se a biblioteca `pandas` para carregar os dados em um DataFrame, facilitando o acesso e manipulação.

### 3.2. Transformação (Transform)

A fase de transformação realiza as seguintes operações nos dados brutos:

*   **Renomear Colunas:** As colunas `cotacaoVenda`, `cotacaoCompra` e `dataHoraCotacao` são renomeadas para `cotacao_venda`, `cotacao_compra` e `data_hora_cotacao`, respectivamente, para padronização e melhor legibilidade.
*   **Conversão de Tipo de Dados:** A coluna `data_hora_cotacao` é convertida para o tipo `datetime` para permitir operações baseadas em tempo.
*   **Extração de Data:** Uma nova coluna `data` é criada, contendo apenas a data da cotação, sem a informação de hora.
*   **Cálculo de Média:** Uma nova coluna `cotacao_media` é calculada, representando a média entre a cotação de venda e a cotação de compra do dólar.
*   **Seleção de Colunas:** Apenas as colunas `data`, `cotacao_venda`, `cotacao_compra` e `cotacao_media` são mantidas no DataFrame transformado, descartando informações desnecessárias.

### 3.3. Carga (Load)

Na etapa de carga, os dados transformados são salvos em um novo arquivo CSV (`dolar_cotacao_processado.csv`). Isso garante que os dados processados estejam disponíveis para consumo por outras aplicações ou para análises posteriores.

## 4. Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal para o desenvolvimento do pipeline.
*   **Pandas:** Biblioteca Python para manipulação e análise de dados.

## 5. Resultados

O pipeline foi executado com sucesso, processando os dados de cotação do dólar para o ano de 2023. O arquivo `dolar_cotacao_processado.csv` contém as cotações de venda, compra e a média diária do dólar, prontas para serem utilizadas em análises ou visualizações.

## 6. Próximos Passos

Este pipeline pode ser expandido para incluir:

*   Integração com bancos de dados (SQL ou NoSQL) para armazenamento persistente.
*   Agendamento da execução do pipeline para atualização diária dos dados.
*   Implementação de tratamento de erros e logs mais robustos.
*   Criação de visualizações e dashboards a partir dos dados processados.

