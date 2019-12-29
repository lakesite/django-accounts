# install #

1. Install django-accounts using pipenv:

    $ pipenv install -e git+https://github.com/lakesite/django-accounts#egg=django-emailuser
    $ pipenv install -e git+https://github.com/lakesite/django-accounts#egg=django-accounts

2. Add the app to your settings.py project file:

```
AUTH_USER_MODEL = 'emailuser.EmailUser' # required per standard config

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'emailuser',

    'accounts',
]

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'accounts/login'

```

3. Run migrations:

    $ pipenv shell
    (venv) $ python manage.py migrate

4. Include the accounts URLconf in your project urls.py like this:

    path('accounts/', include('accounts.urls'))