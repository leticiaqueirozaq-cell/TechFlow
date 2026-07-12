# Registro de Mudança de Escopo

## 1. Contexto

Após a implementação inicial do CRUD de tarefas, revisamos os requisitos
originais do cliente (startup de logística) e identificamos uma lacuna: o
pedido de **"monitorar o desempenho da equipe"** não era plenamente atendido
apenas com a listagem individual de tarefas.

## 2. Alteração Proposta

| Item | Escopo Original | Escopo Revisado |
|---|---|---|
| Campos da tarefa | title, description, status, priority, assignee | + `due_date` (prazo de entrega) |
| Endpoints | CRUD básico (`/api/tasks`) | + `GET /api/tasks/report/summary` |
| Capacidade de monitoramento | Nenhuma visão agregada | Contagem de tarefas por status e prioridade |

## 3. Justificativa

- **Valor para o cliente:** um gestor de logística precisa saber, de forma
  rápida, quantas tarefas críticas estão em aberto e quantas foram
  concluídas — não apenas visualizar uma lista.
- **Baixo risco/esforço:** a mudança reaproveita a estrutura já existente
  (modelo `Task` e repositório), exigindo apenas um novo campo e um novo
  endpoint, sem alterar contratos já publicados da API.
- **Alinhamento ágil:** dentro do Kanban, mudanças de escopo pequenas e bem
  justificadas são esperadas e tratadas como um novo card, não como um
  retrabalho — reforçando a natureza adaptativa da metodologia.

## 4. Processo de Aprovação e Rastreabilidade (simulado)

1. Necessidade identificada durante revisão do backlog;
2. Criado o card **"Adicionar due_date e endpoint de resumo"** na coluna
   `A Fazer` do quadro Kanban;
3. Card movido para `Em Progresso` ao iniciar a implementação;
4. Implementação feita em commits isolados (ver `docs/commits.md`,
   commits 10 e 11);
5. Testes automatizados criados/atualizados para cobrir a nova
   funcionalidade (`test_summary_report`);
6. Pipeline de CI validado com sucesso após a mudança;
7. Card movido para `Concluído`;
8. README.md atualizado (seção "Gestão de Mudanças") registrando a decisão.

## 5. Impacto

- **Compatibilidade:** nenhuma alteração quebra o comportamento anterior da
  API — `due_date` é um campo opcional, e o novo endpoint é aditivo.
- **Testes:** cobertura ampliada de 12 para 13 casos de teste.
- **Cronograma:** impacto mínimo, absorvido dentro do fluxo contínuo do
  Kanban, sem necessidade de repriorizar outras tarefas.

## 6. Lições Aprendidas

Mudanças de escopo são naturais em projetos ágeis quando bem geridas: a
chave é isolar a mudança em cards e commits específicos, justificar a
decisão por escrito e validar com testes automatizados antes de considerar
a tarefa concluída — evitando que o "scope creep" comprometa a qualidade ou
o prazo do projeto.
