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
    admin = db.execute(
        "SELECT id FROM usuarios WHERE email = ?",
        ("admin@cupcakeshop.com",)
    ).fetchone()

    if admin is None:
        db.execute(
            """
            INSERT INTO usuarios
            (nome, email, senha_hash, tipo)
            VALUES (?, ?, ?, 'admin')
            """,
            (
                "Administrador",
                "admin@cupcakeshop.com",
                generate_password_hash("admin123")
            )
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


@app.route("/adicionar-carrinho/<int:produto_id>", methods=["POST"])
def adicionar_carrinho(produto_id):

    if "usuario_id" not in session:
        flash("Faça login para adicionar produtos ao carrinho.")
        return redirect(url_for("login"))

    db = get_db()

    carrinho = db.execute(
        "SELECT id FROM carrinhos WHERE usuario_id = ?",
        (session["usuario_id"],)
    ).fetchone()

    produto = db.execute(
        "SELECT * FROM produtos WHERE id = ? AND disponivel = 1",
        (produto_id,)
    ).fetchone()

    if produto is None:
        flash("Produto indisponível.")
        return redirect(url_for("home"))

    item = db.execute(
        """
        SELECT *
        FROM itens_carrinho
        WHERE carrinho_id = ? AND produto_id = ?
        """,
        (carrinho["id"], produto_id)
    ).fetchone()

    if item:
        db.execute(
            """
            UPDATE itens_carrinho
            SET quantidade = quantidade + 1
            WHERE id = ?
            """,
            (item["id"],)
        )
    else:
        db.execute(
            """
            INSERT INTO itens_carrinho
            (carrinho_id, produto_id, quantidade)
            VALUES (?, ?, 1)
            """,
            (carrinho["id"], produto_id)
        )

    db.commit()

    return redirect(url_for("home"))


@app.route("/carrinho")
def carrinho():

    if "usuario_id" not in session:
        flash("Faça login para acessar o carrinho.")
        return redirect(url_for("login"))

    db = get_db()

    carrinho_usuario = db.execute(
        "SELECT id FROM carrinhos WHERE usuario_id = ?",
        (session["usuario_id"],)
    ).fetchone()

    itens = db.execute(
        """
        SELECT
            itens_carrinho.id,
            itens_carrinho.quantidade,
            produtos.id AS produto_id,
            produtos.nome,
            produtos.preco,
            produtos.imagem,
            (produtos.preco * itens_carrinho.quantidade) AS subtotal
        FROM itens_carrinho
        JOIN produtos
            ON produtos.id = itens_carrinho.produto_id
        WHERE itens_carrinho.carrinho_id = ?
        """,
        (carrinho_usuario["id"],)
    ).fetchall()

    total = sum(item["subtotal"] for item in itens)

    return render_template(
        "carrinho.html",
        itens=itens,
        total=total
    )


@app.route("/carrinho/aumentar/<int:item_id>", methods=["POST"])
def aumentar_item(item_id):

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    db.execute(
        """
        UPDATE itens_carrinho
        SET quantidade = quantidade + 1
        WHERE id = ?
        """,
        (item_id,)
    )

    db.commit()

    return redirect(url_for("carrinho"))


@app.route("/carrinho/diminuir/<int:item_id>", methods=["POST"])
def diminuir_item(item_id):

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    item = db.execute(
        "SELECT quantidade FROM itens_carrinho WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item and item["quantidade"] > 1:
        db.execute(
            """
            UPDATE itens_carrinho
            SET quantidade = quantidade - 1
            WHERE id = ?
            """,
            (item_id,)
        )

        db.commit()

    return redirect(url_for("carrinho"))


@app.route("/carrinho/remover/<int:item_id>", methods=["POST"])
def remover_item(item_id):

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    db.execute(
        "DELETE FROM itens_carrinho WHERE id = ?",
        (item_id,)
    )

    db.commit()

    return redirect(url_for("carrinho"))
    
@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    if "usuario_id" not in session:
        flash("Faça login para continuar.")
        return redirect(url_for("login"))

    db = get_db()

    carrinho_usuario = db.execute(
        "SELECT id FROM carrinhos WHERE usuario_id = ?",
        (session["usuario_id"],)
    ).fetchone()

    itens = db.execute(
        """
        SELECT
            itens_carrinho.produto_id,
            itens_carrinho.quantidade,
            produtos.nome,
            produtos.preco,
            (produtos.preco * itens_carrinho.quantidade) AS subtotal
        FROM itens_carrinho
        JOIN produtos
            ON produtos.id = itens_carrinho.produto_id
        WHERE itens_carrinho.carrinho_id = ?
        """,
        (carrinho_usuario["id"],)
    ).fetchall()

    if not itens:
        flash("Seu carrinho está vazio.")
        return redirect(url_for("carrinho"))

    total = sum(item["subtotal"] for item in itens)

    if request.method == "POST":

        rua = request.form["rua"].strip()
        numero = request.form["numero"].strip()
        complemento = request.form.get("complemento", "").strip()
        bairro = request.form["bairro"].strip()
        cidade = request.form["cidade"].strip()
        cep = request.form["cep"].strip()
        forma_pagamento = request.form["forma_pagamento"]

        if not rua or not numero or not bairro or not cidade or not cep:
            flash("Preencha os dados do endereço.")
            return render_template(
                "checkout.html",
                itens=itens,
                total=total
            )

        cursor_endereco = db.execute(
            """
            INSERT INTO enderecos
            (usuario_id, rua, numero, complemento, bairro, cidade, cep)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session["usuario_id"],
                rua,
                numero,
                complemento,
                bairro,
                cidade,
                cep
            )
        )

        endereco_id = cursor_endereco.lastrowid

        cursor_pedido = db.execute(
            """
            INSERT INTO pedidos
            (usuario_id, endereco_id, valor_total, status)
            VALUES (?, ?, ?, 'Recebido')
            """,
            (
                session["usuario_id"],
                endereco_id,
                total
            )
        )

        pedido_id = cursor_pedido.lastrowid

        for item in itens:
            db.execute(
                """
                INSERT INTO itens_pedido
                (pedido_id, produto_id, quantidade, preco_unitario)
                VALUES (?, ?, ?, ?)
                """,
                (
                    pedido_id,
                    item["produto_id"],
                    item["quantidade"],
                    item["preco"]
                )
            )

        db.execute(
            """
            INSERT INTO pagamentos
            (pedido_id, forma, status)
            VALUES (?, ?, 'Aprovado (simulação)')
            """,
            (
                pedido_id,
                forma_pagamento
            )
        )

        db.execute(
            "DELETE FROM itens_carrinho WHERE carrinho_id = ?",
            (carrinho_usuario["id"],)
        )

        db.commit()

        return redirect(
            url_for("pedido", pedido_id=pedido_id)
        )

    return render_template(
        "checkout.html",
        itens=itens,
        total=total
    )


@app.route("/pedido/<int:pedido_id>")
def pedido(pedido_id):

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    pedido = db.execute(
        """
        SELECT
            pedidos.*,
            enderecos.rua,
            enderecos.numero,
            enderecos.bairro,
            enderecos.cidade,
            enderecos.cep,
            pagamentos.forma AS forma_pagamento,
            pagamentos.status AS status_pagamento
        FROM pedidos
        JOIN enderecos
            ON enderecos.id = pedidos.endereco_id
        JOIN pagamentos
            ON pagamentos.pedido_id = pedidos.id
        WHERE pedidos.id = ?
        AND pedidos.usuario_id = ?
        """,
        (
            pedido_id,
            session["usuario_id"]
        )
    ).fetchone()

    if pedido is None:
        flash("Pedido não encontrado.")
        return redirect(url_for("home"))

    itens = db.execute(
        """
        SELECT
            itens_pedido.quantidade,
            itens_pedido.preco_unitario,
            produtos.nome,
            produtos.imagem
        FROM itens_pedido
        JOIN produtos
            ON produtos.id = itens_pedido.produto_id
        WHERE itens_pedido.pedido_id = ?
        """,
        (pedido_id,)
    ).fetchall()

    return render_template(
        "pedido.html",
        pedido=pedido,
        itens=itens
    )


@app.route("/meus-pedidos")
def meus_pedidos():

    if "usuario_id" not in session:
        flash("Faça login para consultar seus pedidos.")
        return redirect(url_for("login"))

    pedidos = get_db().execute(
        """
        SELECT
            pedidos.id,
            pedidos.data,
            pedidos.valor_total,
            pedidos.status,
            pagamentos.forma AS forma_pagamento
        FROM pedidos
        LEFT JOIN pagamentos
            ON pagamentos.pedido_id = pedidos.id
        WHERE pedidos.usuario_id = ?
        ORDER BY pedidos.id DESC
        """,
        (session["usuario_id"],)
    ).fetchall()

    return render_template(
        "meus_pedidos.html",
        pedidos=pedidos
    )


@app.route("/admin")
def admin():

    if session.get("usuario_tipo") != "admin":
        flash("Acesso restrito ao administrador.")
        return redirect(url_for("home"))

    db = get_db()

    produtos = db.execute(
        "SELECT * FROM produtos ORDER BY id"
    ).fetchall()

    pedidos = db.execute(
        """
        SELECT
            pedidos.id,
            pedidos.data,
            pedidos.valor_total,
            pedidos.status,
            usuarios.nome AS cliente
        FROM pedidos
        JOIN usuarios
            ON usuarios.id = pedidos.usuario_id
        ORDER BY pedidos.id DESC
        """
    ).fetchall()

    return render_template(
        "admin.html",
        produtos=produtos,
        pedidos=pedidos
    )


@app.route("/admin/produto/novo", methods=["POST"])
def admin_novo_produto():

    if session.get("usuario_tipo") != "admin":
        return redirect(url_for("home"))

    nome = request.form["nome"].strip()
    descricao = request.form["descricao"].strip()
    preco = request.form["preco"].replace(",", ".")
    imagem = request.form.get("imagem", "🧁").strip() or "🧁"

    if not nome or not descricao or not preco:
        flash("Preencha os dados do produto.")
        return redirect(url_for("admin"))

    db = get_db()

    db.execute(
        """
        INSERT INTO produtos
        (nome, descricao, preco, imagem, disponivel)
        VALUES (?, ?, ?, ?, 1)
        """,
        (nome, descricao, float(preco), imagem)
    )

    db.commit()

    flash("Produto cadastrado com sucesso.")
    return redirect(url_for("admin"))


@app.route("/admin/produto/<int:produto_id>", methods=["POST"])
def admin_editar_produto(produto_id):

    if session.get("usuario_tipo") != "admin":
        return redirect(url_for("home"))

    nome = request.form["nome"].strip()
    descricao = request.form["descricao"].strip()
    preco = request.form["preco"].replace(",", ".")
    imagem = request.form.get("imagem", "🧁").strip() or "🧁"
    disponivel = 1 if request.form.get("disponivel") else 0

    db = get_db()

    db.execute(
        """
        UPDATE produtos
        SET nome = ?,
            descricao = ?,
            preco = ?,
            imagem = ?,
            disponivel = ?
        WHERE id = ?
        """,
        (
            nome,
            descricao,
            float(preco),
            imagem,
            disponivel,
            produto_id
        )
    )

    db.commit()

    flash("Produto atualizado.")
    return redirect(url_for("admin"))


@app.route("/admin/pedido/<int:pedido_id>/status", methods=["POST"])
def admin_status_pedido(pedido_id):

    if session.get("usuario_tipo") != "admin":
        return redirect(url_for("home"))

    status = request.form["status"]

    status_validos = [
        "Recebido",
        "Em preparo",
        "Saiu para entrega",
        "Entregue"
    ]

    if status not in status_validos:
        flash("Status inválido.")
        return redirect(url_for("admin"))

    db = get_db()

    db.execute(
        """
        UPDATE pedidos
        SET status = ?
        WHERE id = ?
        """,
        (status, pedido_id)
    )

    db.commit()

    flash("Status do pedido atualizado.")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
