from flask import Flask, render_template, redirect, url_for
from config import Config
from database import db
from flask_login import LoginManager
from models import User, Station, Booking  # Import models to ensure they are registered

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from routes.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from routes.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from routes.navigation import navigation_bp
    app.register_blueprint(navigation_bp, url_prefix='/navigation')

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()  # Create database tables
        
        # Create default admin if not exists
        if not User.query.filter_by(role='admin').first():
            admin = User(username='admin', email='admin@ev.com', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Create sample stations
            s1 = Station(name='Charger A1', max_power_kw=50.0, location='Gandhipuram')
            s2 = Station(name='Charger B2', max_power_kw=100.0, location='Peelamedu')
            s3 = Station(name='Charger C3', max_power_kw=22.0, location='RS Puram')
            db.session.add_all([s1, s2, s3])
            
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
