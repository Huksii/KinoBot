from dotenv import load_dotenv
from os import getenv
load_dotenv

TOKEN = "6239692911:AAF8Ue3tvAXCdOwyCs2aQymgNgsw1R8h268"
ADMIN_ID = getenv("ADMIN_ID")

URL = getenv("URL")
DOMAIN = getenv("DOMAIN")

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36"}