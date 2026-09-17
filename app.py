from flask import Flask, render_template, g
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

    quantidade = db.execute("SELECT COUNT(*) FROM produtos").fetchone()[0]
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
            """INSERT INTO produtos
               (nome, descricao, preco, imagem, disponivel)
               VALUES (?, ?, ?, ?, ?)""",
            produtos,
        )
    db.commit()
    db.close()

@app.route("/")
def home():
    produtos = get_db().execute(
        "SELECT * FROM produtos WHERE disponivel = 1 ORDER BY id"
    ).fetchall()
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
