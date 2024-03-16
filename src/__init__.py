from flask import Flask

# Routes
from .routes import ExtractRoutes, IndexRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(ExtractRoutes.main, url_prefix='/extract')
    return app
