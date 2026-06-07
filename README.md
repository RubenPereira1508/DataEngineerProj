# Goldenergy Weather ETL Pipeline & Analytics Dashboard ⚡☀️

Este projeto consiste num **pipeline ETL (Extract, Transform, Load) de Engenharia de Dados** completo, integrado com um dashboard analítico desenvolvido no **Power BI**. O objetivo principal é extrair, processar e consolidar dados meteorológicos e de radiação solar para correlacioná-los com potenciais picos de consumo elétrico e capacidade de geração de energia renovável no mercado ibérico (OMIE).

O projeto foi totalmente contentorizado utilizando o **Docker** para garantir a portabilidade e a consistência do ambiente de execução, eliminando conflitos de dependências locais.

---

## 🏗️ Arquitetura do Projeto

O pipeline segue uma arquitetura modular e linear dividida em três fases principais:

1. **Extract (`src/extract.py`):** Consome dados históricos e em tempo real de uma API meteorológica pública. Os dados brutos horários são extraídos e armazenados localmente em formato CSV.
2. **Transform (`src/transform.py`):** Utiliza a biblioteca **Pandas** para carregar os dados brutos, efetuar a limpeza de dados, tratar tipos de variáveis e agregar as métricas horárias em valores máximos, mínimos e médias diárias.
3. **Load (`src/load.py`):** Estabelece ligação a uma base de dados relacional **SQLite** (`goldenergy_warehouse.db`) e insere os registos estruturados na tabela `daily_weather` utilizando SQL, garantindo a integridade dos dados.

---

## 📂 Estrutura de Pastas

```text
DataEngineerProj/
├── data/                             # Armazenamento local de dados (ignorado no Git)
│   ├── raw_weather_data.csv          # Dados horários brutos obtidos da API
│   ├── clean_weather_data.csv        # Dados diários agregados e limpos pelo Pandas
│   └── goldenergy_warehouse.db       # Base de dados SQLite (Data Warehouse local)
├── src/                              # Código-fonte do Pipeline ETL
│   ├── __init__.py
│   ├── extract.py                    # Script de extração da API
│   ├── transform.py                  # Script de transformação e engenharia de atributos
│   └── load.py                       # Script de carga para a base de dados SQL
├── Dockerfile                        # Configuração do contentor Docker
├── requirements.txt                  # Dependências do projeto Python (Pandas, Requests, etc.)
├── .gitignore                        # Ficheiros e pastas ignorados pelo Git
└── README.md                         # Documentação do projeto (este ficheiro)

---

#📊 Dashboard & Insights de Negócio (Power BI)

Os dados processados pelo pipeline foram conectados ao Power BI para extrair valor estratégico alinhado com o mercado de comercialização de energia e soluções renováveis:

Evolução da Temperatura (Máxima vs. Média): Permite identificar com precisão ondas de calor (como o pico registado no final de maio). Para uma comercializadora de energia, estes picos traduzem-se num aumento imediato do consumo elétrico (sistemas de climatização), influenciando a estratégia de previsão de carga e compra de energia.

Potencial de Radiação Solar Total: Analisa a densidade solar diária. Dias com níveis elevados de radiação indicam uma forte oportunidade para promover soluções de autoconsumo solar (painéis fotovoltaicos) e prever uma maior injeção de energia verde na rede.

KPIs Executivos (Cartões): Destaca no topo do relatório as métricas críticas de controlo — Temperatura Máxima Absoluta registada e o Acumulado de Radiação Solar do período para tomada de decisões rápidas por parte da gestão.
