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
