#! /bin/bash
# Build and run the fae-util processor
# 
# Compiles the java source first because it takes a while
# and if the build_and_run_server.sh is ran at the same
# time then this will prevent us from trying to create,
# migrate, or populate simultaneously.

# compile java source for fae-util
cd fae-util
./build

# create database if doesn't already exist
cd ..
python utils/create_db.py

# make sure django migrations are up to date
python manage.py migrate

# make sure database has been populated with seed data
python utils/populate_db.py

# run fae-util processor
cd fae-util
python fae-util.py
