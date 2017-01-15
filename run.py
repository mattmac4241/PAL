import os

from dotenv import load_dotenv

from app.database import db
from app.user.views import users_blueprint
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('app/config.py')
    db.init_app(app)
    app.register_blueprint(users_blueprint)
    return app


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    load_dotenv(dotenv_path)
    app = create_app()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
