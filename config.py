import os

SECRET_KEY = "Alura"

SGBD = "mysql+mysqlconnector"
usuario = "root"
senha = "admin"
servidor = "localhost"
database = "jogoteca"

SQLALCHEMY_DATABASE_URI = f"{SGBD}://{usuario}:{senha}@{servidor}/{database}"

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
