#!/usr/bin/python

# Create database identified as DATABASE_NAME in fae2/secrets.json
# unless it already exists.  This assumes that DATABASE_USER has
# CREATEDB privileges.


import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
from os.path import join, abspath, dirname

def main():
	with open(join(abspath(dirname(__file__)),'..','fae2','secrets.json')) as f:
		secrets = json.loads(f.read())

	print("\nChecking to see if database '{0}' needs to be created...".format(secrets['DATABASE_NAME']))

	conn_string = "host='{0}' user='{1}' password='{2}' dbname=postgres".format(secrets['DATABASE_HOST'], secrets['DATABASE_USER'], secrets['DATABASE_PASSWORD'])
	# print("Connecting to database: {0}".format(conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = conn.cursor()

	# check to see if database already exists
	cur.execute("select count(*) from pg_database where datname = %s;", [secrets['DATABASE_NAME']])
	result = cur.fetchone()
	if result[0] < 1:
		print("    creating database")
		cur.execute("CREATE DATABASE {0};".format(secrets['DATABASE_NAME']))
	else:
		print("    database already exists")
	print("")

 
if __name__ == "__main__":
	main()
