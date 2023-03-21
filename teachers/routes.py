from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from db.queris import *
from pprint import pprint
from datetime import datetime


from teachers import forms


teachers = Blueprint('teachers', __name__, template_folder='templates')

@teachers.route('/get_teachers', methods=['GET', 'POST'])
def get_teachers():
    create_form = forms.UserForm(request.form)
    teachers = search_all_teachers()
    pprint(teachers)

    if request.method == 'POST':
        id = create_form.id.data 
        if not id:  # Si el formulario está vacío, devuelve todos los profesores
            teachers = search_all_teachers()
        else:
            teachers = search_teachers_(id)

    return render_template("teachers.html", form=create_form, teachers=teachers)


@teachers.route('/insert_teachers', methods=['GET', 'POST'])
def insert_teachers():
    create_form = forms.UserForm(request.form)
    name = create_form.name.data
    surname = create_form.surname.data
    email = create_form.email.data
    insert_teachers = None
    if request.method=='POST':
        insert_teacher(name, surname, email, datetime.now())
    return render_template("insert_teachers.html", form=create_form, insert_teachers=insert_teachers)


@teachers.route('/update_teachers', methods=['GET', 'POST'])
def update_teachers():
    
    create_form = forms.UserForm(request.form)
    update_teachers = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        teacher=search_teachers_(id)
        create_form.id.data = id
        create_form.name.data = teacher[0]['name']
        create_form.surname.data =teacher[0]['surname']
        create_form.email.data = teacher[0]['email']
        
    if request.method=='POST':
        id = create_form.id.data 
        name = create_form.name.data
        surname = create_form.surname.data
        email = create_form.email.data
        update_teacher(id, name, surname, email)
    return render_template("update_teachers.html", form=create_form, update_teachers=update_teachers)

@teachers.route('/delete_teachers', methods=['GET', 'POST'])
def delete_teachers():
    
    create_form = forms.UserForm(request.form)
    delete_teachers = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        teacher=search_teachers_(id)
        create_form.id.data = id
        create_form.name.data = teacher[0]['name']
        create_form.surname.data =teacher[0]['surname']
        create_form.email.data = teacher[0]['email']
        
    if request.method=='POST':
        id = create_form.id.data 
        delete_teacher(id)
    return render_template("delete_teachers.html", form=create_form, update_teachers=delete_teachers)



