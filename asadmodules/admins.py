# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks Â© @JAI6H Â© Rocks
# Owner Asad + Harshit
 

from cache.admins import admins
from rocksdriver.asad import call_py
from pyrogram import Client, filters
from rocksdriver.decorators import authorized_users_only
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, clear_queue
from rocksdriver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL, REPO_OWNER, BOT_UPDATE, MY_BRO, MY_SERVER, BOT_NAME, MY_HEART
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð É¢á´ Êá´á´á´", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð á´Êá´sá´", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(f"""**âââââââââââââââââââ
ð¥ Êá´ÊÊá´, Éª á´á´ á´ á´ á´Êá´Êá´Ê
Êá´á´ Òá´Ê á´á´Êá´É¢Êá´á´ É¢Êá´á´á´s.
âââââââââââââââââââ
â£â Êá´á´ : [Êá´Êá´á´á´á´á´](t.me/{BOT_USERNAME})
â£â á´á´á´ÉªÉ´ : At [{BOT_NAME}](t.me/Akja0) Êá´ÒÊá´sÊá´á´
â£â sá´á´á´á´Êá´ : [Êá´á´ á´á´á´Atá´s](t.me/BOT_UPDATE)
âââââââââââââââââââ
â¢ ÉªÒ Êá´á´ ÊÉªá´á´ á´Êá´É´ [á´á´á´ á´](t.me/JAI6H) á´á´
â¢ ÉªÒ Êá´á´ Êá´á´ á´ á´É´Ê Â» Ç«á´á´sá´Éªá´É´
á´Êá´É´ á´á´ á´á´ á´Ê [á´á´¡É´á´Ê](t.me/uu_ak)
âââââââââââââââââââ**""",
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("â **ÙØ§ ÙÙØ¬Ø¯ Ø´ÙØ¡ ÙØ´ØºÙ**")
        elif op == 1:
            await m.reply("â ÙÙØ§Ø¦Ù **Ø§ÙØ¥ÙØªØ¸Ø§Ø± ÙØ§Ø±ØºÙ.**\n\n**â¢ ØªÙÙÙ [ØªØ´ØºÙÙ Ø§ÙÙÙØ³ÙÙÙ](t.me/Akja0) ÙØªØ±Ù Ø§ÙØ­Ø³Ø§Ø¨ Ø§ÙÙØ³Ø§Ø¹Ø¯ Ø§ÙÙØ­Ø§Ø¯Ø«Ù Ø§ÙØµÙØªÙÙ**")
        elif op == 2:
            await m.reply("ðï¸ **ÙØ³Ø­ ÙÙØ§Ø¦Ù Ø§ÙØ§ÙØªØ¸Ø§Ø±**\n\n**ØªÙÙÙ [ØªØ´ØºÙÙ Ø§ÙÙÙØ³ÙÙÙ](t.me/Akja0) ÙØªØ±Ù Ø§ÙØ­Ø³Ø§Ø¨ Ø§ÙÙØ³Ø§Ø¹Ø¯ Ø§ÙÙØ­Ø§Ø¯Ø«Ù Ø§ÙØµÙØªÙÙ**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"â­ **Skipped to next tarck.**\n\nðï¸ **Name:** [{op[0]}]({op[1]})\n\nð **Status:** `Playing`\nð§ **Request by:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "ð **ØªÙ Ø§Ø²Ø§ÙÙ Ø§ÙØ§ØºÙÙÙ**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("â **ØªÙ Ø§ÙÙØ§Ù** [ØªØ´ØºÙÙ](t.me/JAI6H) **Ø§ÙÙÙØ³ÙÙÙ ÙÙ Ø§ÙÙØ¬ÙÙØ¹Ù**")
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â ÙØ§ ØªÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "â¸ **ØªÙ Ø¥ÙÙØ§Ù Ø§ÙÙØ³Ø§Ø± ÙØ¤ÙØªÙØ§.**\n\nâ¢ **ÙØ§Ø³ØªØ¦ÙØ§Ù Ø§Ø³ØªØ®Ø¯Ø§Ù**\nÂ» /resume ."
            )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â ÙØ§ ØªÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "â¶ï¸ **At** [ØªØ´ØºÙÙ Ø§ÙÙÙØ³ÙÙÙ](t.me/Akja0) **TÊá´á´á´ Éªs Êá´sá´á´á´á´.**\n\nâ¢ **To pause the stream, use the**\nÂ» /pause command."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â ÙØ§ ØªÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "ð ØªÙ ÙØªÙ Ø§ÙØµÙØª Ø¨ÙØ¬Ø§Ø­ .**\n\nâ¢ **Ø§Ø³ØªØ®Ø¯Ù ÙØ°Ø§ Ø§ÙØ§ÙØ± ÙØ§ÙØºØ§Ø¡ Ø§ÙÙØªÙ**\nÂ» /unmute ."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â ÙØ§ ØªÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "ð **ØªÙ Ø§ÙØºØ§Ø¡ Ø§ÙÙØªÙ Ø¹ÙØ¯ ØªØ´ØºÙÙ Ø§ÙÙÙØ³ÙÙÙ Ø ÙÙÙÙ Ø§ÙØ¨ÙØª ØºÙØ± ÙÙØªÙÙ.**\n\nâ¢ **ÙÙØªÙ ØµÙØª Ø§ÙØ§ØºØ§ÙÙ Ø§Ø±Ø³Ù Ø§ÙØ±**\nÂ» /mute ."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â ÙØ§ ØªÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Java .ï¸", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/Akja0"),
            ]
        ]
    )


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ÙÙØ§Ù Ø®Ø·Ø§ ÙØ§ Ø¹Ø²ÙØ²Ù !\n\nÂ» ÙØ±Ø¬Ù Ø¥ÙÙØ§Ù ØµÙØ§Ø­ÙÙ Ø§ÙØ¨ÙØ§Ø¡ ÙØ®ØªÙÙØ§Ù.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð Ø§ÙÙØ³Ø¤ÙÙ Ø§ÙÙØ­ÙØ¯ Ø§ÙØ°Ù ÙØ¯ÙÙ Ø¥Ø°Ù Ø¥Ø¯Ø§Ø±Ø© Ø§ÙØ¯Ø±Ø¯Ø´Ø§Øª Ø§ÙØµÙØªÙØ© ÙÙÙÙÙ Ø§ÙÙÙØ± Ø¹ÙÙ ÙØ°Ø§ Ø§ÙØ²Ø± !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "â¸ the streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â ÙØ§ ÙÙØ¬Ø¯ Ø´Ø¦ ÙØ´ØºÙ Ø§ÙØ§Ù", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ÙÙØ§Ù Ø®Ø·Ø§ ÙØ§ Ø¹Ø²ÙØ²Ù !\n\nÂ» ÙØ±Ø¬Ù Ø¥ÙÙØ§Ù ØµÙØ§Ø­ÙÙ Ø§ÙØ¨ÙØ§Ø¡ ÙØ®ØªÙÙØ§Ù.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð Ø§ÙÙØ³Ø¤ÙÙ Ø§ÙÙØ­ÙØ¯ Ø§ÙØ°Ù ÙØ¯ÙÙ Ø¥Ø°Ù Ø¥Ø¯Ø§Ø±Ø© Ø§ÙØ¯Ø±Ø¯Ø´Ø§Øª Ø§ÙØµÙØªÙØ© ÙÙÙÙÙ Ø§ÙÙÙØ± Ø¹ÙÙ ÙØ°Ø§ Ø§ÙØ²Ø± !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "â¶ï¸ ØªÙ Ø§Ø³ØªØ¦ÙØ§Ù Ø§ÙØ¨Ø«", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â ÙØ§ ÙÙØ¬Ø¯ Ø´Ø¦ ÙØ´ØºÙ Ø§ÙØ§Ù", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ÙÙØ§Ù Ø®Ø·Ø§ ÙØ§ Ø¹Ø²ÙØ²Ù !\n\nÂ» ÙØ±Ø¬Ù Ø¥ÙÙØ§Ù ØµÙØ§Ø­ÙÙ Ø§ÙØ¨ÙØ§Ø¡ ÙØ®ØªÙÙØ§Ù.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð Ø§ÙÙØ³Ø¤ÙÙ Ø§ÙÙØ­ÙØ¯ Ø§ÙØ°Ù ÙØ¯ÙÙ Ø¥Ø°Ù Ø¥Ø¯Ø§Ø±Ø© Ø§ÙØ¯Ø±Ø¯Ø´Ø§Øª Ø§ÙØµÙØªÙØ© ÙÙÙÙÙ Ø§ÙÙÙØ± Ø¹ÙÙ ÙØ°Ø§ Ø§ÙØ²Ø± !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("â **Ø§ÙØªÙÙ ØªØ´ØºÙÙ ÙØ°Ø§ Ø§ÙØ´Ø¦**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â ÙØ§ ÙÙØ¬Ø¯ Ø´Ø¦ ÙØ´ØºÙ Ø§ÙØ§Ù", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ÙÙØ§Ù Ø®Ø·Ø§ ÙØ§ Ø¹Ø²ÙØ²Ù !\n\nÂ» ÙØ±Ø¬Ù Ø¥ÙÙØ§Ù ØµÙØ§Ø­ÙÙ Ø§ÙØ¨ÙØ§Ø¡ ÙØ®ØªÙÙØ§Ù.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð Ø§ÙÙØ³Ø¤ÙÙ Ø§ÙÙØ­ÙØ¯ Ø§ÙØ°Ù ÙØ¯ÙÙ Ø¥Ø°Ù Ø¥Ø¯Ø§Ø±Ø© Ø§ÙØ¯Ø±Ø¯Ø´Ø§Øª Ø§ÙØµÙØªÙØ© ÙÙÙÙÙ Ø§ÙÙÙØ± Ø¹ÙÙ ÙØ°Ø§ Ø§ÙØ²Ø± !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "ð ØªÙ Ø§ÙØºØ§Ø¡ Ø§ÙÙØ¶Ø¹ Ø§ÙØµØ§ÙØª Ø¨ÙØ¬Ø§Ø­", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â ÙØ§ ÙÙØ¬Ø¯ Ø´Ø¦ ÙØ´ØºÙ Ø§ÙØ§Ù", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ÙÙØ§Ù Ø®Ø·Ø§ ÙØ§ Ø¹Ø²ÙØ²Ù !\n\nÂ» ÙØ±Ø¬Ù Ø¥ÙÙØ§Ù ØµÙØ§Ø­ÙÙ Ø§ÙØ¨ÙØ§Ø¡ ÙØ®ØªÙÙØ§Ù.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð Ø§ÙÙØ³Ø¤ÙÙ Ø§ÙÙØ­ÙØ¯ Ø§ÙØ°Ù ÙØ¯ÙÙ Ø¥Ø°Ù Ø¥Ø¯Ø§Ø±Ø© Ø§ÙØ¯Ø±Ø¯Ø´Ø§Øª Ø§ÙØµÙØªÙØ© ÙÙÙÙÙ Ø§ÙÙÙØ± Ø¹ÙÙ ÙØ°Ø§ Ø§ÙØ²Ø± !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "ð ØªÙ Ø§ÙØºØ§Ø¡ Ø§ÙØµÙØª Ø¨ÙØ¬Ø§Ø­**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â **ÙØ§ ÙÙØ¬Ø¯ Ø´Ø¦ ÙØ´ØºÙÙ Ø§ÙØ§Ù**", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"â **ØªÙ Ø¶Ø¨Ø· Ø§ÙØµÙØª Ø¹ÙÙ** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"ð« **ÙÙØ§Ù Ø®Ø·Ø£:**\n\n`{e}`")
    else:
        await m.reply("â **ÙØ§ ÙÙØ¬Ø¯ ÙÙØ³ÙÙÙ ÙØ´ØºÙÙ Ø§ÙØ§Ù**")