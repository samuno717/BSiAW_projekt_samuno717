import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicjalizacja obiektu aplikacji
app = Flask(__name__)

# Konfiguracja pobierana ze zmiennych środowiskowych (z docker-compose)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja bazy danych
db = SQLAlchemy(app)

# Inicjalizacja menedżera logowania
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Nazwa widoku logowania
login_manager.login_message = "Zaloguj się, aby uzyskać dostęp."

# Import tras na końcu, aby uniknąć cyklicznych importów
from app import routes
