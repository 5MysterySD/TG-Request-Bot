#()5MysterySD

from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from config import OWNER_ID

@Bot.on_message(filters.command('request'))
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    chatid = message.chat.id 
    start = message.reply_text("Request Assigned")
