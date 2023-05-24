from app import db

# aqui cada class abaixo, é uma tabela que será criada no banco de dados usando o SQLAlchemy.
class User(db.Model):
    __tablename__ = "users" #nome da tabela
    id = db.Column(db.Integer, primary_key=True) #coluna que guardará os IDs, do tipo inteiro, e primary key 
    username= db.Column(db.String, unique=True) #.....
    password = db.Column(db.String)# ....
    name= db.Column(db.String)# ....
    email = db.Column(db.String, unique=True)# ....

    def __init__(self, username, password, name, email):#quando for chamado esse comando, aqui estão os argumentos de inicialização
        self.username = username#init self.username = username (parâmetro)
        self.password = password# ...
        self.name = name #...
        self.email = email #...
    
    def __repr__(self): #o repr. é como o dado será exibido ao chamar a função
        return "<User %r>" % self.username
    #os comentarios acima servem para as partes de baixo, a unica diferença, é que abaixo tem as chaves estrangeiras e joins.

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)#Leitura == variavel id, recebe o retorno da função Column (a qual cria uma coluna na tabela)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', db.ForeignKey('user_id')) #join

    def __init__(self,content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id
    
class Follow(db.Model):
    __tablenames__ = "follow"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys = user_id)