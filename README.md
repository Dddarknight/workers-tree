# Workers-tree
The app provides oppotunities:
- to show the full hierarchical tree of company's employees,

| ![Django](workers_tree/examples/django_example.png "Django example") |  ![JS](workers_tree/examples/js_tree_example.png "js-tree example") |

- to see all the information about employees for the registered users with filtering.
User profile also includes the user's /the employee's photos.

### CodeClimate and CI status
<a href="https://codeclimate.com/github/Dddarknight/workers-tree/maintainability"><img src="https://api.codeclimate.com/v1/badges/9b8bd7b1fdc3d62a0ca7/maintainability" /></a> <a href="https://codeclimate.com/github/Dddarknight/workers-tree/test_coverage"><img src="https://api.codeclimate.com/v1/badges/9b8bd7b1fdc3d62a0ca7/test_coverage" /></a> [![Python CI](https://github.com/Dddarknight/workers-tree/actions/workflows/pyci.yml/badge.svg)](https://github.com/Dddarknight/workers-tree/actions)

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [Django ](https://www.djangoproject.com/) |  "A high-level Python web framework" |
| [PostgreSQL](https://www.postgresql.org/) |  "An open source object-relational database system" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |
| [Py.Test](https://pytest.org) | "A mature full-featured Python testing tool" |
| [django-seed](https://pypi.org/project/django-seed/) | "Uses the faker library to generate test data for your Django models" |
| [django-filter](https://django-filter.readthedocs.io/en/stable/) | "Allows to filter down a queryset based on a model’s fields" |
| [django-tables2](https://django-tables2.readthedocs.io/en/latest/) | "Support for automatic table generation based on a Django model" |
| [jsTree](https://www.jstree.com/) | "Jquery plugin" |

## Installation for contributors
```
$ git clone git@github.com:Dddarknight/workers-tree.git
$ cd workers-tree
$ pip install poetry
$ make install
$ touch .env

You have to write into .env file SECRET_KEY for Django app. See .env.example.
To get SECRET_KEY for Django app:
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()

Then add new SECRET_KEY to .env file

$ make migrate
$ make run
```