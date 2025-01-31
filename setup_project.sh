#!/bin/bash

# Nome do diretório principal do projeto
PROJECT_NAME="water_potability_classifier"

# Criando a estrutura de diretórios
mkdir -p $PROJECT_NAME/{data,notebooks,src/{data_processing,models,evaluation,tracking,utils},tests}

# Criando arquivos principais
touch $PROJECT_NAME/{README.md,Makefile,pyproject.toml,.pre-commit-config.yaml}

echo "Estrutura de diretórios criada com sucesso!"
