from flask import Flask

# Routes
from .routes import ExtractRoutes
from .routes import ViewRoutes
from flask_cors import CORS

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1 gigabyte
    app.config['CORS_HEADERS'] = 'Content-Type'
    # Blueprints
    CORS(app)
    app.register_blueprint(ExtractRoutes.main)
    app.register_blueprint(ViewRoutes.main)
    return app
