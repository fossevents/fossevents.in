## Foss Events (India)


[![Join the chat at https://gitter.im/fossevents/fossevents.in](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossevents/fossevents.in)
[![Build Status](https://travis-ci.org/fossevents/fossevents.in.svg?branch=master)](https://travis-ci.org/fossevents/fossevents.in) [![Coverage Status](https://coveralls.io/repos/fossevents/fossevents.in/badge.svg)](https://coveralls.io/r/fossevents/fossevents.in)


Source code for Foss Events India Website (https://beta.fossevents.in)

## Getting Started

Run the following command in a virtual environment:
```
createdb fossevents
python manage.py migrate
python manage.py sample_data
python manage.py runserver
```

Open http://localhost:8000/ (Initial creds: admin / 123123)
