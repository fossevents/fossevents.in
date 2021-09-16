# This repo has now been archived. Please redirect to [Fossevents.in](https://github.com/afrost-org/fossevents.in)

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

## Postgresql Setup

The database which we are using for production is Postgresql. You can skip this part and jump to `Project Setup` as postgresql does not need to be installed for development.

__NOTE__: Psycopg2 version 2.6.1 has a dependency that requires postgres to be install on system before you can install the library.

Postgresql installation and its setup:
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

For migration, we need to alter some trust auth in pg_hba.conf file:
```
sudo -i
cd var/lib/pgsql/data/
atom pg_hba.conf
Change host of 127.0.0.1/32 and ::1/128 to METHOD "trust"
```

## Project Setup

Install the following for requirements/development.txt installation:
```
sudo dnf  install libxml2-dev libxslt1-dev python-dev  libpq-dev
pip install rcssmin --install-option="--without-c-extensions"
pip install rjsmin --install-option="--without-c-extensions"
pip install django-compressor --upgrade
pip install -r requirements/development.txt
```

Run the following commands in your virtual environment:
```
python manage.py migrate
python manage.py sample_data
python manage.py runserver
```

Open http://localhost:8000/ (Initial creds: admin / 123123)

## Contributors

This is project would have possible with the valuable contributions from these awesome humans.

<table>
  <tr>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/920701?v=3><br>Aniket Maithani (<a href=https://github.com/aniketmaithani>@aniketmaithani</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/499894?v=3><br>Anuvrat Parashar (<a href=https://github.com/bhanuvrat>@bhanuvrat</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/6106465?v=3><br>Durwasa Chakraborty (<a href=https://github.com/durwasa-chakraborty>@durwasa-chakraborty</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/653561?v=3><br>Karambir Singh Nain (<a href=https://github.com/akarambir>@akarambir</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/7566983?v=3><br><a href=https://github.com/Kushagra343>@Kushagra343</a></td>
  </tr>
  <tr>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/1026624?v=3><br>Mayank Jain (<a href=https://github.com/jainmickey>@jainmickey</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/8039608?v=3><br>Sanyam Khurana (<a href=https://github.com/CuriousLearner>@CuriousLearner</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/822770?v=3><br>Satyaakam Goswami (<a href=https://github.com/satyaakam>@satyaakam</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/236356?v=3><br>Saurabh Kumar (<a href=https://github.com/theskumar>@theskumar</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/312622?v=3><br>Shakthi Kannan (<a href=https://github.com/shakthimaan>@shakthimaan</a>)</td>
  </tr>
  <tr>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/13979600?v=3><br>Shweta Suman (<a href=https://github.com/cosmologist10>@cosmologist10</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/3908832?v=3><br>Umang Shukla (<a href=https://github.com/mascot6699>@mascot6699</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/5447064?v=3><br>Vipul (<a href=https://github.com/vipul-sharma20>@vipul-sharma20</a>)</td>
    <td align=center><img width=100 src=https://avatars.githubusercontent.com/u/7746143?v=3><br>Vishal Jain (<a href=https://github.com/jainvishal520>@jainvishal520</a>)</td>
  </tr>
</table>
