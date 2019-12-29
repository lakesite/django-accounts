# development #

Extending and developing django-accounts is best done through the included 
example django project.  

## setup ##

Using pipenv:

        $ cd example_project
        $ pipenv install --ignore-pipfile
        (django-accounts) $ python manage.py migrate
        (django-accounts) $ python manage.py createsuperuser
        (django-accounts) $ python manage.py runserver

## using ##

        (django-accounts) $ python manage.py createsuperuser
        (django-accounts) $ python manage.py runserver

The default Django system with accounts app is accessible at:

    http://localhost:8000/

## testing ##

        (django-accounts) $ cd example_project
        (django-accounts) $ python manage.py test
