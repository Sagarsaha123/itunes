from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus

import config
from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        try:
            await self.send_message(config.LOG_GROUP_ID, "Bot Started")
        except errors.PeerIdInvalid:
            raise SystemExit(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
        except Exception as ex:
            raise SystemExit(
                f"Bot has failed to access the log group/channel.\nReason : {type(ex).__name__}."
            )
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            raise SystemExit("Please promote your bot as an admin in your log group/channel.")
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")
