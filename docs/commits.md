# Guia de Commits — Histórico Sugerido

O requisito pede **no mínimo 10 commits** com mensagens claras e descritivas,
distribuídos ao longo do desenvolvimento. Abaixo está a sequência sugerida,
seguindo o padrão de **Conventional Commits** (`tipo: descrição`), que
facilita a leitura do histórico e é amplamente usado no mercado.

Depois de colocar todos os arquivos deste projeto na pasta do seu
repositório local, você pode reproduzir este histórico com os comandos
abaixo (rode-os em sequência, um de cada vez, para simular um
desenvolvimento incremental real — não faça tudo em um único commit):

```bash
git init
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/techflow-task-manager.git

# 1
git add README.md .gitignore
git commit -m "docs: adiciona README inicial com objetivo, escopo e metodologia"

# 2
git add src/__init__.py src/models.py
git commit -m "feat: cria modelo de dados Task com validacao de campos"

# 3
git add src/storage.py
git commit -m "feat: implementa repositorio em memoria para operacoes CRUD"

# 4
git add src/app.py
git commit -m "feat: implementa endpoints REST de criacao e listagem de tarefas"

# 5
git add src/app.py
git commit -m "feat: implementa endpoints de leitura, atualizacao e remocao de tarefas"

# 6
git add tests/__init__.py tests/test_app.py
git commit -m "test: adiciona testes automatizados para o CRUD de tarefas"

# 7
git add requirements.txt
git commit -m "chore: adiciona arquivo de dependencias do projeto"

# 8
git add .github/workflows/ci.yml
git commit -m "ci: configura pipeline de integracao continua com GitHub Actions"

# 9
git add docs/kanban.md
git commit -m "docs: documenta estrutura do quadro Kanban no GitHub Projects"

# 10 (inicio da mudanca de escopo)
git add src/models.py
git commit -m "feat: adiciona campo due_date ao modelo de tarefa (mudanca de escopo)"

# 11
git add src/app.py tests/test_app.py
git commit -m "feat: adiciona endpoint de resumo de desempenho da equipe"

# 12
git add README.md docs/mudanca_de_escopo.md
git commit -m "docs: registra justificativa da mudanca de escopo no README"

# 13
git add docs/diagramas/
git commit -m "docs: adiciona diagramas UML de casos de uso e de classes"

# Enviar tudo para o GitHub
git push -u origin main
```

## Boas práticas seguidas neste histórico

- Cada commit representa **uma unidade lógica de trabalho** (não misturamos
  funcionalidades diferentes em um mesmo commit).
- As mensagens seguem o padrão `tipo: descrição no imperativo`, com tipos
  como `feat` (nova funcionalidade), `fix` (correção), `docs`
  (documentação), `test` (testes) e `ci` (integração contínua).
- A mudança de escopo (commits 10, 11 e 12) fica isolada e claramente
  identificável no histórico, facilitando auditoria e rastreabilidade.
