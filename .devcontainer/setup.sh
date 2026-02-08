#!/bin/bash

# Cores para facilitar a leitura no terminal (TDAH-friendly) 🎨
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🏗️ Iniciando configuração do ambiente Pantheon...${NC}"

# 1. Criar o ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    echo -e "${BLUE}📦 Criando ambiente virtual (.venv)...${NC}"
    python -m venv .venv
else
    echo -e "${GREEN}✅ Ambiente virtual já existe.${NC}"
fi

# 2. Ativar e Instalar Dependências
echo -e "${BLUE}📥 Instalando/Atualizando dependências...${NC}"
source .venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependências instaladas.${NC}"
else
    echo -e "${BLUE}⚠️ requirements.txt não encontrado. Pulando instalação.${NC}"
fi

# 3. Configurar o Cofre de Segredos (.env)
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo -e "${BLUE}🔐 Criando arquivo .env a partir do exemplo...${NC}"
        cp .env.example .env
        echo -e "${GREEN}✅ .env criado. NÃO ESQUEÇA de preencher suas chaves!${NC}"
    fi
fi

echo -e "${GREEN}🚀 Setup concluído com sucesso! Bom trabalho, Vinicius.${NC}"
