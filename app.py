# o arquivo app.py cria uma instância flask, e utiliza do decorador route
# para chamar a função

# para executar local > flask --app app run
    # acesse com http://127.0.0.1:5000/
# para executar rede  > flask run --host=0.0.0.0

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
