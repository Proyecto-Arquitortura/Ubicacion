from prettyconf import config as pconfig

DEBUG = pconfig("DEBUG", default=False)

VERSION = pconfig("VERSION", default="2.4.0")

MONGODB_SETTINGS = {
    'host': pconfig("MONGODB_HOST", default='mongodb+srv://evadb.l657k.mongodb.net/EvaDB'),
    'port': pconfig("MONGODB_PORT", default=27017),
    'username': pconfig("MONGODB_USERNAME", default='oscar'),
    'password': pconfig("MONGODB_PASSWORD", default='iwCTSZT1h9Ky3FgQ'),
}

SECRET_KEY = pconfig("SECRET_KEY", default="iwCTSZT1h9Ky3FgQ")

JSONIFY_PRETTYPRINT_REGULAR = pconfig("JSONIFY_PRETTYPRINT_REGULAR", default=True)
