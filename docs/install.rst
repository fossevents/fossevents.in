Install
=========

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development:
 For apt-get mass install packages from a file::
 
     $ apt-get install $(grep -vE "^\s*#" requirements.apt  | tr "\n" " ")

 Then installing required packages::
 
    $ pip install -r requirements/base.txt
    
    $ pip install -r requirements/development.txt 
    
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the ``runserver_plus`` command::

    $ python manage.py runserver_plus

The base app will run but you'll need to carry out a few steps to make the sign-up and login forms work. These are currently detailed in `issue #39`_.

.. _issue #39: https://github.com/pydanny/cookiecutter-django/issues/39

It's time to write the code!!!

