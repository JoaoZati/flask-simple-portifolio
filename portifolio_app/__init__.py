from flask import Flask

app = Flask(__name__)

from portifolio_app.views.home import home
