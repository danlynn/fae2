# How to setup and run fae2 for development

The fae2 project is a really nice python django webapp for examining the accessibility compliance of websites.  This repo is designed to quickly setup and run the fae2 webapp via docker containers.

It consists of 3 containers:

+ **database** - runs the postgres db and contains the data
+ **server** - runs the python django app
+ **processor** - runs a worker app that processes the submitted URLs

The database container runs the postgres db on the default port (5432).  It exposes the 5432 port to the host OS where you can access the database using the default 'postgres' user and 'password' password.

The server container runs a script on startup that will make sure that the 'fae2' db is created, run any migrations, and populate the db with seed data if it does not already exist (all the accessibility rules, etc).  It then launches the django webapp.

The processor container similarly runs a script on startup that will make sure that the 'fae2' db is created, run any migrations, and populate the db with seed data.  Additionally, it will make sure that the fae-util java app is built.  It then launches the fae-util.py processor.

The 'fae2' directory in the project directory where you cloned this project is mapped by the server and processor containers to their internal '/usr/src/app' dir.  Thus, any source code changes or compiled artifacts are immediately accessible both inside and outside the docker environment.  Therefore, you can user your laptop's code editor and perform all development locally on your laptop and the changes will be picked up by the docker containers and any changes will automatically be re-compiled by the django server for immediate interactive development - just as if the server was running on your laptop's host OS instead of inside a docker container.

The 'data' directory in the project directory is mapped by the processor container to its internal '/usr/src/data' dir.  Any processing config and data files are placed there and accessible to your host OS if needed.

## Installation and Setup

1. Clone this project
2. Make sure that you have Docker Toolbox installed
3. Open a terminal in the fae2 sub-directory (which contains the docker-compose.yml file)
4. Make sure that you have an existing docker-machine started or create and start one:

	```
	$ docker-machine start default
	```
	
	Or if you haven't craeted one yet:
	
	```
	$ docker-machine create
	```
	
	This creates a docker machine named 'default' and starts it using VirtualBox by default.

5. Start the system:

	```
	$ docker-compose up
	```
	
	This single command will start the database, server, and processor.  If this is the first time then the containers will be created and any software required will be automagically installed and setup first.
	
6. Open webapp in browser:

	[http://192.168.99.100:8000/](http://192.168.99.100:8000/)
	
	This assumes the default IP for the docker machine.  You can determine the actual IP using:
	
	```
	$ docker-machine ip default
	```
	
	Where 'default' is the name of the docker machine.


## Usage:

The following is a list of common tasks and how they are performed against the docker environment.

+ **Open bash shell in container**

	```
	$ docker-compose run server bash
	```
	
	Note that 'server' is the name of the container that you want to open the bash shell within.  Any changes made while using this bash shell will be persisted and available to subsequent 'server' containers that are started.

+ **Connect to database via command line:**

	```
	$ docker-compose run server bash
	
	root@749de25acfd0:/usr/src/app# psql -d fae2 -h database -U postgres
	Password for user postgres: ********
	psql (9.4.5)
	Type "help" for help.

	fae2=# 
	```
	
	Note the password is 'password'.  The `-h database` specifies to connect to the 'database' hostname which is mapped to the database container.

+ **Common psql commands**
	+ use different database
	
		```
		# \c dbname
		```

	+ list all databases

		```
		# \l
		```
		
	+ list all table names for current database

		```
		# \dt
		```

	+ display a table schema

		```
		# \d tablename
		```

	+ quit out of psql shell

		```
		# \q
		```

+ **Migrate tables**

	```
	$ docker-compose run server python manage.py migrate
	```

+ **Manually invoke processor**

	```
	$ docker-compose run processor bash
	$ cd fae-util/
	$ . ./org/fae/util/classpath
	$ ./build
	$ rm -r ../../data/jongund/report_00007/data
	$ java org.fae.util.FaeUtil -c ../../data/jongund/report_00007/	report_00007.properties
	```

	After making changes to the fae-util java source code, simply re-execute those last 3 lines to re-try the processing of that properties file with the new code changes.

+ **Manually run django server**

	```
	$ docker-compose run --service-ports server bash
	root@83b445b144b6:/usr/src/app# python manage.py runserver 0.0.0.0:8000
	Performing system checks...
	
	System check identified no issues (0 silenced).
	January 20, 2016 - 13:58:53
	Django version 1.9, using settings 'fae2.settings'
	Starting development server at http://0.0.0.0:8000/
	Quit the server with CONTROL-C.
	```
	
	The first line opens a bash shell into the server container. The `--service-ports` option exposes port 8000 to your host OS so that you can open the webapp in your browser at: [http://192.168.99.100:8000/](http://192.168.99.100:8000/)
	
	The second line starts the django server such that it can be accessed on port 8000 from your host OS.


## Resources:

+ **Original Firefox Addon:**

	[https://addons.mozilla.org/en-US/firefox/addon/ainspector-sidebar/](https://addons.mozilla.org/en-US/firefox/addon/ainspector-sidebar/)


## Requirements:

+ **Docker Toolbox:**

	Docker Toolbox is a collection of docker tools that provide a complete environment for working with docker.
	
	[https://www.docker.com/docker-toolbox](https://www.docker.com/docker-toolbox)

+ **VirtualBox**

	These instructions assume you are using VirtualBox.  But, you can easily adapt to using an AWS container, or VMware, or whatever.

+ **Nothing else**

	No other software is required.  The entire development environment is provided via docker containers.