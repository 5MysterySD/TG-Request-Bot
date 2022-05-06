import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5347120398:AAFKgxPGUF6jjTqSf4h5RPlp_DYEG_baA2Y")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6878048"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3833ae3a7415af46df46a83a3ba2c432")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1789263079"))

LOG_FILE_NAME = "Requestbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
