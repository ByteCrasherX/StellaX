

import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


ZEN = f"""✘ 𝐒𝐓𝐄𝐋𝐋𝐀 𝐗 ✘

➲ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.11.1`
➲ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `1.4.16`
➲ **sᴛᴇʟʟᴀ ᴠᴇʀsɪᴏɴ**  : `1.0`
➲ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ** : @ZenBotX\n"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"◇ SᴛᴇʟʟᴀX\n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `1.0`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=ZEN)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.id, ALIVE_PIC, caption=ZEN)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀɛsтαятιиɢ вσт...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ `60` sᴇᴄᴏɴᴅs.")
    execle(sys.executable, *args, environ)
