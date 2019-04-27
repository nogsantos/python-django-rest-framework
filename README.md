# Python Django REST framework

## Setup

### Requirement

[Pipenv](https://pipenv.readthedocs.io/en/latest/)

#### Virtualenv

To activate this project's virtualenv

```bash
$ pipenv shell
```

This shell can be deactivated by using `exit`.

#### Dependencies

Install project dependencies

```bash
$ pipenv install
```

#### Installed dependencies.

Get a list of installed dependencies

```bash
$ pipenv run pip freeze
```

#### Dependency graph 

Show a dependency graph of installed dependencies.

```bash
$ pipenv graph
```

#### Checks for vulnerabilities

Checks for security vulnerabilities and asserts that PEP 508 requirements are being met by the current environment.

```bash
$ pipenv check
```

### Migrate

```bash
$ python manage.py migrate
```

### Super user

```bash
$ python manage.py createsuperuser --email [admin@example.com] --username [admin]
```

### Run 

```bash
$ python manage.py runserver
```
