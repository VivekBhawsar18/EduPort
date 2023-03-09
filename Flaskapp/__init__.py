from flask import Flask
from config import Config
from Flaskapp.extensions import db

app = Flask(__name__)

# App configuration
app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)

# Register blueprints here
from Flaskapp.blueprints.Test.routes import bp as Test_bp
app.register_blueprint(Test_bp , url_prefix='/test')

from Flaskapp.blueprints.home.views import bp as Home_bp
app.register_blueprint(Home_bp)

from Flaskapp.blueprints.authentication.views import bp as Auth_bp
app.register_blueprint(Auth_bp)


# @app.route('/')
# def home():
#         return '<h1>Home page of Flask Application Factory Pattern</h1>'