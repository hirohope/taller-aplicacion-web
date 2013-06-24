from __future__ import with_statement
from contextlib import closing
from flask import Flask

#configuration
DATABASE = 'postgres://username:password@host:port/database'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import microblog.views

from microblog.database import db_session
@app.teardown_request
def teardown_request(exception):
	db_session.remove()

