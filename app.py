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


from teachers.routes import teachers
from students.routes import students

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect(app)



@app.route('/', methods=['GET'])
def home():
    return jsonify({'Datos':'Hola'})

app.register_blueprint(teachers)
app.register_blueprint(students)

if __name__ == '__main__':
    
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)