# TechFlow Task Manager

Sistema de gerenciamento de tarefas desenvolvido pela **TechFlow Solutions**
para uma startup de logística, permitindo acompanhar o fluxo de trabalho da
equipe em tempo real, priorizar tarefas críticas e monitorar o desempenho
do time, seguindo práticas de Engenharia de Software e metodologias ágeis.

![CI](https://github.com/SEU-USUARIO/techflow-task-manager/actions/workflows/ci.yml/badge.svg)

---

## 1. Objetivo do Projeto

O cliente — uma startup de logística — precisava de um sistema simples e
confiável para:

- Acompanhar o andamento das tarefas da equipe em tempo real;
- Priorizar tarefas críticas (ex.: entregas urgentes, incidentes operacionais);
- Monitorar o desempenho do time por meio de indicadores simples (quantidade
  de tarefas por status e por prioridade).

Este repositório simula, de ponta a ponta, o ciclo de vida do desenvolvimento
desse sistema: planejamento ágil, codificação, testes automatizados,
integração contínua e gestão de mudanças de escopo.

## 2. Escopo do Projeto

**Escopo inicial:**

- API REST para CRUD (Create, Read, Update, Delete) de tarefas;
- Cada tarefa possui: título, descrição, status (A Fazer / Em Progresso /
  Concluído), prioridade (Baixa / Média / Alta / Crítica) e responsável;
- Testes automatizados cobrindo as operações de CRUD;
- Pipeline de Integração Contínua (CI) via GitHub Actions.

**Escopo após a mudança (ver seção 6):**

- Adição do campo `due_date` (prazo de entrega) às tarefas;
- Novo endpoint `/api/tasks/report/summary`, que resume a quantidade de
  tarefas por status e por prioridade — atendendo ao pedido do cliente de
  **monitorar o desempenho da equipe**, requisito citado no desafio original
  mas ainda não coberto pela primeira versão do sistema.

## 3. Metodologia Ágil Adotada

Foi adotada uma abordagem **Kanban**, por ser leve, visual e adequada a um
time pequeno que precisa de visibilidade contínua do fluxo de trabalho
(princípio de "fluxo contínuo" em vez de sprints fechados, mais alinhado à
realidade de uma operação de logística que recebe demandas a qualquer
momento).

O quadro é organizado no **GitHub Projects**, com três colunas:

| A Fazer | Em Progresso | Concluído |
|---|---|---|
| Tarefas planejadas, ainda não iniciadas | Tarefas sendo desenvolvidas no momento | Tarefas finalizadas e validadas |

Cada card do quadro corresponde a uma *issue* do GitHub, vinculada aos
commits que a implementam, permitindo rastreabilidade completa entre
planejamento e código.

> Consulte `docs/kanban.md` para o passo a passo de como o quadro foi
> montado e a lista completa dos cards.

## 4. Estrutura do Repositório

```
techflow-task-manager/
├── README.md                  # Este arquivo
├── requirements.txt           # Dependências Python
├── .gitignore
├── src/                       # Código-fonte da aplicação
│   ├── app.py                 # API REST (Flask) com as rotas do CRUD
│   ├── models.py               # Modelo de dados da Task
│   └── storage.py              # Camada de persistência (repositório em memória)
├── tests/                     # Testes automatizados (PyTest)
│   └── test_app.py
├── docs/                      # Documentação complementar
│   ├── kanban.md               # Estrutura do quadro Kanban e cards
│   ├── commits.md              # Guia/histórico de commits sugeridos
│   ├── mudanca_de_escopo.md    # Justificativa da mudança de escopo
│   └── diagramas/               # Diagramas UML (casos de uso e classes)
└── .github/
    └── workflows/
        └── ci.yml               # Pipeline de CI (GitHub Actions)
```

## 5. Como Executar o Sistema Localmente

### Pré-requisitos
- Python 3.11 ou superior instalado
- `pip` instalado

### Passo a passo

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/techflow-task-manager.git
cd techflow-task-manager

# 2. Criar e ativar um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python -m flask --app src.app run --debug
# A API ficará disponível em http://127.0.0.1:5000
```

### Testando a API manualmente (exemplos com curl)

```bash
# Criar uma tarefa
curl -X POST http://127.0.0.1:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Organizar entregas da manhã", "priority": "Crítica", "assignee": "Carlos"}'

# Listar todas as tarefas
curl http://127.0.0.1:5000/api/tasks

# Atualizar o status de uma tarefa
curl -X PUT http://127.0.0.1:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "Em Progresso"}'

# Ver o resumo de desempenho da equipe
curl http://127.0.0.1:5000/api/tasks/report/summary

# Remover uma tarefa
curl -X DELETE http://127.0.0.1:5000/api/tasks/1
```

### Rodando os testes automatizados

```bash
pytest -v --cov=src --cov-report=term-missing
```

Todos os testes também são executados automaticamente pelo GitHub Actions a
cada `push` ou `pull request` na branch `main` (ver `.github/workflows/ci.yml`).

## 6. Gestão de Mudanças de Escopo

Durante o desenvolvimento, identificamos que o escopo inicial (apenas CRUD
de tarefas) não permitia responder de forma clara a um dos requisitos do
cliente: **"monitorar o desempenho da equipe"**. O CRUD sozinho mostra as
tarefas individualmente, mas não oferece uma visão agregada do fluxo de
trabalho.

**Mudança realizada:**
1. Adição do campo `due_date` (prazo de entrega) ao modelo de tarefa, para
   permitir priorização por urgência;
2. Criação do endpoint `GET /api/tasks/report/summary`, que retorna a
   contagem de tarefas por status e por prioridade.

**Justificativa:** sem essa mudança, o sistema atenderia apenas parcialmente
ao pedido do cliente. A alteração foi pequena o suficiente para não
comprometer o prazo, mas essencial para entregar valor real ao usuário final
(o gestor da equipe de logística, que precisa desses indicadores para tomar
decisões rápidas).

**Processo de gestão da mudança:**
- Um novo card foi criado no quadro Kanban (coluna "A Fazer") descrevendo a
  necessidade;
- O card foi movido para "Em Progresso" durante a implementação;
- A implementação foi registrada em commits específicos (ver
  `docs/commits.md`);
- O card foi movido para "Concluído" após os testes automatizados
  confirmarem o funcionamento da nova funcionalidade;
- Esta seção do README foi atualizada como registro formal da mudança.

Detalhes completos em `docs/mudanca_de_escopo.md`.

## 7. Controle de Qualidade

- **Testes automatizados:** implementados com PyTest, cobrindo criação,
  leitura, atualização, remoção de tarefas, validação de dados inválidos e o
  endpoint de resumo (13 casos de teste no total).
- **Integração Contínua:** configurada via GitHub Actions
  (`.github/workflows/ci.yml`), executando os testes e um *smoke test* de
  inicialização da aplicação a cada alteração enviada ao repositório.
- **Cobertura de código:** monitorada com `pytest-cov`.

## 8. Autor / Equipe

Projeto desenvolvido como atividade acadêmica da disciplina de Engenharia de
Software, simulando o papel de desenvolvedor e gestor de projetos ágeis na
empresa fictícia TechFlow Solutions.

## 9. Licença

Projeto de uso educacional, distribuído sob licença MIT (ver `LICENSE`).
