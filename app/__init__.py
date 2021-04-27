from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

from app.controllers.hello import api as hello_ns
from app.controllers.home import api as home_ns
from app.controllers.product import api as prod_ns

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

    api = Api(
        app,
        version='0.1',
        title='Buying For Earth Server'
    )

    api.add_namespace(hello_ns, '/hello')
    api.add_namespace(home_ns, '/home')
    api.add_namespace(prod_ns, '/product')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)