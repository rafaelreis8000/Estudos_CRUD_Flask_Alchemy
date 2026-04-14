from app import db

class Task(db.Model):
    __tablename__ = 'tasks'
    
    taskid = db.Column(db.Integer, primary_key = True, nullable = False)
    description = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'Task nº{self.taskid}: {self.description}'