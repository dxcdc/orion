from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
@auth_bp.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # Busca o usuário no banco de dados PostgreSQL / SQLite
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session["user"] = user.username
            session["user_id"] = user.id
            session["role"] = user.role
            flash(f"Bem-vindo de volta, {user.username}! Sessão iniciada com sucesso.", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Credenciais inválidas. Verifique seu usuário e senha.", "error")
            return render_template("login.html")

    if session.get("user"):
        return redirect(url_for("main.dashboard"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Sessão encerrada com sucesso.", "info")
    return redirect(url_for("main.landing"))
