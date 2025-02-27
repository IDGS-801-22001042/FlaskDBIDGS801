from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms

from models import db
from models import Alumnos

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf= CSRFProtect()

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
          db.create_all()
    app.run(debug=True)