#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from pyrogram import filters

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database import autoend_off, autoend_on
from AlexaMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**الاستخدام:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل انهاء البث التلقائي.\n\nسيغادر المساعد محادثة الفيديو تلقائيًا بعد بضع دقائق عندما لا يكون احد يستمع  مع رسالة تحذيرية."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("تم تعطيل إنهاء البث التلقائي.")
    else:
        await message.reply_text(usage)
