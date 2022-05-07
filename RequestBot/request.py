#()5MysterySD

from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from RequestBot.bot import RequestBot
from config import OWNER_ID, LOGGER 

@RequestBot.on_message(filters.command('start'))
async def start_command(client: Client, message: Message):
    try:
        id = message.from_user.id
        chatid = message.chat.id 
        start = message.reply_text("Request Assigned")
    except Exception as e:
        LOGGER.getLogger(__name__).error(err)
