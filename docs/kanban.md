# Quadro Kanban — GitHub Projects

Este documento descreve **exatamente** como montar o quadro Kanban na aba
**Projects** do repositório no GitHub, incluindo os cards obrigatórios.

## Como criar o quadro (passo a passo)

1. No repositório, acesse a aba **Projects** → **New project**.
2. Escolha o template **Board** (Kanban).
3. Dê o nome **"TechFlow Task Manager — Kanban"**.
4. Renomeie/configure as colunas para exatamente:
   - `A Fazer`
   - `Em Progresso`
   - `Concluído`
5. Para cada card abaixo, crie uma *issue* no repositório (aba **Issues →
   New issue**) e depois adicione essa issue ao quadro (botão **+ Add item**
   dentro da coluna correspondente). Isso garante rastreabilidade entre o
   card do Kanban, a issue e os commits que a resolvem.
6. Use labels para prioridade, por exemplo: `prioridade:crítica`,
   `prioridade:alta`, `prioridade:média`, `prioridade:baixa`.

## Lista de cards (mínimo de 10, conforme exigido)

### Coluna "Concluído"
1. **Estruturar repositório e diretórios** (`/src`, `/tests`, `/docs`)
2. **Criar README.md inicial** com objetivo, escopo e metodologia
3. **Implementar modelo de dados Task** (`src/models.py`)
4. **Implementar camada de persistência** (`src/storage.py`)
5. **Implementar endpoints CRUD da API** (`src/app.py`)
6. **Escrever testes automatizados do CRUD** (`tests/test_app.py`)
7. **Configurar pipeline de CI com GitHub Actions**
8. **Documentar quadro Kanban** (`docs/kanban.md`)

### Coluna "Em Progresso" (durante a simulação da mudança de escopo)
9. **Adicionar campo `due_date` ao modelo de tarefa**

### Coluna "A Fazer" → depois movido para "Concluído"
10. **Criar endpoint de resumo de desempenho** (`/api/tasks/report/summary`)
11. **Atualizar README com a justificativa da mudança de escopo**
12. **Gravar vídeo pitch de apresentação do projeto**

> Dica: ao finalizar cada item, mova o card manualmente para a coluna
> `Concluído` e, na mensagem do commit relacionado, referencie a issue
> (ex.: `git commit -m "feat: adiciona endpoint de resumo (closes #10)"`).
> O GitHub move automaticamente issues fechadas por commits/PRs vinculados.

## Prints obrigatórios para a Parte Teórica

Lembre-se de capturar (para incluir no documento DOCX/PDF):
- O quadro completo com os cards distribuídos nas 3 colunas;
- Um card aberto mostrando a descrição e os labels;
- O board após a movimentação do card da mudança de escopo.
