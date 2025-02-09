from user_manager.app import create_app
from user_manager.models import db

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)