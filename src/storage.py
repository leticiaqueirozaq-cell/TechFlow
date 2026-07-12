"""
storage.py
----------
Camada de persistência simples, em memória, para o sistema de tarefas.

Em um cenário real de produção, esta camada seria substituída por um banco
de dados (ex.: PostgreSQL, SQLite). Para fins didáticos deste projeto,
usamos uma estrutura em memória para manter o exemplo simples e focado
nos conceitos de Engenharia de Software (CRUD, testes, CI/CD).
"""

from typing import Dict, List, Optional
from src.models import Task


class TaskRepository:
    """Repositório responsável pelas operações CRUD sobre as tarefas."""

    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def reset(self):
        """Limpa o repositório. Usado principalmente nos testes automatizados."""
        self._tasks.clear()
        self._next_id = 1

    # ---------- CREATE ----------
    def create(self, title, description="", status="A Fazer",
               priority="Média", assignee=None, due_date=None) -> Task:
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            assignee=assignee,
            due_date=due_date,
        )
        task.validate()
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    # ---------- READ ----------
    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list_all(self, status: Optional[str] = None) -> List[Task]:
        tasks = list(self._tasks.values())
        if status:
            tasks = [t for t in tasks if t.status == status]
        return sorted(tasks, key=lambda t: t.id)

    # ---------- UPDATE ----------
    def update(self, task_id: int, **fields) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        for key, value in fields.items():
            if value is not None and hasattr(task, key):
                setattr(task, key, value)
        task.validate()
        return task

    # ---------- DELETE ----------
    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False


# Instância única (singleton) usada pela aplicação Flask
repository = TaskRepository()
