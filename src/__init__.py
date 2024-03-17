from flask import Flask

# Routes
from .routes import ExtractRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1 gigabyte

    # Blueprints
    app.register_blueprint(ExtractRoutes.main, url_prefix='/extract')
    return app
