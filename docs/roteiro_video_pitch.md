# Roteiro do Vídeo Pitch — TechFlow Task Manager (até 4 minutos)

> Objetivo: cobrir todos os pontos exigidos no desafio, com tempo estimado
> por bloco. Grave em tela cheia, alternando entre você falando (câmera/
> voz) e a tela compartilhada (GitHub + terminal + aplicação rodando).

---

### Bloco 1 — Abertura e apresentação do projeto (0:00 – 0:40)
**Fale:**
"Olá, meu nome é [seu nome]. Este é o TechFlow Task Manager, um sistema de
gerenciamento de tarefas desenvolvido para a TechFlow Solutions, simulando
uma entrega real para uma startup de logística. O objetivo do sistema é
permitir que a equipe acompanhe o fluxo de trabalho em tempo real, priorize
tarefas críticas e monitore o desempenho do time."

**Tela:** README.md do repositório aberto no GitHub, rolando pela seção de
objetivo e escopo.

---

### Bloco 2 — Metodologia ágil e organização do Kanban (0:40 – 1:30)
**Fale:**
"Para organizar o desenvolvimento, usei a metodologia Kanban, com um quadro
no GitHub Projects dividido em três colunas: A Fazer, Em Progresso e
Concluído. Cada card representa uma issue do repositório, conectada
diretamente aos commits que a implementam."

**Tela:** Aba **Projects** aberta, mostrando o quadro completo com os cards
distribuídos nas três colunas. Abra um card para mostrar a descrição e os
labels de prioridade.

---

### Bloco 3 — Demonstração do sistema funcionando (1:30 – 2:30)
**Fale:**
"Agora vou demonstrar o sistema rodando. Ele é uma API REST feita em Python
com Flask, com um CRUD completo de tarefas."

**Tela (terminal + navegador/Postman/curl):**
1. Rode `python -m flask --app src.app run --debug` e mostre o servidor
   subindo;
2. Crie uma tarefa via `curl` ou Postman (`POST /api/tasks`);
3. Liste as tarefas (`GET /api/tasks`);
4. Atualize o status de uma tarefa para "Em Progresso" (`PUT /api/tasks/1`);
5. Mostre o endpoint de resumo (`GET /api/tasks/report/summary`), explicando
   que ele nasceu da mudança de escopo.

---

### Bloco 4 — Testes automatizados (2:30 – 3:00)
**Fale:**
"O sistema conta com 13 testes automatizados escritos em PyTest, cobrindo
criação, leitura, atualização, remoção de tarefas e validação de dados
inválidos."

**Tela:** Terminal rodando `pytest -v --cov=src`, mostrando os testes
passando (todos em verde) e o relatório de cobertura.

---

### Bloco 5 — GitHub Actions (CI) (3:00 – 3:25)
**Fale:**
"Todo esse processo de testes também roda automaticamente a cada push, por
meio de um pipeline de Integração Contínua configurado no GitHub Actions."

**Tela:** Aba **Actions** do repositório, mostrando um workflow executado
com sucesso (ícone verde) e o log de execução dos testes.

---

### Bloco 6 — Mudança de escopo (3:25 – 3:50)
**Fale:**
"Durante o desenvolvimento, percebi que apenas o CRUD não atendia
totalmente ao pedido do cliente de monitorar o desempenho da equipe. Por
isso, simulei uma mudança de escopo: adicionei o campo de prazo de entrega
e criei o endpoint de resumo de desempenho. Essa mudança foi registrada
como um novo card no Kanban, implementada em commits específicos e
documentada no README."

**Tela:** Trecho do README.md com a seção "Gestão de Mudanças" e o card
correspondente no quadro Kanban.

---

### Bloco 7 — Reflexão final (3:50 – 4:00)
**Fale:**
"Esse projeto mostrou, na prática, como a Engenharia de Software vai muito
além de escrever código: envolve planejamento, testes, automação e gestão
de mudanças — pilares essenciais para entregar software confiável no
mercado de tecnologia. Obrigado!"

---

## Checklist antes de gravar

- [ ] Repositório já publicado como **público** no GitHub;
- [ ] Quadro Kanban completo, com pelo menos 10 cards;
- [ ] Pelo menos 10 commits no histórico;
- [ ] Pipeline de CI passando (verde) no momento da gravação;
- [ ] Sistema testado localmente antes de gravar, para evitar erros ao vivo;
- [ ] Vídeo com no máximo 4 minutos, publicado no YouTube (não listado ou
      público) ou Google Drive com link de acesso público;
- [ ] Link do vídeo adicionado ao README.md e ao documento teórico.
