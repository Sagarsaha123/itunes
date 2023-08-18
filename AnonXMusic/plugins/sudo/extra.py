# © @MR_RAICHU & @PyXen

import os

from asyncio import sleep
from traceback import format_exc

from config import LOGGER_ID, OWNER_ID, STRING1, STRING2, STRING3, STRING4, STRING5

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import UserDeactivated, UserNotParticipant, FloodWait

from AnonXMusic import app, userbot
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import get_served_chats
from AnonXMusic.utils.decorators.language import language

MAINGROUP_ID = LOGGER_ID

ub1 = userbot.one
ub2 = userbot.two
ub3 = userbot.three
ub4 = userbot.four
ub5 = userbot.five

# Check Every Userbots & Bot
@app.on_message(filters.command(/check) & filters.user(OWNER_ID))
@language
async def systest(client, message: Message, _):
    mys = await message.reply_text(_["extra_1"])
    await app.send_message(LOGGER_ID, _["extra_2"])
    suspendedacc = []
    count = 0

    if STRING1:
        try:
            await userbot.one.send_message(LOGGER_ID, _["extra_3"].format("1"))
            count += 1
        except UserDeactivated:
            suspendedacc.append("Assistant 1")

    if STRING2:
        try:
            await userbot.two.send_message(LOG_GROUP_ID, _["extra_3"].format("2"))
            count += 1
        except UserDeactivated:
            suspendedacc.append("Assistant 2")

    if STRING3:
        try:
            await userbot.three.send_message(LOGGER_ID, _["extra_3"].format("3"))
            count += 1
        except UserDeactivated:
            suspendedacc.append("Assistant 3")

    if STRING4:
        try:
            await userbot.four.send_message(LOGGER_ID, _["extra_3"].format("4"))
            count += 1
        except UserDeactivated:
            suspendedacc.append("Assistant 4")

    if STRING5:
        try:
            await userbot.five.send_message(LOGGER_ID, _["extra_3"].format("5"))
            count += 1
        except UserDeactivated:
            suspendedacc.append("Assistant 5")

    mtext = _["extra_4"].format(count, len(suspendedacc))
    if len(suspendedacc) > 0:
        mtext += _["extra_5"].format(", ".join(suspendedacc))
    await mys.edit_text(mtext)


# Logs, Temps Etc Cleaner Without Restarting Bot
@app.on_message(avoice(["/fc"]) & SUDOERS)
async def cleaning(client: Client, message: Message):
    A = 'rm -rf downloads'
    try:
        os.system(A)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Downloads", quote=True)

    
CPU_LOAD = psutil.cpu_percent(interval=0.5)
RAM_LOAD = psutil.virtual_memory().percent
DISK_SPACE = psutil.disk_usage("/").percent

#Link Creater
@app.on_message(
    filters.command(link)
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def new_link_getter(client, message: Message):
    try:
        chat_id = int(message.text.split(" ", maxsplit=1)[1])
    except:
        await message.reply_text("**Usage:** /link [ᴄʜᴀᴛ-ɪᴅ]")
        return

    try:
        link = await app.export_chat_invite_link(chat_id)
        await message.reply_text(f"**Chat's Link** >>\n\n{link}", quote=True)
    except:
        try:
            link = await app.create_chat_invite_link(chat_id)
            await message.reply_text(f"**Chat's Link** >>\n\n{link}", quote=True)
        except:
            await message.reply_text("**Error**\nMaybe Bot Have No Permission Of Invite Users Permission OR Bot Removed!", quote=True)


@app.on_message(
    filters.command(/track)
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
@language
async def tracking_user(client, message: Message, _):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        try:
            user_id = int(message.text.split(" ", maxsplit=2)[1])
        except:
            await message.reply_text("**Usage:** /track [ᴜsᴇʀ_ɪᴅ | ʀᴇᴘʟʏ_ᴛᴏ_ᴜsᴇʀ]")
            return

    replyreport = await message.reply_text("🏷 **Trying To Validate The User...**")
    await sleep(1)
    try:
        await app.resolve_peer(user_id)
        validated_user = await app.get_users(user_id)
    except:
        return await replyreport.edit_text("❌ **Bot Never Met This User!\nPlease Force That User To Start your bot even if bot is not online!\nFor Now, Stopping The Tracking!!**")

    await replyreport.edit_text("✅ **User Validated!\n\n🔄 Loading Database...**")
    allchats = []
    dbchat = await get_served_chats()
    for chat in dbchat:
        allchats.append(int(chat["chat_id"]))

    await sleep(3)
    await replyreport.edit_text(f"✅ **{len(allchats)} Chats Loaded!\n\n🔄 Tracking Now...**")

    addmintext = ""
    foundtext = ""
    ownertext = ""
    addminfoundin = 0
    foundin = 0
    ownerin = 0

    for chat_id in allchats:
        try:
            user = await app.get_chat_member(chat_id, user_id)
            if user.status == "creator":
                ownerin += 1
                ownertext += f"\n {ownerin}. {chat_id}"
            elif user.status == "administrator":
                addminfoundin += 1
                addmintext += f"\n {addminfoundin}. {chat_id}"
            elif user.status == "member":
                foundin += 1
                foundtext += f"\n {foundin}. {chat_id}"
            await sleep(0.3)
        except UserNotParticipant:
            continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await sleep(flood_time)
        except:
            pass

    await sleep(1)
    ran_hash = f"\\files\\UserChats{user_id}.txt"
    data = f"OwnerGroupsID:\n{ownertext}\n\n\nAdminGroupsID:\n{addmintext}\n\n\nMemberGroupsID:\n{foundtext}"
    with open(ran_hash, "w") as lyr:
        lyr.write(data)
    mtext = f"""✅ **Tracking Completed!**

✨ **User Info!**
**‣ ɴᴀᴍᴇ:** {validated_user.mention}
**‣ ᴜsᴇʀ_ɪᴅ:** `{validated_user.id}`
**‣ ᴜsᴇʀɴᴀᴍᴇ:** @{validated_user.username}

**Common Chats** = {ownerin + addminfoundin + foundin}
**Owner In** = {ownerin} Groups
**Admin In** = {addminfoundin} Groups
**Member In** = {foundin} Groups"""
    try:
        await message.reply_document(ran_hash, caption=mtext, file_name="UserChats.txt")
        try:
            await replyreport.delete()
        except:
            return
    except Exception as e:
        await replyreport.edit_text(_["error_1"].format(str(e)))
    finally:
        os.remove(ran_hash)
