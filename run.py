from app import app, db
import os

if __name__ == '__main__':
    # Tworzenie tabel w bazie danych przy starcie, jeśli nie istnieją
    with app.app_context():
        db.create_all()

    # Uruchomienie serwera (host 0.0.0.0 jest wymagany dla Dockera)
    app.run(host='0.0.0.0', port=5000, debug=True) # nosec B104

    db_password = os.environ.get('DB_PASSWORD', 'local_pass')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_password}@db_host/dbname'
