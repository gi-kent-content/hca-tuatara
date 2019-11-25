# HCA-Tuatara
A little python-based web site for helping the wranglers and others track incoming single cell projects as they are brought 
into HCA.

Note that we are trying to develop this the tried and true (for us at least) spiral approach to development.
By this I mean rather than develop a spec that gets sent around and expanded and argued,  we develop a working
prototype that we gradually add features to in response to requests from people who use the prototype.
The initial prototype was built after discussions with prospective users.  In spiral development,
at all points working code is maintained.   The prototype will gradually develop into production code. It is
not thrown away.  In fact it is already pretty robust. 

Please contact Clay Fischer if you would like access to the actual web site as well as the code.  

The code is in Python 3, and relies on Django and a database.  Django fortunately is flexible about what database
it connects to, so long as it supports SQL.  We have flipped it between sqllite3 and mariaDb.  You'll need to edit
the mysite/settings.py file in the database section to point it to your own database, or just comment out the mariaDb
stuff and uncomment the sqllite3 stuff for a quick look.

Deployments (DEPL) are: dev, test, stage, and prod

#create new
virtualenv hcat_DEPL
or 
mkvirtualenv --python=/path/to/python3 hcat_DEPL

# activate it
source DEPL/bin/activate

#use virtualenv
workon hcat_DEPL

use pip 

Requirements are in requirements/ subdirectory.
Install the base requirements:
pip install -r requirements/base.txt

Also use the requirment corresponding to your deployment (developer, testing, staging, production)
pip install -r requirements/DEPLOYMENT.txt

Settings may be customized under mysite/settings/
Edit the base.py or corresponding DEPLOYMENT.py settings file.

Set the following in your virtualenv

workon hcat_dev
cd $VIRTUAL_ENV/bin

vi postactivate
--- append the following lines
export DJANGO_SETTINGS_MODULE="mysite.settings.SOMEDEPLOYMENT"
export HCAT_MEDIA="/hive/groups/hca/hcat/SOMEUSER/media/"
export HCAT_DB='hcatSOMEUSER'
export HCAT_USER='hgcat'
export HCAT_PASSWORD='NOT_SHOWN'
export HCAT_WEBPORT="8126"

Of course, you MUST customize it to your own deployment and username and media files location.
It is probably a bad idea to use what others are using. 
You should have your own instance of the database and media.

Find a free tcp port number for your development server and assign it to web port.
(This step is not required for production, which uses apache server configuration.)

vi predeactivate
--- append the following lines
unset DJANGO_SETTINGS_MODULE
unset HCAT_MEDIA
unset HCAT_DB
unset HCAT_USER
unset HCAT_PASSWORD
unset HCAT_WEBPORT

TODO instructions for cloning hcat db and media from production (or a backup of it).


workon hcat_DEPL
./runserver

