from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

from app.controllers.home import api as home_ns
from app.controllers.product import api as prod_ns
from app.controllers.search import api as search_ns
from app.controllers.category import api as category_ns

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    # db.init_app(app)
    # migrate.init_app(app, db)

    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }

    api = Api(
        app,
        version='0.1',
        title='Buying For Earth Server',
        authorizations=authorizations, 
        security='apikey'
    )

    api.add_namespace(home_ns, '/home')
    api.add_namespace(prod_ns, '/product')
    api.add_namespace(search_ns, '/search')
    api.add_namespace(category_ns, '/category')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)