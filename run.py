from app import app, db

if __name__ == '__main__':
    # Tworzenie tabel w bazie danych przy starcie, jeśli nie istnieją
    with app.app_context():
        db.create_all()

    # Uruchomienie serwera (host 0.0.0.0 jest wymagany dla Dockera)
    app.run(host='0.0.0.0', port=5000, debug=True) # nosec B104
