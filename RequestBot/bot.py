# (c) 5MysterySD

from typing import Union
from pyromod import listen
from pyrogram import Client as RawClient
from pyrogram.storage import Storage

from config import API_HASH, APP_ID, OWNER_ID, BOT_TOKEN

class Client(RawClient):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "RequestBot"):
        super().__init__(
            session_name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "plugins"
            },
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.LOGGER(__name__).info("Bot Started!")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped!")
