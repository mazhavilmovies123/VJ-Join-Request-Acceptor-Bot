from os import environ

API_ID = int(environ.get("API_ID", "21419016"))
API_HASH = environ.get("API_HASH", "79198e1eb4cfd0f771a89d83b9144e7e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8195734162:AAEDqrvuIgVqnPqEJ4yiDcwtMUW9K8lM3mQ")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003132292615"))
ADMINS = int(environ.get("ADMINS", "1933114137"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://melodysotto4_db_user:BCUKIKDEAqFEzeCj@cluster0.trrt89o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "Mazhavilapproverbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
