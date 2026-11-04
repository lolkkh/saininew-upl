#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "33772865"))
API_HASH = environ.get("API_HASH", "8bfd1acf38686fc8ac29f44205450597")
BOT_TOKEN = environ.get("BOT_TOKEN", "8676600538:AAHT7JW6HU7RqRMbwdVt4W0daTCWf4ltUx0")

OWNER = int(environ.get("OWNER", "8749565729"))
CREDIT = environ.get("CREDIT", "vj BOSS")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8749565729').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6761345074').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
