#! /bin/bash
# Build and run the django webapp


# create database if doesn't already exist
python utils/create_db.py

# make sure django migrations are up to date
python manage.py migrate

# make sure database has been populated with seed data
python utils/populate_db.py

# run django webapp
python manage.py runserver 0.0.0.0:8000
