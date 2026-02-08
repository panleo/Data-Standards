# Data-Standards
Basic projects of IA and data analysis

Basic configuration of programming setup on github codespaces, using
docker plus a virtual enviroment for optimized learning focused in ADHD.

# 🏗️ Automação ACC & Inteligência de Dados - Engenharia EPC
**Status:** Configuração de Ambiente e Aguardando Credenciais API.

---

## 🎯 Objetivo do Projeto
Desenvolver uma ferramenta de integração entre o Autodesk Construction Cloud (ACC) e scripts Python para automatizar o fluxo de aprovação de documentos em projetos de subestações de média/alta tensão.

## Estrutura da Solução
graph TD
    A[Início: Script Python] --> B{Possui Token?}
    B -- Não --> C[Solicita OAuth2 Autodesk]
    C --> D[Salva Token em Memória]
    D --> E[Busca Documentos Pendentes]
    B -- Sim --> E
    E --> F{Status: Pendente?}
    F -- Sim --> G[Aplica Lógica de Aprovação]
    G --> H[Atualiza ACC via API]

## 💻 Ambiente de Desenvolvimento (Setup Profissional)
O ambiente foi construído para ser **Cloud-Native** e **Isolado**, garantindo portabilidade total.

### 🛠️ Tecnologias Utilizadas
* **GitHub Codespaces:** Ambiente de desenvolvimento em nuvem.
* **Dev Containers:** Infraestrutura como código para padronização do VS Code.
* **Python 3.12:** Linguagem base para automação e IA.
* **Venv (.venv):** Isolamento de dependências.

### 📋 Passo a Passo para Reconfiguração
Se precisar configurar do zero em outra máquina:
1.  **Clonar o Repositório:** `git clone [URL_DO_REPO]`
2.  **Abrir no Codespaces:** O VS Code detectará o `.devcontainer` e instalará as extensões de IA e Python automaticamente.
3.  **Criar Ambiente Virtual:** ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
4.  **Configurar Segredos:** Criar arquivo `.env` baseado no `.env.example`.

---

## 🔐 Segurança e Boas Práticas (Git Workflow)
* **Cofre (.env):** Jamais subir chaves de API para o GitHub. O arquivo está no `.gitignore`.
* **Commits Semânticos:**
    * `feat:` para novas funcionalidades.
    * `chore:` para configurações e bibliotecas.
    * `fix:` para correções de bugs.

---

## 📝 Próximos Passos (Backlog)
- [x] Configurar Dev Container e Extensões.
- [x] Implementar estrutura de variáveis de ambiente.
- [ ] Obter Client ID e Secret da Autodesk (Tecnova).
- [ ] Mapear Endpoints de Aprovação de Documentos.
- [ ] Criar Mock Data para testes offline.
