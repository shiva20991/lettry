from bot.core.get_vars import get_val


async def start_handler(message):
    user_id= message.sender_id
    chat_id= message.chat_id
    if user_id in get_val("ALLOWED_USERS") or chat_id in get_val("ALLOWED_CHATS") or user_id == get_val("OWNER_ID"):
        msg = '''**Selamat datang di Mirror RClone Bot, Bot ini dapat membantumu mengunggah TG file ke penyimpanan awan ataupun sebaliknya; serta trasnfer antar penyimpanan awan.\n
'''
        await message.reply(msg)
    else:
        await message.reply('Kamu tidak diijinkan!')
