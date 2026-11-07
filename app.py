from pathlib import Path
import sqlite3

from flask import Flask, render_template_string, make_response

app = Flask(__name__)

DB_PATH = Path(__file__).with_name("visits.db")


@app.route("/")
def home():
    # Avaa SQLite-tietokanta.
    conn = sqlite3.connect(DB_PATH)

    try:
        # Luo tietokantataulu, jos sitä ei vielä ole.
        conn.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY,
                count INTEGER NOT NULL
            )
        """)

        # Aloita laskuri nollasta vain ensimmäisellä kerralla.
        conn.execute(
            "INSERT OR IGNORE INTO visits (id, count) VALUES (1, 0)"
        )

        # Lisää yksi käynti.
        conn.execute(
            "UPDATE visits SET count = count + 1 WHERE id = 1"
        )

        # Hae uusi käyntimäärä.
        visits = conn.execute(
            "SELECT count FROM visits WHERE id = 1"
        ).fetchone()[0]

        conn.commit()

    finally:
        conn.close()

    html = """
    <!DOCTYPE html>
    <html lang="fi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Minun Python-palvelimeni – Viikko 2</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eaf4ff;
                color: #243447;
                text-align: center;
                padding: 50px 20px;
            }
            .box {
                background: white;
                max-width: 650px;
                margin: auto;
                padding: 35px;
                border-radius: 18px;
                box-shadow: 0 4px 15px #ccd9e6;
            }
            h1 { color: #1769aa; }
            .counter {
                font-size: 55px;
                color: #16834a;
                font-weight: bold;
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🐍 Minun Python-verkkosovellukseni</h1>
            <h2>Viikkotehtävä 2</h2>

            <p>Tervetuloa omalle Linux-palvelimelleni!</p>

            <h3>Sivun latauskerrat:</h3>
            <div class="counter">{{ visits }}</div>

            <p>Päivitä sivu, niin laskuri kasvaa yhdellä.</p>

            <hr>

            <h3>Miten tämä toimii?</h3>
            <p>Verkkosovellus on tehty Pythonilla ja Flaskilla.</p>
            <p>Nginx välittää pyynnöt Python-sovellukselle.</p>
            <p>Kävijälaskuri tallennetaan SQLite-tietokantaan
            nimeltä <strong>visits.db</strong>.</p>
            <p>Tietokannan avulla laskurin arvo säilyy
            myös palvelimen uudelleenkäynnistyksen jälkeen.</p>

            <hr>
            <h3>GitHub</h3>
            <p><a href="https://github.com/Mohamed196-wq/viikko2-python-kavijalaskuri">
            View my Python source code on GitHub</a></p>

            <h3>Restart test</h3>
            <p>The Python service was active after reconnecting to
            the server. The SQLite database still contained
            the previous visitor count of 3.</p>
        </div>
    </body>
    </html>
    """

    response = make_response(render_template_string(html, visits=visits))
    response.headers["Cache-Control"] = "no-store"
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

