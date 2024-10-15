from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = "ccdfd612-8ef7-4db8-acdc-3d8b8ef13efc"
bootstrap = Bootstrap(app)


import os.path


def mkpath(p):
    print()
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)