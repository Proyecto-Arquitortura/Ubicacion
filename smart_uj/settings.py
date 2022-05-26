from prettyconf import config as pconfig

DEBUG = pconfig("DEBUG",
                default=False)

VERSION = pconfig("VERSION",
                  default="2.4.0")

# Change this to the database you want to use
SQLALCHEMY_DATABASE_URI = pconfig("SQLALCHEMY_DATABASE_URI",
                                  default="postgresql://postgres:postgres@localhost:5432/smart_uj")

SECRET_KEY = pconfig("SECRET_KEY",
                     default="smart_uj?")

JSONIFY_PRETTYPRINT_REGULAR = pconfig("JSONIFY_PRETTYPRINT_REGULAR",
                                      default=True)
