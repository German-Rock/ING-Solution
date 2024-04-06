from flask import Flask

<<<<<<< Updated upstream:app/app.py
app = Flask("ceva aplicatie")
=======
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
>>>>>>> Stashed changes:app.py

if __name__ == '__main__':
    app.run(debug=True)
    
