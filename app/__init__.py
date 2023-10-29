from flask import Flask,render_template
from dotenv import load_dotenv
import config
import os

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__),"..")
dotenv_path = os.path.join(APP_ROOT,".env")
load_dotenv(dotenv_path)

app.config.from_object('config.settings.'+os.environ.get("ENV"))

#handle Error
@app.errorhandler(404)
def error_handle(error):
    return render_template("errors/404.html"),404

#Blueprint
from app.views.home import home as home_template

#Blueprint register
app.register_blueprint(home_template)