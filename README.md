# Django task

## Description

Django plays a big role in abstracting away the need to deal with database management. However, this means as developers we have to make good choices about what structures and data our models contain and how they are related to enable the ORM to work most efficiently.

In our research software we have task objects that a user has to complete, each task has a title, an order field, a description and a type (such as survey, discussion, diary). We group tasks together in a container which we call a tile. Each tile has a launch date and a status. The status can be either live, pending or archived. A tile can be made up of one or many tasks. A task can only belong to a single tile.

Therefore, this exercise is to create a Django 2.x project that contains task and tile models, configured as outlined above. We would also like you to create a simple API to allow interaction with these models with DRF (Django Rest Framework version 3.10), using the appropriate viewsets and serialisers provided by DRF. No frontend work is required for this task.

## Planning

![Entity_relationship Diagram](https://github.com/sandyMax974/django_task/blob/main/documents/Screenshot%202021-06-18%20at%2012.31.44.png)

## How to run

### Prerequisites

1. Clone this repository: `git clone git@github.com:sandyMax974/django_task.git`
2. `cd` into `django_task` directory
4. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) (optional)
5. Dowload Python 3.7.10: `pyenv install 3.7.10`
6. Create a new virtualenv called `django_test`: `pyenv virtualenv 3.7.10 django_test`
7. Activate virtualenv `pyenv activate django_test`
9. Run dependancy install: `pip install -r requirements.txt`

### Run server
1. `cd` into `src` folder
2. Run `python manage.py runserver`

We will be using the default database provided by Django 2.0.7 (SQLite3)

## Usage

**Available routes**
* http://127.0.0.1:8000/admin/ # django admin console
* http://127.0.0.1:8000/api/tiles # tiles app endpoints
* http://127.0.0.1:8000/api/tasks # tasks app endpoints
