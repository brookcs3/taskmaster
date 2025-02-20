import pytest
from app import app, db, Task
from datetime import datetime, UTC

# Setup a test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# ✅ Test 1: Creating a Task
def test_create_task(client):
    response = client.post('/add', data={'title': 'Test Task'})
    assert response.status_code == 302  # Redirects after adding task

    # Check if task exists in DB
    with app.app_context():
        task = Task.query.filter_by(title='Test Task').first()
        assert task is not None

# ✅ Test 2: Assigning a Task
def test_assign_task(client):
    with app.app_context():
        new_task = Task(title='Unassigned Task')
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id

    response = client.post(f'/assign/{task_id}', data={'assigned_to': 'Cameron'})
    assert response.status_code == 302  # Redirects after assigning

    with app.app_context():
        task = db.session.get(Task, task_id)  # ✅ FIXED
        assert task.assigned_to == 'Cameron'

# ✅ Test 3: Setting a Deadline
def test_set_deadline(client):
    with app.app_context():
        new_task = Task(title='Task with No Deadline')
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id

    response = client.post(f'/deadline/{task_id}', data={'deadline': '2025-02-25'})
    assert response.status_code == 302  # Redirects after setting deadline

    with app.app_context():
        task = db.session.get(Task, task_id)  # ✅ FIXED
        assert task.deadline.strftime('%Y-%m-%d') == '2025-02-25'

# ✅ Test 4: Prevent Blank Task Creation
def test_prevent_blank_task(client):
    response = client.post('/add', data={'title': ''})
    assert response.status_code == 302  # Redirects, but task should not be added

    with app.app_context():
        task = Task.query.filter_by(title='').first()
        assert task is None  # Task should NOT be created
