import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "25625520"))
API_HASH = getenv("API_HASH", "b8d327b196bae9b4c72e93a7395b8f05")

BOT_TOKEN = getenv("BOT_TOKEN", "8147450157:AAHT4Qx1rQvyKeZ7geYmXrGGc9f8LTqonXg")
OWNER_USERNAME = getenv("OWNER_USERNAME","AloneHuVai")
BOT_USERNAME = getenv("BOT_USERNAME" , "AloneXMusicBot")
BOT_NAME = getenv("BOT_NAME" , "𝙍𝙚𝙙 ✘ 𝙒𝙞𝙣𝙚 ✘ 𝙈𝙪𝙨𝙞𝙘")
ASSUSERNAME = getenv("ASSUSERNAME" , "RedWineXAss")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1001603822916))
OWNER_ID = int(getenv("OWNER_ID", 7552579717))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DilwarHosen/AloneRobo",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-for-AloneXMusic-12-01")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+1iN6Tuz0-atmODI1")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "700"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", "BQGHA7AACDKewU6Kob8Qg7TNCk7vX8zMma1tk6pkIYESb12qglcyRwIXSdAb5dKevKMHo2RD6zSo0mi7DZmrjWMrA1UwUf9IBlVj96dbIf2j0e41n1hcDriukrVsOnZP7wG9s5O1qDITy8s4ttpsWMG5WREMxtDRui61k8SDhaga8rQJwZ-jEbMVNyagZYSgPepGGsW_UGbwAADU6y5W1ODAzfnF84GIPaVNQVpgX56_ffuRn42-DT-AjKx3TfgP2erTDWfhRubyu-VEhy8Pl4H_-6u_-cTykyAptAcxOiPiVsbB3ZPRJiHgRE4mWtuPqqOdMeOOuVx-BpSpu5Ts7c54728-sQAAAAG2UkNcAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/vr3kx9.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/vr3kx9.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
STATS_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/vr3kx9.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/vr3kx9.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/vr3kx9.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        
