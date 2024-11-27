import os

TOKEN = None
DB_CREDENTIALS = None


def get_token():
    global TOKEN

    if TOKEN is None:
        TOKEN = os.getenv("BOT_TOKEN")

    return TOKEN
