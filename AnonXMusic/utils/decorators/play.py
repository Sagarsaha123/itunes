import asyncio

from pyrogram import filters
from pyrogram.errors import (ChatAdminRequired, FloodWait,
                             UserAlreadyParticipant, UserNotParticipant)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import LOGGER_ID, PLAYLIST_IMG_URL, adminlist, MUSIC_BOT_NAME, SUPPORT_GROUP
from strings import get_string
from AnonXMusic import YouTube, app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (get_cmode, get_lang, get_playmode, get_playtype,
                                       is_active_chat, is_served_user)
from AnonXMusic.utils.database.assistantdatabase import get_assistant
from AnonXMusic.utils.database.memorydatabase import is_maintenance
from AnonXMusic.utils.inline.playlist import botplaylist_markup


links = {}


def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴏᴡ ᴛᴏ ғɪx ?",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(_["general_4"], reply_markup=upl)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    f"{MUSIC_BOT_NAME} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_GROUP}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ."
                )

        try:
            await message.delete()
        except:
            pass

        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if audio_telegram is None and video_telegram is None and url is None:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["play_20"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])
            fplay = True
        else:
            fplay = None

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                try:
                    get = await app.get_chat_member(chat_id, userbot.id)
                except ChatAdminRequired:
                    return await message.reply_text(
                        "» ʙᴏᴛ ʀᴇǫᴜɪʀᴇs <b>ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ</b> ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ."
                    )
                if get.status == ChatMemberStatus.BANNED or get.status == ChatMemberStatus.RESTRICTED:
                    return await message.reply_text(
                        f"<u>{MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ɪs ʙᴀɴɴᴇᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.</u>\n\n<b>ɪᴅ :</b> <code>{userbot.id}</code>\n<b>ɴᴀᴍᴇ :</b> {userbot.name}\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{userbot.username}\n\nᴘʟᴇᴀsᴇ ᴜɴʙᴀɴ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.",
                    )
            except UserNotParticipant:
                if chat_id in links:
                    invitelink = links[chat_id]
                else:
                    if message.chat.username:
                        invitelink = message.chat.username
                        try:
                            await userbot.resolve_peer(invitelink)
                        except:
                            pass
                    else:
                        try:
                            invitelink = await app.export_chat_invite_link(chat_id)
                        except ChatAdminRequired:
                            return await message.reply_text(
                                "» ʙᴏᴛ ʀᴇǫᴜɪʀᴇs <b>ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ</b> ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ."
                            )
                        except Exception as e:
                            return await message.reply_text(
                                f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ {MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.\n\nʀᴇᴀsᴏɴ : <code>{type(e).__name__}</code>"
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                myu = await message.reply_text(
                    f"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\nɪɴᴠɪᴛɪɴɢ {MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ..."
                )
                try:
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                except InviteRequestSent:
                        try:
                            await app.approve_chat_join_request(chat_id, userbot.id)
                        except Exception as e:
                            return await message.reply_text(
                                f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ {MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.\n\nʀᴇᴀsᴏɴ : <code>{type(e).__name__}</code>"
                            )
                    await asyncio.sleep(3)
                    await myu.edit(
                        f"{MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.\n\nᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍ..."
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    return await message.reply_text(
                        f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ {MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.\n\nʀᴇᴀsᴏɴ : <code>{type(e).__name__}</code>"
                    )

                links[chat_id] = invitelink

                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
