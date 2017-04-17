<h2> Setting up Postgres in Ubuntu</h2>

It is highly recommended to use a virtualenv before getting started in any python project to familiarize oneself with pip and virtualenv. Link [http://stackoverflow.com/questions/4483888/what-are-the-benefits-of-pip-and-virtualenv] for more information.

We need to install dependencies for Postgresql first 
     `sudo apt-get install libpq-dev python-dev`
     `sudo apt-get install postgresql postgresql-contrib` 
<br>

After the installation is done run the following command<br>
    `$ sudo service postgresql start` 
    <br>it should display the following result <br>
    _Starting PostgreSQL 9.3 database server_ <br>
    or you can even try to start postgresql by switching on to _postgres_ as a user
    `sudo -i -u postgres`
    That would change the username of the terminal and would read something like : <br>`postgres@system:-$`.<br>

After the installation is done cd to the folder that contains the project
<br>
`path/to/fossevents.in`
`pip install -r requirements.txt`