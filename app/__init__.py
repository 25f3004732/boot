from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'

    @app.route('/')
    def home(): 
        return '<h1>Home Page</h1>'

    from app.routes.auth import auth
    from app.routes.views import view
    app.register_blueprint(auth)
    app.register_blueprint(view)

    return app