from flask import render_template , Blueprint
from config import Config

bp = Blueprint('home' , __name__ , static_folder='static' , template_folder='home_temps')

@bp.route('/')
def index():
    return render_template('index.html')