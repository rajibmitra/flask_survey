import os

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)
rel_path = "/home/k/Dropbox/Work/text.txt"
# abs_file_path = os.path.join(script_dir, rel_path)
pw = open(rel_path, 'r+')

CSRF_ENABLED = True
SECRET_KEY = 'xcvBy5aDdDE9lL2CtcPuDwtd6m0VRg9W'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'rkk09c'
MAIL_PASSWORD = pw

# administrator list
ADMINS = ['rkk09c@gmail.com']
