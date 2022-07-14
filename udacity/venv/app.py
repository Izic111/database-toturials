from pydoc import describe
from flask import Flask,jsonify, redirect, render_template, request, url_for
from flask import jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
db = SQLAlchemy(app)

class todo(db.Model):
        _tablename_ ='todo'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:12345@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
id=db.Column(db.Integer, Primary_Key=True)
description =db.column(db.String(), nullable=False)
def __repr__(self):
                return f' <todo {self.id} {self.description}>'

db.create_all()
@app.route('/')
def index():
        return render_template ('index.html', data= todo.query.all())

        if __name__ == '__main__':
            app.run(host="0.0.0.0", port=3000)

