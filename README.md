# django-accounts #

Standard django.contrib.auth account app.

## motivation ##

Most Django projects will require user authentication views.  We want an easy,
standard app which handles the login, logout, forgot password, account
registration and confirmation process. 

* django-accounts uses [django-emailsuer](https://github.com/lakesite/django-emailuser)
* django-accounts uses an email and password field.
* django-accounts handles login, logout, forgot password, account registration,
and confirmation via django.contrib.auth.
* django-accounts uses bootstrap 4

* Area of focus:
  - All django projects which require login/auth templates.
  - Django apps.

Further [rationale](docs/rationale.md) provided.

## install ##

For installation, please see [install](docs/install.md)

## development ##

To run locally and develop, see [development.md](docs/development.md)

## contributing ##

Please review [standards](docs/standards.md) before submitting issues and pull requests.  Thank you in advance for feedback, criticism, and feature requests.

## example ##

A full example is provided [here](example_project)

## license ##

MIT - See [LICENSE.md](LICENSE.md)
