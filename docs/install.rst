Install
=========

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

Install all the apt packages from requirements.apt file.
You can use the following command for debian based systems::

    $ sudo apt-get install $(grep -vE "^\s*#" requirements.apt  | tr "\n" " ")

First make sure to create and activate a virtualenv_

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

And now install the requirements from requirements/development.txt::

    $ pip install -r requirements/development.txt

Now change user to postgres::

    $ su - postgres

Login to psql to create database by::

    $ psql

Create a database named 'fossevents' by logging in your postgres server

    $ create database fossevents

Create a role for your database:

    $ create role fossevents with login encrypted password 'password' createdb;

Here quoted password is the password you want for the database

Now make a .env file in the root directory. You can check about python-dotenv_

.. _python-dotenv: https://github.com/theskumar/python-dotenv

In the .env file put the settings for your database configuration as:

`DATABASE_URL="postgres://fossevents:password@localhost/fossevents"`

Here, fossevents is the db name
password is the password you set for the db

Now migrate your changes for the database by::

    $ python manage.py migrate

Now run the server with this command::

    $ python manage.py runserver_plus

Your server is up and running on http://127.0.0.1:8000/

It's time to write code :)