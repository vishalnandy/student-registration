from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Vishal1nand@@db.tvlobiffdkivwwpyolwi.supabase.co:5432/postgres'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres.tvlobiffdkivwwpyolwi:Vishal1nand%40@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('register.html', students=students)

@app.route('/register', methods=['POST'])
def register():
    new_student = Student(
        name=request.form['name'],
        email=request.form['email'],
        age=int(request.form['age'])
    )
    db.session.add(new_student)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
