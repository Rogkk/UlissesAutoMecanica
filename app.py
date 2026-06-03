# o arquivo app.py cria uma instância flask, e utiliza do decorador route
# para chamar a função home

# puxa os blueprints

# para executar local > flask --app app run
    # acesse com http://127.0.0.1:5000/
# para executar rede  > flask run --host=0.0.0.0

from flask import Flask, render_template
from routes.dashboard import dashboard_bp
from routes.fiscal import fiscal_bp

app = Flask(__name__)

app.register_blueprint(dashboard_bp)
app.register_blueprint(fiscal_bp)

@app.route("/")
def home():
    return render_template("dashboard/index.html")