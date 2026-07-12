"""
models.py
----------
Define o modelo de dados 'Task', que representa uma tarefa dentro do
sistema de gerenciamento de tarefas da TechFlow Solutions.

Cada tarefa possui:
- id: identificador único (gerado automaticamente)
- title: título curto da tarefa
- description: descrição detalhada
- status: estado atual no fluxo Kanban ("A Fazer", "Em Progresso", "Concluído")
- priority: prioridade da tarefa ("Baixa", "Média", "Alta", "Crítica")
- assignee: pessoa responsável pela tarefa
- due_date: prazo de entrega (formato YYYY-MM-DD), campo adicionado na
  mudança de escopo (ver seção "Gestão de Mudanças" do README.md)
"""

from dataclasses import dataclass, field, asdict
from typing import Optional

VALID_STATUSES = ("A Fazer", "Em Progresso", "Concluído")
VALID_PRIORITIES = ("Baixa", "Média", "Alta", "Crítica")


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: str = "A Fazer"
    priority: str = "Média"
    assignee: Optional[str] = None
    due_date: Optional[str] = None  # Campo incluído na mudança de escopo

    def to_dict(self):
        return asdict(self)

    def validate(self):
        """Valida os campos da tarefa antes de persistir. Lança ValueError
        caso algum dado esteja fora do esperado."""
        if not self.title or not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("O campo 'title' é obrigatório e não pode ser vazio.")
        if self.status not in VALID_STATUSES:
            raise ValueError(
                f"Status inválido: '{self.status}'. Use um de {VALID_STATUSES}."
            )
        if self.priority not in VALID_PRIORITIES:
            raise ValueError(
                f"Prioridade inválida: '{self.priority}'. Use um de {VALID_PRIORITIES}."
            )
        return True
