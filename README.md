Установка для Windows
1) установите виртуальную среду: python -m venv env/myshop
2) активируйте виртуальную среду: .\env\myshop\Scripts\activate
3) установите зависимости: pip install -r requirements.txt
4) создайте начальные миграции: python manage.py makemigrations
5) примените их: python manage.py migrate
