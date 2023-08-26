import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "10577960"))
API_HASH = getenv("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6139173699:AAGNYFgSSZA7MLMm8UoI77DdX7sFAEvHOo8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://lecej39035:lecej39035@cluster0.mvqxqlm.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOG_ID = int(getenv("LOG_ID", "-1001831007764"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001969560344"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5665115127"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Raichuop07/Tcsv2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tcs_chatting_hub_forever")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/about_tcs")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5363619fbddd46bb80021085e46c620e")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5d3180c8869847cebc15dab2a2586b90")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 700))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFqNk0AMzLBKFJJAns8215lBX8P7mk0UhYx3MRYlScEOz69yatcUMKlpGYhLXtpaAVYYOeZoYOf696t_WRuZfQhJoDK6n9zScCjINvYZC2JIdxMKd3cKXQOgootvOLoVaVETrcWtfj05uKfxBPH6hDT3K-i-pKDjOQyAsiXhuabxN-0ISOtbwduvYRwcwhsBnlsp0paurJlu8wnS-Gm5OSGX3ytc7iEjVcD7A1dtdh42uyozMdKq4usgLelKxouait9SzN6SbJbXfY3vXmjbqyysq4I_IPSo8OYLp2KLbZjNeNPg1WF4nEw2zf_4-HoIFuY33xZpUVBQe4ZfLQmqrdgPiKX2gAAAAFyJzM7AA")
STRING2 = getenv("STRING_SESSION2", "BQFqNk0ApnrqEex2iImaZTwDqzetsq8kU8e-vh_3Sphk-chvygjUarMXV3cBvtZk2tFWwEn23xO6GGm1lMr_5SzHuxTPMTZY9STquXw47evwbQGA3Zp-9OEF08mgQKALM6mHlGlP0o8qKVg1FroX0QuE62QymnUV8vjEiMX25N4pq_om8YM-20vf9lbkZJAcBdKqa9PiQnndM8KielMXx4cJLCsymYDs4dxr-5VsR-D4Z-LWviIYpZc-1ELSmCLYvdoYuXzQZ3E94Ewdz-DXCrDBKZbncEygHspHoudUgjEosf9EkOJTMvECj23iJ1azFeRUcKxIJ_0fprgKRemWP5qZZsIafAAAAAF71Q5pAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/daa9b259ed274c0d5b2e7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/e78fb35228a5a76aa6a07.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


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
