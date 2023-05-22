DEBUG = True #vantagem do debug: quando alterar algo no arquivo e salvar, ele reinicia a palicação, sem precisar dar ctrl + c e iniciar novamente.

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True