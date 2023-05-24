from app import app, db
from flask import render_template
from app.models.forms import LoginForm

@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)
#aqui nao precisa passar o diretório porque por padrão ele vai na pasta templates

@app.route("/login", methods=["GET", "POST"])
def login():
    form= LoginForm()
    if form.validate():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)



@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = db.User("juliarizza", "1234", "Julia Rizza", "julia.rizza@gmail.com")
    db.session.add(i)
    db.session.commit()