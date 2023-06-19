start pip install django
start pip install huey
start pip install redis
start pip install yoomoney
start redis-server
cd nixie
start python manage.py run_huey
start python manage.py runserver 1111
start http://127.0.0.1:1111/
pause