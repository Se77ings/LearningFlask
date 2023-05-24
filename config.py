import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True #vantagem do debug: quando alterar algo no arquivo e salvar, ele reinicia a palicação, sem precisar dar ctrl + c e iniciar novamente.

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'Secret_Name_passwd'