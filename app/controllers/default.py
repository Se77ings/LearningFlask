from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
@app.route("/test/<name>")
def teste(name=None):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, Usuário"