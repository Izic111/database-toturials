from flask import Flask, render_template
from flask_sqlalchemy import SQLAchemy

app = Flask(__name__)
db = SQLALchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://postgres:12345@localhost:5432/todoapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
id = db.Column (db.Integer, primary_key = True)
description = db.Column (db.String(), nullable= False)
def __repr__ (self):
    return f'< Todo {self.id} {self.description}>'

    db.create_all()

@app.route('/')
def index():
    return render_template ('index.html', data= Todo.query.all())

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=3000)