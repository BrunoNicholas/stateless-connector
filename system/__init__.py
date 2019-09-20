from flask import Flask

from .routes.router import sys_app

app = Flask(__name__)

# register a blueprint for the version
# with the API standard
app.register_blueprint(sys_app, url_prefix="/api/v1")
