import pytest
from app import app as flask_app, tasks  # Import the tasks dictionary

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_task(client):
    # The form data name might differ; adjust 'task_content' as needed
    response = client.post('/', data={'task_content': 'New Task', 'add_task': True})
    assert response.status_code == 200
    assert 'New Task' in tasks.values()

def test_delete_task(client):
    # Add a task first
    client.post('/', data={'task_content': 'Task to Delete', 'add_task': True})
    task_id_to_delete = list(tasks.keys())[0]
    response = client.post('/', data={'task_id_to_delete': task_id_to_delete, 'delete_task': True})
    assert response.status_code == 200
    assert task_id_to_delete not in tasks

