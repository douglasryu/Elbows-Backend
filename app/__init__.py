from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from .routes import api, aws
from .models import db
from .config import Configuration

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)

db.init_app(app)
Migrate(app, db)

app.register_blueprint(api.bp)
app.register_blueprint(aws.bp)
