#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "33772865"))
API_HASH = environ.get("API_HASH", "8bfd1acf38686fc8ac29f44205450597")
BOT_TOKEN = environ.get("BOT_TOKEN", "8702988582:AAFpjZvHMR8OdBXg6nAFSwWJTlWyD4_2g_4")

OWNER = int(environ.get("OWNER", "6761345074"))
CREDIT = environ.get("CREDIT", "🜲꯭⌯❖ Mʀ᭄ 𝐍𝐞𝐞𝐫𝐚𝐣[𝐁𝐖] •𝆺꯭𝅥─‌‌⃝🦅")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6761345074').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6761345074').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
