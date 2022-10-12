import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("RJ"):
  load_dotenv("RJ")

# import os
# from os import getenv
# from dotenv import load_dotenv

# if os.path.exists("local.env"):
   #  load_dotenv("local.env")

# load_dotenv()
# admins = {}
SESSION_NAME = getenv("SESSION_NAME", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME", None)
API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
OWNER_NAME = getenv("OWNER_NAME", "Romeo")
OWNER_USERNAME = getenv("OWNER_USERNAME", None)
ALIVE_NAME = getenv("ALIVE_NAME", None)
BOT_USERNAME = getenv("BOT_USERNAME", None)
OWNER_ID = getenv("OWNER_ID", None)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", None)
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RomeoBot_op")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Romeo_op")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Romeo-RJ/Romeo-musicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg")
