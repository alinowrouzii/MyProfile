
# Portfolio project

Portfolio project that is written in Django and is fully Dockerized.

### How to run project:

All dependencies should be installed:
```
cd MyProfile
virtualenv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Run on Docker:
```
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up

```

The project should be available at [localhost:8000](http://localhost:8000)
