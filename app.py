from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        cep = request.form["cep"]

        url = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url)

        dados = resposta.json()

        return render_template("index.html", dados=dados)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)