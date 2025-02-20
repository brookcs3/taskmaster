from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(50), nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))  # ✅ Fixed for timezone awareness

# Create database
with app.app_context():
    db.create_all()

# Homepage - List Tasks
@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

# Create a Task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# Assign a Task
@app.route('/assign/<int:task_id>', methods=['POST'])
def assign_task(task_id):
    task = db.session.get(Task, task_id)  # ✅ Fixed for SQLAlchemy 2.0
    assigned_to = request.form.get('assigned_to')
    if task and assigned_to:
        task.assigned_to = assigned_to
        db.session.commit()
    return redirect(url_for('index'))

# Set a Deadline
@app.route('/deadline/<int:task_id>', methods=['POST'])
def set_deadline(task_id):
    task = db.session.get(Task, task_id)  # ✅ Fixed for SQLAlchemy 2.0
    deadline = request.form.get('deadline')
    if task and deadline:
        task.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        db.session.commit()
    return redirect(url_for('index'))

# Delete a Task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = db.session.get(Task, task_id)  # ✅ Fixed for SQLAlchemy 2.0
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

# Run App
if __name__ == '__main__':
    app.run(debug=True)
