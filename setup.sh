python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Запуск Redis сервера
redis-server &

cd nixie

python manage.py run_huey &
python manage.py runserver 1111 &

xdg-open http://127.0.0.1:1111/

read -p "Press any key to continue..."