from app import app
from flask import render_template

@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)
#aqui nao precisa passar o diretório porque por padrão ele vai na pasta templates

@app.route("/login")
def login():
    return render_template('base.html')