# example-app
Powered by Django, Django Rest Framework, Swagger and all other usefull libs and packages

## Installation
### 1. virtualenvwrapper way
```sh
pip install -r requirements.txt
python src/manage.py runserver
```

### 2. Docker-compose way.
```sh
docker-compose build
docker-compose up
```

## Initial data
### 1. virtualenvwrapper way
```sh
python src/manage.py migrate
python src/manage.py make_initial_data
```

### 2. Docker-compose way.
```sh
docker-compose run mycity python src/manage.py migrate
docker-compose run mycity python src/manage.py make_initial_data
```