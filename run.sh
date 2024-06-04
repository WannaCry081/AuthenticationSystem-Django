#!/usr/bin/bash

if [ ! -d "$(pwd)/venv" ]; then 
    virtualenv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
else
    source venv/Scripts/activate
fi

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

deativate