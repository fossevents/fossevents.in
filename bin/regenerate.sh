echo "--> Generate Database"
dropdb fossevents
createdb fossevents

echo "--> Generate database"
python manage.py migrate
python manage.py sample_data
