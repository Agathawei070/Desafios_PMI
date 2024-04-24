from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/portifolio")
def portifolio():
    return render_template ("portifolio.html")

@app.route("/contatos")
def contatos():
    return render_template ("contatos.html")

@app.route("/curriculo")
def curriculo():
    return render_template ("curriculo.html")