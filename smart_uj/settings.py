from prettyconf import config as pconfig

DEBUG = pconfig("DEBUG",
                default=False)

VERSION = pconfig("VERSION",
                  default="2.4.0")

# TODO: Change this to the database you want to use
SQLALCHEMY_DATABASE_URI = pconfig("SQLALCHEMY_DATABASE_URI",
                                  default="mysql://@10.43.102.22:5432/")
SQLALCHEMY_TRACK_MODIFICATIONS = pconfig("SQLALCHEMY_TRACK_MODIFICATIONS", default=True)

SECRET_KEY = pconfig("SECRET_KEY",
                     default="smart_uj?")

JSONIFY_PRETTYPRINT_REGULAR = pconfig("JSONIFY_PRETTYPRINT_REGULAR",
                                      default=True)
