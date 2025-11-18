FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Instalacja zależności
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Kopiowanie reszty plików aplikacji
COPY . .

# Otwarcie portu
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "run.py"]
