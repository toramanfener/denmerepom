from pyrogram import Client, filters
from pyrogram.types import Message

from Hero import SUDOERS, app
from Hero.Database import (_get_authusers, delete_authuser, get_authuser,
                            get_authuser_count, get_authuser_names,
                            save_authuser)
from Hero.Decorators.admins import AdminActual
from Hero.Utilities.changers import (alpha_to_int, int_to_alpha,
                                      time_to_seconds)

__MODULE__ = "Yönetici Kullanıcılar"
__HELP__ = """

**ɴᴏᴛᴇ:**
-ᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴘ, ᴘᴀᴜsᴇ, sᴛᴏᴘ, ʀᴇsᴜᴍᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴇᴠᴇɴ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs...


`/ver` [ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ ᴠᴇʏᴀ ᴍᴇsᴀᴊ ʏᴀɴɪᴛʟᴀᴍᴀ] 
- ʏᴇᴛᴋɪʟɪ ᴏʟᴍᴀʏᴀɴ ᴋᴜʟʟᴀɴɪᴄɪʏᴀ ʏᴏɴᴇᴛɪᴄɪ ᴋᴏᴍᴜᴛʟᴀᴛɪɴɪ ᴋᴜʟʟᴀɴᴍᴀsɪ ɪᴄɪɴ ʏᴇᴛᴋɪ ᴠᴇʀɪɴ.

`/al` [ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ ᴠᴇʏᴀ ᴍᴇsᴀᴊ ʏᴀɴɪᴛʟᴀᴍᴀ] 
- ʙᴏᴛ ᴅᴀ ʏᴏɴᴇᴛɪᴄɪ ɪᴢɪɴʟᴇʀɪ ᴠᴇʀᴅɪɢɪɴɪᴢ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴀɴ ʏᴇᴛᴋɪʏɪ ᴀʟɪɴ.

`/authusers` 
- ɢʀᴜʙᴜɴᴜᴢᴅᴀᴋɪ ʏᴇᴛᴋɪʟɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀ.
"""


@app.on_message(filters.command("ver") & filters.group)
@AdminActual
async def auth(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ ᴠᴇʀɪɴ ᴠᴇʏᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ. \n\nᴏʀɴᴇᴋ /auth @MajesteSahip"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = 0
        for smex in _check:
            count += 1
        if int(count) == 20:
            return await message.reply_text(
                "**sᴜ ᴀɴʟɪᴋ sᴀᴅᴇᴄᴇ 20 ᴋᴜʟʟᴀɴɪᴄɪ ᴇᴋʟᴇʏᴇʙɪʟɪʀsɪɴ...!**"
            )
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            await save_authuser(message.chat.id, token, assis)
            await message.reply_text(
                f"ᴋᴜʟʟᴀɴɪᴄɪ ʏᴇᴛᴋɪʟɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴇᴋʟᴇɴᴅɪ..."
            )
            return
        else:
            await message.reply_text(f"ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ...")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text(
            "**sᴜ ᴀɴʟɪᴋ sᴀᴅᴇᴄᴇ 20 ᴋᴜʟʟᴀɴɪᴄɪ ᴇᴋʟᴇʏᴇʙɪʟɪʀsɪɴ..!**"
        )
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        await save_authuser(message.chat.id, token, assis)
        await message.reply_text(
            f"ᴋᴜʟʟᴀɴɪᴄɪ ʏᴇᴛᴋɪʟɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴇᴋʟᴇɴᴅɪ..."
        )
        return
    else:
        await message.reply_text(f"ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ...")


@app.on_message(filters.command("al") & filters.group)
@AdminActual
async def whitelist_chat_func(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ ɪᴅ"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        if deleted:
            return await message.reply_text(
                f"ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ..."
            )
        else:
            return await message.reply_text(f"ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀ...")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    if deleted:
        return await message.reply_text(
            f"ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ..."
        )
    else:
        return await message.reply_text(f"ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀ...")


@app.on_message(filters.command("authusers") & filters.group)
async def authusers(_, message: Message):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text(
            f"**Grubunuzda Yetkili Kullanıcı Bulunmadı.** \n\nEklemek İçin /ver almak için /al Kullanın."
        )
    else:
        j = 0
        m = await message.reply_text(
            "ғᴇᴛᴄʜɪɴɢ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ..."
        )
        msg = f"**ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ[ᴀᴜʟ]:**\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            user_name = _note["auth_name"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            msg += f"{j}➤ {user}[`{user_id}`]\n"
            msg += f"    ┗ ᴀᴅᴅᴇᴅ ʙʏ:- {admin_name}[`{admin_id}`]\n\n"
        await m.edit_text(msg)
