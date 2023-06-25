#!/bin/sh

until cd /app/digitalsys_loan
do
    echo "Loading server volume..."
done

# Rodando as migrations
until python manage.py makemigrations
do
    echo "Making migrations..."
    sleep 2
done
until python manage.py migrate
do
    echo "Applying migrations..."
    sleep 2
done

python manage.py collectstatic --noinput

# Criando o superuser para o django admin
python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL

# Rodando o server. Para um ambiente de produção
# seria mais interessante usar o gunicorn e/ou daphne
python manage.py runserver 0.0.0.0:8000

