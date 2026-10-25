from flask import Flask, current_app
from app.config import Config
from app.extensions import db
from app.models import User


def seed_admin():
    admin_email = current_app.config['ADMIN_EMAIL']
    admin_password = current_app.config['ADMIN_PASSWORD']

    admin_user = User.query.filter_by(email=admin_email).first()
    if admin_user:
        return # Admin user already exists, no need to create a new one

    admin_user = User(email=admin_email, role= 'admin', username='Admin')
    admin_user.set_password(admin_password)

    db.session.add(admin_user)
    db.session.commit()

def seed_services():

def create_app(class_name=Config):
    app = Flask(__name__)

    app.config.from_object(class_name)
    db.init_app(app)

    from app.models import User

    from app.routes.auth import auth
    from app.routes.views import views
    app.register_blueprint(auth)
    app.register_blueprint(views)

    return app