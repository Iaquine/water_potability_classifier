# Projeto: Versionamento de Modelos de Machine Learning com MLflow

## 1. Introdução e Objetivo

O objetivo deste projeto foi desenvolver um modelo de Machine Learning supervisionado para classificar se uma amostra de água era potável ou não, com base em características físico-químicas extraídas do dataset **Water Potability Dataset**.

Além da construção do modelo, o projeto focou em rastreabilidade, versionamento e boas práticas de engenharia de software, garantindo que o código fosse modular, reprodutível e escalável.

### Principais objetivos técnicos:
- ✅ Criar um pipeline robusto para ingestão, pré-processamento, treinamento e avaliação do modelo.
- ✅ Aplicar boas práticas de engenharia de software, incluindo Design Patterns.
- ✅ Utilizar MLflow para rastrear experimentos, versionar modelos e registrar métricas.
- ✅ Seguir uma estrutura automatizada com ferramentas como Makefile, Poetry e Pre-commit.
- ✅ Gerar uma documentação clara para facilitar a reprodução do projeto.

## 2. Arquitetura do Projeto

O projeto foi estruturado em um formato modular, separando as responsabilidades de forma clara:


📂 water_ml/ ├── 📂 data/ → Armazena o dataset bruto e processado. ├── 📂 notebooks/ → Análises exploratórias (EDA). ├── 📂 src/ → Código-fonte do projeto. │ ├── 📂 data_processing/ → Pipeline de carregamento e tratamento de dados. │ ├── 📂 models/ → Implementação dos modelos e tuning de hiperparâmetros. │ ├── 📂 evaluation/ → Scripts para avaliar modelos. │ ├── 📂 tracking/ → Integração com MLflow. │ ├── 📂 utils/ → Funções auxiliares. ├── 📄 mlflow_tracking.py → Script para registrar os experimentos. ├── 📄 Makefile → Comandos automatizados para rodar o pipeline. ├── 📄 pyproject.toml → Gerenciamento de dependências com Poetry. ├── 📄 README.md → Documentação. ├── 📄 .pre-commit-config.yaml → Configuração para linting e formatação.


## 3. Pipeline de Machine Learning

O pipeline foi organizado da seguinte forma:

### 1️⃣ Coleta e Validação de Dados
O dataset foi carregado via Pandas, e os dados passaram por uma validação utilizando Pydantic. Features ausentes foram tratadas com técnicas como imputação estatística e remoção de outliers.

### 2️⃣ Pré-processamento e Engenharia de Features
A normalização das variáveis foi realizada para evitar impactos negativos em algoritmos sensíveis a escala. Além disso, novas features foram criadas (quando necessário) para melhorar a separabilidade das classes.

### 3️⃣ Treinamento de Modelos
- Random Forest (modelo base devido à robustez contra dados faltantes).

Cada modelo foi avaliado com métricas como Acurácia, Precisão, Recall e F1-score.

### 4️⃣ Registro e Versionamento com MLflow
Cada execução de treinamento foi registrada no MLflow, armazenando:
- ✅ Hiperparâmetros usados no modelo.
- ✅ Métricas de performance.
- ✅ Artefatos do modelo (pickle, JSON com metadados).
- ✅ Gráficos de importância de features.

### 5️⃣ Automação e Qualidade de Código
O pipeline foi executado com Makefile, permitindo rodar etapas como:
```bash
make train
make evaluate
make register_model
```
Pre-commit foi utilizado para garantir qualidade de código com checagens de Ruff (linting), isort (ordenação de imports) e black (formatação).

4. Uso de MLflow para Versionamento de Modelos
O MLflow Tracking foi utilizado para registrar todas as execuções do modelo.

1️⃣ Registro de um experimento
Cada execução do modelo foi associada a um experimento:
```python
import mlflow

mlflow.set_experiment("Water_Potability_Classification")
with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_metric("accuracy", 0.89)
    mlflow.sklearn.log_model(model, "random_forest_model")
```

2️⃣ Consulta de modelos registrados
O modelo mais recente pode ser recuperado para inferência:

```python
import mlflow.pyfunc

model_uri = "models:/random_forest_model/production"
model = mlflow.pyfunc.load_model(model_uri)
prediction = model.predict(new_data)
```

5. Integração com Boas Práticas de Engenharia

| Ferramenta   | Função                                                       |
|--------------|--------------------------------------------------------------|
| Poetry       | Gerenciamento de dependências e ambiente virtual.            |
| Bump2version | Controle automático da versão do projeto.                    |
| Pre-commit   | Garante qualidade de código antes de commits no Git.         |
| Ruff         | Linter rápido e eficiente para Python.                       |
| Pydantic     | Validação de dados estruturados.                             |
| Makefile     | Automação de comandos recorrentes.                           |
| MLflow       | Rastreamento e versionamento dos modelos.                    |

6. Para acessar a interface de usuário (UI) do MLflow, siga os seguintes passos:

1️⃣ Inicie o servidor MLflow
No terminal, navegue até o diretório do seu projeto onde o MLflow foi configurado e execute o seguinte comando:
```bash
mlflow ui
```
2️⃣ Acesse a UI no navegador:
http://127.0.0.1:5000


7. Conclusão
Este projeto combinou aprendizado de máquina, boas práticas de engenharia de software e versionamento de modelos, garantindo um ciclo de vida bem estruturado e reprodutível. A integração com MLflow permitiu rastrear experimentos, comparar modelos e facilitar a implantação em produção.

O uso de Design Patterns, Makefile, Pre-commit e Poetry contribuiu para um fluxo de trabalho eficiente, tornando o código modular, testável e escalável.