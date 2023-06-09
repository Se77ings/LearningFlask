from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db) #responsavel pelas migrações

manager = Manager(app) #responsavel pelos comandos para inciaizar a aplicação, por padrao, o run server
manager.add_command('db', MigrateCommand) #adicionamos o comando DB,e o MigrateCommand passa os comandos necessarios

from app.controllers import default
from app.models import tables
