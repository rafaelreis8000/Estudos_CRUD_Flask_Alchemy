from flask import render_template, request, redirect
from models import Task
from sqlalchemy import func

def register_routes(app, db):

    #cRud. Main route, shows every task
    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks = tasks)

    #Crud. Creates a new task
    @app.route('/create', methods =['GET', 'POST'])
    def create_task():
        description = request.form['description'].strip()

        #input validation. If it's already in the task list, it won't pass
        task_validation = Task.query.filter(func.lower(Task.description) == description.lower()).first()
        if task_validation:
            return f'This task already exists!', 400
        
        new_task = Task(description = description)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    
    #cruD. Delete a chosen task
    @app.route('/delete/<int:task_id>', methods = ['POST'])
    def delete_task(task_id):
        task = Task.query.get(task_id)

        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect('/')
    
    #crUd. Update a task
    @app.route('/update/<int:task_id>', methods = ['POST'])
    def update_task(task_id):
        task = Task.query.get(task_id)

        if task:
            task.description = request.form['description']
            db.session.commit()
        return redirect('/')