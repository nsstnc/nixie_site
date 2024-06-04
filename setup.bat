@echo off

python -m venv venv

call venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

start redis\redis-server

cd nixie
start python manage.py run_huey
start python manage.py runserver 1111
start http://127.0.0.1:1111/
pause


