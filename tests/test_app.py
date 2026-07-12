"""
test_app.py
-----------
Suíte de testes automatizados do sistema de gerenciamento de tarefas.

Cobre:
- Criação, listagem, leitura, atualização e remoção de tarefas (CRUD).
- Validação de entradas inválidas (título vazio, status/prioridade inválidos).
- Endpoint de resumo (funcionalidade da mudança de escopo).

Executar com:
    pytest -v
"""

import pytest
from src.app import app
from src.storage import repository


@pytest.fixture
def client():
    """Cria um cliente de testes Flask e garante um repositório limpo
    antes de cada teste, para que os testes sejam independentes entre si."""
    app.config["TESTING"] = True
    repository.reset()
    with app.test_client() as test_client:
        yield test_client
    repository.reset()


# ---------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------
def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


# ---------------------------------------------------------------------
# CREATE
# ---------------------------------------------------------------------
def test_create_task_success(client):
    payload = {
        "title": "Configurar pipeline de CI",
        "description": "Criar workflow do GitHub Actions",
        "priority": "Alta",
        "assignee": "Ana Silva",
    }
    response = client.post("/api/tasks", json=payload)
    body = response.get_json()

    assert response.status_code == 201
    assert body["title"] == payload["title"]
    assert body["status"] == "A Fazer"  # valor padrão
    assert body["priority"] == "Alta"
    assert body["id"] == 1


def test_create_task_without_title_fails(client):
    response = client.post("/api/tasks", json={"description": "Sem título"})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_create_task_with_invalid_priority_fails(client):
    response = client.post(
        "/api/tasks", json={"title": "Tarefa X", "priority": "Urgentíssima"}
    )
    assert response.status_code == 400


# ---------------------------------------------------------------------
# READ
# ---------------------------------------------------------------------
def test_list_tasks_empty(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_list_tasks_after_creation(client):
    client.post("/api/tasks", json={"title": "Tarefa 1"})
    client.post("/api/tasks", json={"title": "Tarefa 2"})
    response = client.get("/api/tasks")
    body = response.get_json()
    assert response.status_code == 200
    assert len(body) == 2


def test_get_task_not_found(client):
    response = client.get("/api/tasks/999")
    assert response.status_code == 404


def test_filter_tasks_by_status(client):
    client.post("/api/tasks", json={"title": "T1", "status": "A Fazer"})
    client.post("/api/tasks", json={"title": "T2", "status": "Em Progresso"})
    response = client.get("/api/tasks?status=Em Progresso")
    body = response.get_json()
    assert len(body) == 1
    assert body[0]["title"] == "T2"


# ---------------------------------------------------------------------
# UPDATE
# ---------------------------------------------------------------------
def test_update_task_status(client):
    create_resp = client.post("/api/tasks", json={"title": "Implementar CRUD"})
    task_id = create_resp.get_json()["id"]

    update_resp = client.put(
        f"/api/tasks/{task_id}", json={"status": "Em Progresso"}
    )
    assert update_resp.status_code == 200
    assert update_resp.get_json()["status"] == "Em Progresso"


def test_update_nonexistent_task(client):
    response = client.put("/api/tasks/999", json={"status": "Concluído"})
    assert response.status_code == 404


# ---------------------------------------------------------------------
# DELETE
# ---------------------------------------------------------------------
def test_delete_task(client):
    create_resp = client.post("/api/tasks", json={"title": "Tarefa a remover"})
    task_id = create_resp.get_json()["id"]

    delete_resp = client.delete(f"/api/tasks/{task_id}")
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/api/tasks/{task_id}")
    assert get_resp.status_code == 404


def test_delete_nonexistent_task(client):
    response = client.delete("/api/tasks/999")
    assert response.status_code == 404


# ---------------------------------------------------------------------
# Endpoint de resumo (mudança de escopo)
# ---------------------------------------------------------------------
def test_summary_report(client):
    client.post("/api/tasks", json={"title": "T1", "status": "A Fazer", "priority": "Alta"})
    client.post("/api/tasks", json={"title": "T2", "status": "Concluído", "priority": "Alta"})
    client.post("/api/tasks", json={"title": "T3", "status": "Concluído", "priority": "Baixa"})

    response = client.get("/api/tasks/report/summary")
    body = response.get_json()

    assert response.status_code == 200
    assert body["total_tasks"] == 3
    assert body["by_status"]["Concluído"] == 2
    assert body["by_priority"]["Alta"] == 2
