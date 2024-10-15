#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
fi

echo "Activation de l'environnement virtuel..."
source venv/bin/activate

echo "Installation des dépendances..."
pip install flask
pip install python-dotenv
pip install bootstrap-flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install flask-login
pip install PyYAML

echo "Démarrage de l'application Flask..."
flask run
