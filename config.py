import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8967766")) #optional
API_HASH = getenv("API_HASH", "505dc1f394f59c8a55b1aa798a0715f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1989750989").split()))
OWNER_ID = int(getenv("OWNER_ID", 1989750989))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Hacker999:selvan868@cluster0.z27ur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5224062087:AAGb5ZWLUKjNEQwqk_N7pm6dWT6S0VK8rLg")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/947c56dfb8e2c588b9bd3.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "Your Account Hacked So You Can't Access Me Bye 😂")
PM_LOGGER = getenv("PM_LOGGER", "Nakku Setha Payala)
LOG_GROUP = getenv("LOG_GROUP", "-1001869389707")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/bavabee/Zaid")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQByDjHneo7z7A3PGQzlnBqJT8Flfh_CAjPvpHaCrZAZld_Kb1C6abM3K65Nsy0w19Ax9DhfkpOmRxSS0R0lEZGaoWIcdCYwnUBIUxhGNo_v-FdZarQjuNsR9K1rQmzXSn9hoNDJG9Sp7ILZW6Nn3ncUvU3c5KK41uPGuENKDGzoHZ5y7lPV0QE7VtWYWt9nW5sfopv2m9dICSX2ikzWPRFGJqO35LdHnzeqSNAJd8UxqEtDS5KnjKEhoab-ugKZV1A-KLC115WVLAY6lF_8KUFPzaqIIG-b_-tu7zvNhbEdYEe58lScCgk34UMOhUP8yrEgrcH7ZJPUbpiPfh6YZJzRQnZcZwA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
