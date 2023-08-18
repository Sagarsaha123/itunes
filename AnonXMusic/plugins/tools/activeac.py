from AnonXMusic import app
from AnonXMusic.utils.database.memorydatabase import active, activevideo
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic.utils.inline.play import close_keyboard
from config import OWNER_ID



@app.on_message(filters.command("ac") & filters.user(OWNER_ID))
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"✫ <b><u>ʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ.📟</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}", quote=True, reply_markup=close_keyboard)


@app.on_message(filters.command("activevc") & filters.user(OWNER_ID))
async def start(client: Client, message: Message):
    await message.reply_text(f"ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ʟɪsᴛ...")
