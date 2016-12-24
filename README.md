## Foss Events (India)


Fossevents focuses on providing all the information about the events which happen in India under FOSS.


[![Join the chat at https://gitter.im/fossevents/fossevents.in](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossevents/fossevents.in)
[![Build Status](https://travis-ci.org/fossevents/fossevents.in.svg?branch=master)](https://travis-ci.org/fossevents/fossevents.in) [![Coverage Status](https://coveralls.io/repos/fossevents/fossevents.in/badge.svg)](https://coveralls.io/r/fossevents/fossevents.in)


Source code for Foss Events India Website (https://beta.fossevents.in)

## Getting Started

Fossevents is developed on Python3(currently python3.5). First check if you have python3 installed using `which python3`. If it does not return anything, please install python3.

The following setup is for fedora 22+

Github setup of the repository:
<pre>
Fork the repository.
git clone git@github.com:<b>YOUR-USERNAME</b>/fossevents.in.git
cd fossevents.in/  //change the directory
git remote add upstream git@github.com:fossevents/fossevents.in.git
Switching of branch
</pre>

Create virtualenv using python3 executable:
```
virtualenv venv -p $(which python3)
. venv/bin/activate
```

The database which we are using is Postgresql, so Postgresql installation and its setup:
```
sudo dnf install postgresql-server postgresql-contrib
sudo systemctl enable postgresql
sudo postgresql-setup --initdb   #initialise database and logs once
sudo systemctl start postgresql
sudo -u postgres psql
postgres=#CREATE USER fossevents WITH PASSWORD 'xxxxxx';
postgres=#ALTER USER fossevents SUPERUSER CREATEDB;
```

Run the command in virtual environment, it will create database:
```
createdb fossevents
```

Install the following for requirements/development.txt installation:
```
sudo dnf  install libxml2-dev libxslt1-dev python-dev  libpq-dev
pip install rcssmin --install-option="--without-c-extensions"
pip install rjsmin --install-option="--without-c-extensions"
pip install django-compressor --upgrade
pip install -r requirements/development.txt
```

For migration, we need to alter some trust auth in pg_hba.conf file:
```
sudo -i
cd var/lib/pgsql/data/
atom pg_hba.conf
Change host of 127.0.0.1/32 and ::1/128 to METHOD "trust"
```

Run the following commands in your virtual environment:
```
python manage.py migrate
python manage.py sample_data
python manage.py runserver
```

Open http://localhost:8000/ (Initial creds: admin / 123123)
