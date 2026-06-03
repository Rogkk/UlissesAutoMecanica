from flask import Blueprint, render_template

fiscal_bp = Blueprint("fiscal", __name__)

@fiscal_bp.route("/fiscal")
def index():
    return render_template("fiscal/index.html")