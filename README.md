# app
Repositorio del proyecto de Ingenieria de Software Untels 2022-1

Comandos útiles para arrancar el proyecto
pip install django
pip install pillow
pip install psycopg2

crear una base de datos en postgresql llamada "is_db"
colocar en settings.py la contraseña con la que ingresamos al postgresql
Posteriormente, ya podrías ejecutar en el terminal la siguiente linea

python manage.py makemigrations

Y finalmente para ver los resultados en postgresql, ejecuta en el terminal

python manage.py migrate

luego ejecutar python manage.py runserver

para terminar ingresar a http://127.0.0.1:8000/login/?next=/