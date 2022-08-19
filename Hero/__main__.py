import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (LOG_GROUP_ID, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Hero import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, app)
from Hero.Core.Clients.cli import LOG_CLIENT
from Hero.Core.PyTgCalls.Hero import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Hero.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from Hero.Inline import private_panel
from Hero.Plugins import ALL_MODULES
from Hero.Utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Hero.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green]ᴍᴀᴊᴇsᴛᴇ ᴍᴜᴢɪᴋ ʙᴏᴛᴜ ʙᴀşʟᴀᴛɪʟᴅɪ 🌸✨\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>**ᴍᴀᴊᴇsᴛᴇ ᴍᴜᴢɪᴋ ʙᴏᴛᴜ ʙᴀşʟᴀᴛɪʟᴅɪ** 🌸✨</b>",
        )
    except Exception as e:
        print(
            "\nʙᴏᴛ ʟᴏɢ ɢʀᴜʙᴜɴᴅᴀ ᴀᴅᴍɪɴ ᴅᴇɢɪʟ ʙᴏᴛᴜ ᴀᴅᴍɪɴ ʏᴀᴘɪᴘ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ❗"
        )
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("ᴘʀᴏᴍᴏᴛᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ʟᴏɢɢᴇʀ ᴄʜᴀɴɴᴇʟ")
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    console.print(f"\n┌[red] ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs {BOT_NAME}")
    console.print(f"├[green] ɪᴅ :- {BOT_ID}")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_GROUP_ID,
                "<b>ᴀsɪsᴛᴀɴ 1 ʙᴀsʟᴀᴛɪʟᴅɪ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nᴀsɪsᴛᴀɴ 1 ʜᴇsᴀʙɪ ʟᴏɢ ɢʀᴜᴘᴛᴀ ᴀᴅᴍɪɴ ᴅᴇɢɪʟ ᴀᴅᴍɪɴ ʏᴀᴘɪᴘ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await ASS_CLI_1.join_chat("HeroOfficialBots")
            await ASS_CLI_1.join_chat("Yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ 1 sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME1}")
        console.print(f"├[green] ɪᴅ :- {ASSID1}")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>ᴄᴏɴɢʀᴀᴛs ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ 2 ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ 2 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await ASS_CLI_2.join_chat("HeroOfficialBots")
            await ASS_CLI_2.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ 2 sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME2}")
        console.print(f"├[green] ɪᴅ :- {ASSID2}")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>ᴄᴏɴɢʀᴀᴛs ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ 3 ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ 3 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await ASS_CLI_3.join_chat("HeroOfficialBots")
            await ASS_CLI_3.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ 3 sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME3}")
        console.print(f"├[green] ɪᴅ :- {ASSID3}")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>ᴄᴏɴɢʀᴀᴛs ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ 4 ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ 4 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await ASS_CLI_4.join_chat("HeroOfficialBots")
            await ASS_CLI_4.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ 4 sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME4}")
        console.print(f"├[green] ɪᴅ :- {ASSID4}")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>ᴄᴏɴɢʀᴀᴛs ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ 5 ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ 5 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await ASS_CLI_5.join_chat("HeroOfficialBots")
            await ASS_CLI_5.join_chat("Yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ 5 sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME5}")
        console.print(f"├[green] ɪᴅ :- {ASSID5}")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                LOG_GROUP_ID,
                "<b>ᴄᴏɴɢʀᴀᴛs ʟᴏɢɢᴇʀ ᴄʟɪᴇɴᴛ ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🌸✨</b>",
            )
        except Exception as e:
            print(
                "\nʟᴏɢɢᴇʀ ᴄʟɪᴇɴᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʟᴏɢɢᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ❗"
            )
            console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
            return
        try:
            await LOG_CLIENT.join_chat("modmenumaking")
            await LOG_CLIENT.join_chat("yaaro_ki_yaarii")
        except:
            pass
    console.print(f"└[red] ʜᴇʀᴏ ᴍᴜsɪᴄ ʙᴏᴛ ʙᴏᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ...")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")


home_text_pm = f"""**𝖬𝖾𝗋𝗁𝖺𝖻𝖺 𝖡𝖾𝗇 𝖬𝖺𝗃𝖾𝗌𝗍𝖾 𝖬𝗎𝗌𝗂𝖼 𝖯𝗋𝗈 𝖡𝗈𝗍 !**

**𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗍𝖾 𝖬𝗎𝗓𝗂𝗄 𝖵𝖾 𝖵𝗂𝖽𝖾𝗈 𝖮𝗒𝗇𝖺𝗍𝖺𝖻𝗂𝗅𝗂𝗋𝗂𝗆...!**

**𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝖮𝗅𝖺𝗋𝖺𝗄 𝖤𝗄𝗅𝖾𝗒𝗂𝗉 𝖪𝖾𝗌𝗂𝗇𝗍𝗂𝗌𝗂𝗓 𝖬𝗎𝗓𝗂𝗀𝗂𝗇 𝖳𝖺𝖽𝗂𝗇𝗂 𝖢𝗂𝗄𝖺𝗋𝖺𝖻𝗂𝗅𝗂𝗋𝖺𝗂𝗇𝗂𝗓 . . . !**"""


@app.on_message(filters.command(["help", "start"]) & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("Hero") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "⭐️<u> **Owners:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}➤ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = (
                            user.first_name
                            if not user.mention
                            else user.mention
                        )
                        if smex == 0:
                            smex += 1
                            text += "\n⭐️<u> **Sudo Users:**</u>\n"
                        sex += 1
                        text += f"{sex}➤ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("Sudo Kullanıcı Yok !")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>sᴜᴅᴏʟɪsᴛ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
                )
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ**__

❇️**ᴛɪᴛʟᴇ:** {title}

⏳**sᴜʀᴇ:** {duration} Mins
👀**ɪᴢʟᴇᴍᴍᴇ:** `{views}`
⏰**ᴘᴜʙʟɪsʜᴇᴅ ᴛɪᴍᴇ:** {published}
🎥**ᴋᴀɴᴀʟ ɪsᴍɪ:** {channel}
📎**kanal linki:** [Visit From Here]({channellink})
🔗**ᴠɪᴅᴇᴏ ʟɪɴᴋɪ:** [Link]({link})

⚡️ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 ʏᴏᴜᴛᴜʙᴇ ᴅᴇ ɪᴢʟᴇ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 ᴋᴀᴘᴀᴛ", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>ᴠɪᴅᴇᴏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
                )
            return
    out = private_panel()
    await message.reply_text(
        home_text_pm,
        reply_markup=InlineKeyboardMarkup(out[1]),
    )
    if await is_on_off(5):
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
        return await LOG_CLIENT.send_message(
            LOG_GROUP_ID,
            f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
        )
    return


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**𝖬𝖾𝗋𝗁𝖺𝖻𝖺 𝖡𝖾𝗇 𝖬𝖺𝗃𝖾𝗌𝗍𝖾 𝖬𝗎𝗌𝗂𝖼 𝖯𝗋𝗈 𝖡𝗈𝗍 !**

**𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗍𝖾 𝖬𝗎𝗓𝗂𝗄 𝖵𝖾 𝖵𝗂𝖽𝖾𝗈 𝖮𝗒𝗇𝖺𝗍𝖺𝖻𝗂𝗅𝗂𝗋𝗂𝗆...!**

**𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝖮𝗅𝖺𝗋𝖺𝗄 𝖤𝗄𝗅𝖾𝗒𝗂𝗉 𝖪𝖾𝗌𝗂𝗇𝗍𝗂𝗌𝗂𝗓 𝖬𝗎𝗓𝗂𝗀𝗂𝗇 𝖳𝖺𝖽𝗂𝗇𝗂 𝖢𝗂𝗄𝖺𝗋𝖺𝖻𝗂𝗅𝗂𝗋𝖺𝗂𝗇𝗂𝗓 . . . !** """.format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("Yorgun_Birisi"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**𝖬𝖾𝗋𝗁𝖺𝖻𝖺 𝖡𝖾𝗇 𝖬𝖺𝗃𝖾𝗌𝗍𝖾 𝖬𝗎𝗌𝗂𝖼 𝖯𝗋𝗈 𝖡𝗈𝗍 !**

**𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗍𝖾 𝖬𝗎𝗓𝗂𝗄 𝖵𝖾 𝖵𝗂𝖽𝖾𝗈 𝖮𝗒𝗇𝖺𝗍𝖺𝖻𝗂𝗅𝗂𝗋𝗂𝗆...!**

**𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝖮𝗅𝖺𝗋𝖺𝗄 𝖤𝗄𝗅𝖾𝗒𝗂𝗉 𝖪𝖾𝗌𝗂𝗇𝗍𝗂𝗌𝗂𝗓 𝖬𝗎𝗓𝗂𝗀𝗂𝗇 𝖳𝖺𝖽𝗂𝗇𝗂 𝖢𝗂𝗄𝖺𝗋𝖺𝖻𝗂𝗅𝗂𝗋𝖺𝗂𝗇𝗂𝗓 . . . !**"""
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "Here is the help for", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ ɢᴇʀɪ", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 ᴋᴀᴘᴀᴛ", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
