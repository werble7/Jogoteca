import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class FormularioJogo(FlaskForm):
    nome = StringField("Nome do Jogo", [validators.data_required(), validators.length(min=1, max=50)])
    categoria = StringField("Nome da Categoria", [validators.data_required(), validators.length(min=1, max=40)])
    console = StringField("Nome do Console", [validators.data_required(), validators.length(min=1, max=20)])
    salvar = SubmitField("Salvar")


class FormularioLogin(FlaskForm):
    nickname = StringField("Nome de usuário", [validators.data_required(), validators.length(min=1, max=8)])
    senha = PasswordField("Senha", [validators.data_required(), validators.length(min=1, max=100)])
    login = SubmitField("Login")


def recuperar_imagem(id):
    for nome_arquivo in os.listdir(app.config["UPLOAD_PATH"]):
        if f"capa{id}" in nome_arquivo:
            return nome_arquivo

    return "capa_padrao.jpg"


def deletar_arquivo(id):
    arquivo = recuperar_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
