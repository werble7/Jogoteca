from jogoteca import app
from flask import request, render_template, redirect, session, flash, url_for
from helpers import FormularioLogin
from models import Usuarios
from flask_bcrypt import check_password_hash


@app.route("/login")
def login():
    form = FormularioLogin(request.form)
    proxima = request.args.get("proxima")
    return render_template("login.html", proxima=proxima, form=form)


@app.route("/autenticar", methods=["POST", ])
def autenticar():
    form = FormularioLogin(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario:
        if senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash("Senha incorreta")
            return redirect(url_for("login"))
    else:
        flash("Usuario não logado")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for("index"))
