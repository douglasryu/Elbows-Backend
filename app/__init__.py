from flask import Flask

from app.routes import api
from app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(api.bp)
