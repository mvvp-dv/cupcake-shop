from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "cupcake_shop.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "cupcake-shop-pit-ii"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("PRAGMA foreign_keys = ON")

    with open(BASE_DIR / "schema.sql", "r", encoding="utf-8") as f:
        db.executescript(f.read())

    quantidade = db.execute(
        "SELECT COUNT(*) FROM produtos"
    ).fetchone()[0]

    if quantidade == 0:
        produtos = [
            ("Chocolate Clássico", "Massa de chocolate com cobertura cremosa.", 9.90, "🧁", 1),
            ("Morango", "Massa leve com cobertura sabor morango.", 10.90, "🍓", 1),
            ("Baunilha", "Cupcake de baunilha com cobertura cremosa.", 8.90, "🧁", 1),
            ("Red Velvet", "Massa red velvet com cobertura suave.", 11.90, "❤️", 1),
            ("Doce de Leite", "Cupcake recheado e finalizado com doce de leite.", 10.90, "🧁", 1),
            ("Limão", "Massa macia com cobertura cítrica de limão.", 9.90, "🍋", 1),
        ]

        db.executemany(
            """
            INSERT INTO produtos
            (nome, descricao, preco, imagem, disponivel)
            VALUES (?, ?, ?, ?, ?)
            """,
            produtos
        )

    db.commit()
    db.close()


@app.route("/")
def home():
    produtos = get_db().execute(
        "SELECT * FROM produtos WHERE disponivel = 1 ORDER BY id"
    ).fetchall()

    return render_template(
        "index.html",
        produtos=produtos
    )


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        if not nome or not email or not senha:
            flash("Preencha todos os campos.")
            return render_template("cadastro.html")

        db = get_db()

        usuario_existente = db.execute(
            "SELECT id FROM usuarios WHERE email = ?",
            (email,)
        ).fetchone()

        if usuario_existente:
            flash("Este e-mail já está cadastrado.")
            return render_template("cadastro.html")

        senha_hash = generate_password_hash(senha)

        cursor = db.execute(
            """
            INSERT INTO usuarios
            (nome, email, senha_hash, tipo)
            VALUES (?, ?, ?, 'cliente')
            """,
            (nome, email, senha_hash)
        )

        usuario_id = cursor.lastrowid

        db.execute(
            "INSERT INTO carrinhos (usuario_id) VALUES (?)",
            (usuario_id,)
        )

        db.commit()

        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        usuario = get_db().execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,)
        ).fetchone()

        if usuario is None or not check_password_hash(
            usuario["senha_hash"],
            senha
        ):
            flash("E-mail ou senha incorretos.")
            return render_template("login.html")

        session.clear()
        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        session["usuario_tipo"] = usuario["tipo"]

        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
