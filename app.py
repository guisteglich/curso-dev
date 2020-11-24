from flask import Flask, render_template  

app = Flask(__name__)


class Cursos:
    def __init__(self, nome, duracao, unidade):
        self.nome = nome
        self.duracao = duracao
        self.unidade = unidade

@app.route("/")
def start():
    return "inicio"

@app.route("/home")
def main():
    si = Cursos("Sistemas de informação", "4 anos", "C3")
    ec = Cursos("Engenharia da computação", "5 anos", "C3")
    ea = Cursos("Engenharia de automação", "5 anos", "C3")

    lista_cursos = [si, ec, ea]
    return render_template("index.html", titulo="Cursos", Cursos=lista_cursos)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')