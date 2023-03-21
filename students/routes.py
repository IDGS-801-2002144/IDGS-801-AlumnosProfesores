from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from db.queris import *
from pprint import pprint
from datetime import datetime
from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from db.config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from db.models import db
from db.models import Student


from students import forms


students = Blueprint('students', __name__, template_folder='templates')

@students.route('/get_students', methods=['GET', 'POST'])
def get_students():
    create_form = forms.UserForm(request.form)
    students = Student.query.all()
    pprint(students)

    if request.method == 'POST':
        id = create_form.id.data 
        if not id:
            students = Student.query.all()
        else:
            students = Student.query.filter_by(id=id).all()

    return render_template("students.html", form=create_form, students=students)

@students.route('/insert_students', methods=['GET', 'POST'])
def insert_students():
    create_form = forms.UserForm(request.form)
    insert_students = None
    if request.method == 'POST' and create_form.validate():
        # Crear una nueva instancia del objeto Student con los datos del formulario
        new_student = Student(name=create_form.name.data, surname=create_form.surname.data,
                              email=create_form.email.data, created_at=datetime.now())
        # Agregar la nueva instancia a la sesión y guardar los cambios
        db.session.add(new_student)
        db.session.commit()
        insert_students = "Student added successfully"
    return render_template("insert_students.html", form=create_form, insert_students=insert_students)

@students.route('/update_students', methods=['GET', 'POST'])
def update_students():
    create_form = forms.UserForm(request.form)
    update_students = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        student = Student.query.get(id)
        create_form.id.data = id
        create_form.name.data = student.name
        create_form.surname.data =student.surname
        create_form.email.data = student.email
        
    if request.method=='POST':
        id = create_form.id.data 
        name = create_form.name.data
        surname = create_form.surname.data
        email = create_form.email.data
        student = Student.query.get(id)
        student.name = name
        student.surname = surname
        student.email = email
        db.session.commit()
        update_students = "Los datos del estudiante han sido actualizados exitosamente."
    return render_template("update_students.html", form=create_form, update_students=update_students)


@students.route('/delete_students', methods=['GET', 'POST'])
def delete_students():
    create_form = forms.UserForm(request.form)
    delete_students = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        student = Student.query.get(id)
        create_form.id.data = id
        create_form.name.data = student.name
        create_form.surname.data = student.surname
        create_form.email.data = student.email
        
    if request.method=='POST':
        id = create_form.id.data 
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        delete_students = "El estudiante ha sido eliminado exitosamente."
    return render_template("delete_students.html", form=create_form, delete_students=delete_students)

