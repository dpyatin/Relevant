import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

twitter_config = {
	'consumer_key': '',
	'consumer_secret': '',
	'access_token_key': '',
	'access_token_secret': ''
}
