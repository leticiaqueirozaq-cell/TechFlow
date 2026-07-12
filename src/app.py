"""
app.py
------
API REST do sistema de gerenciamento de tarefas da TechFlow Solutions.

Endpoints disponíveis:
    GET    /api/health              -> Verifica se a API está no ar
    POST   /api/tasks                -> Cria uma nova tarefa
    GET    /api/tasks                -> Lista todas as tarefas (filtro opcional ?status=)
    GET    /api/tasks/<id>           -> Obtém uma tarefa específica
    PUT    /api/tasks/<id>           -> Atualiza uma tarefa (título, status, prioridade, etc.)
    DELETE /api/tasks/<id>           -> Remove uma tarefa
    GET    /api/tasks/report/summary -> Retorna um resumo (quantidade por status/prioridade),
                                         funcionalidade adicionada na mudança de escopo.

Como executar localmente:
    pip install -r requirements.txt
    python -m flask --app src.app run --debug
    # ou: python src/app.py
"""

from flask import Flask, jsonify, request
from src.storage import repository

app = Flask(__name__)


def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


@app.get("/api/health")
def health():
    """Endpoint simples usado para checar se a aplicação está rodando
    (também utilizado pelo pipeline de CI como smoke test)."""
    return jsonify({"status": "ok", "service": "techflow-task-manager"}), 200


@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    try:
        task = repository.create(
            title=data.get("title"),
            description=data.get("description", ""),
            status=data.get("status", "A Fazer"),
            priority=data.get("priority", "Média"),
            assignee=data.get("assignee"),
            due_date=data.get("due_date"),
        )
    except ValueError as exc:
        return error_response(str(exc))
    return jsonify(task.to_dict()), 201


@app.get("/api/tasks")
def list_tasks():
    status_filter = request.args.get("status")
    tasks = repository.list_all(status=status_filter)
    return jsonify([t.to_dict() for t in tasks]), 200


@app.get("/api/tasks/<int:task_id>")
def get_task(task_id):
    task = repository.get(task_id)
    if task is None:
        return error_response("Tarefa não encontrada.", 404)
    return jsonify(task.to_dict()), 200


@app.put("/api/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    try:
        task = repository.update(task_id, **data)
    except ValueError as exc:
        return error_response(str(exc))
    if task is None:
        return error_response("Tarefa não encontrada.", 404)
    return jsonify(task.to_dict()), 200


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    deleted = repository.delete(task_id)
    if not deleted:
        return error_response("Tarefa não encontrada.", 404)
    return "", 204


@app.get("/api/tasks/report/summary")
def summary_report():
    """Funcionalidade adicionada na mudança de escopo (ver README.md,
    seção 'Gestão de Mudanças'): retorna um resumo com a contagem de
    tarefas por status e por prioridade, permitindo à equipe monitorar
    o desempenho do fluxo de trabalho em tempo real."""
    tasks = repository.list_all()
    by_status, by_priority = {}, {}
    for t in tasks:
        by_status[t.status] = by_status.get(t.status, 0) + 1
        by_priority[t.priority] = by_priority.get(t.priority, 0) + 1
    return jsonify({
        "total_tasks": len(tasks),
        "by_status": by_status,
        "by_priority": by_priority,
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
