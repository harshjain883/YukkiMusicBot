#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=f"{BOT_NAME} ɪs ᴘɪɴɢɪɴɢ..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""➻ ᴩᴏɴɢ : `{resp}ᴍs`
<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :</u></b>
๏ **ᴜᴩᴛɪᴍᴇ :** {uptime}
๏ **ʀᴀᴍ :** {mem}
๏ **ᴄᴩᴜ :** {cpu}
๏ **ᴅɪsᴋ :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❄ sᴜᴘᴘᴏʀᴛ ❄", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "✨ sᴏᴜʀᴄᴇ ✨",
                        callback_data="gib_source",
                    ),
                ],
            ]
        ),
    )
