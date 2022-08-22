import asyncio
import os

import wget
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaDocument, InputMediaVideo, Message)
from youtubesearchpython import VideosSearch

from Hero import MUSIC_BOT_NAME, app
from Hero.Utilities.changers import time_to_seconds
from Hero.Utilities.download import get_formats, get_type

user_time = {}
flex = {}

__MODULE__ = "G-ban"
__HELP__ = """

**ɴᴏᴛᴇ:**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.

`/gban` [Kullanıcı Adı Veya Mesaj Yanıtlama]
- Belirlenen Kullanıcıyı Botun Yönetici Olduğu Gruplardan Yasaklar Ve Botu Kullanamaz Hale Gelir.

`/ungban` [Kullanıcı Adı Veya Mesaj Yanıtlama]
- Yasaklanmış Kullanıcının Yasağını Kaldırır.
"""


@app.on_callback_query(filters.regex("close"))
async def closed(_, query: CallbackQuery):
    await query.message.delete()
    await query.answer()


@app.on_callback_query(filters.regex(pattern=r"down"))
async def down(_, CallbackQuery):
    await CallbackQuery.answer()


@app.on_callback_query(filters.regex(pattern=r"gets"))
async def getspy(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    type, videoid, user_id = callback_request.split("|")
    key = await get_formats(CallbackQuery, videoid, user_id, type)
    try:
        await CallbackQuery.edit_message_reply_markup(reply_markup=key)
    except:
        pass


@app.on_callback_query(filters.regex(pattern=r"ytdata"))
async def ytdata(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    type, format, videoid = callback_request.split("||")
    user_id = CallbackQuery.from_user.id
    key = get_type(type, format, videoid, user_id)
    try:
        await CallbackQuery.edit_message_reply_markup(reply_markup=key)
    except:
        pass


inl = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ɪɴᴅɪʀɪʟɪʏᴏʀ...", callback_data=f"down")]]
)

upl = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ʏᴜᴋʟᴇɴɪʏᴏʀ...", callback_data=f"down")]]
)


def inl_mark(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="ɪɴᴅɪʀɪʟᴅɪ ɢᴏɴᴅᴇʀɪʟɪʏᴏʀ...", callback_data=f"down"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️  ɢᴇʀɪ ᴅᴏɴ", callback_data=f"good {videoid}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🗑 ᴍᴇɴᴜʏᴜ ᴋᴀᴘᴀᴛ", callback_data=f"close2"
            ),
        ],
    ]
    return buttons


ytdl_opts = {"format": "bestaudio", "quiet": True}


@app.on_callback_query(filters.regex(pattern=r"boom"))
async def boom(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    type, format_id, videoid = callback_request.split("||")
    mystic = await CallbackQuery.edit_message_text(
        "ɪɴᴅɪʀᴍᴇ ɪsʟᴇᴍɪ ʙᴀsʟᴀᴅɪ...\n\nɪɴᴅɪʀᴍᴇ ɪsʟᴇᴍɪ ʏᴀᴠᴀş ᴏʟᴀʙɪʟɪʀ ʟᴜᴛғᴇɴ ʙᴇᴋʟᴇʏɪɴ...",
        reply_markup=inl,
    )
    yturl = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(yturl, limit=1)
    for result in results.result()["result"]:
        title = result["title"]
        duration = result["duration"]
        views = result["viewCount"]["short"]
        thumb_image_path = result["thumbnails"][0]["url"]
        channel = channel = result["channel"]["name"]
        fetched = f"""
🔍**Parça İndirildi**

🌸**Başlık:** {title}

⏳**Süre:** {duration} Mins
🧿**İzlenme:** `{views}`
🎥**Kanal İsmi:** {channel}
🔗**ᴠɪᴅᴇᴏ ʟɪɴᴋ:** [Link]({yturl})

⚡️ __{MUSIC_BOT_NAME} Tarafından İndirildi__"""
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(), "downloads", str(user_id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    filepath = os.path.join(userdir, filext)
    img = wget.download(thumb_image_path)
    im = Image.open(img).convert("RGB")
    output_directory = os.path.join(os.getcwd(), "search", str(user_id))
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    thumb_image_path = f"{output_directory}.jpg"
    im.save(thumb_image_path, "jpeg")
    width = 0
    height = 0
    if os.path.exists(thumb_image_path):
        metadata = extractMetadata(createParser(thumb_image_path))
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        img = Image.open(thumb_image_path)
        if type == "audio":
            img.resize((320, height))
        elif type == "docaudio":
            img.resize((320, height))
        elif type == "docvideo":
            img.resize((320, height))
        else:
            img.resize((90, height))
        img.save(thumb_image_path, "JPEG")
    audio_command = [
        "yt-dlp",
        "-c",
        "--prefer-ffmpeg",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--audio-quality",
        format_id,
        "-o",
        filepath,
        yturl,
    ]
    video_command = [
        "yt-dlp",
        "-c",
        "--embed-subs",
        "-f",
        f"{format_id}+140",
        "-o",
        filepath,
        "--hls-prefer-ffmpeg",
        yturl,
    ]
    loop = asyncio.get_event_loop()
    med = None
    perf = MUSIC_BOT_NAME
    if type == "audio":
        filename = await downloadaudiocli(audio_command)
        med = InputMediaAudio(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
            title=os.path.basename(filename),
            performer=perf,
        )
    if type == "video":
        filename = await downloadvideocli(video_command)
        dur = int(time_to_seconds(duration))
        med = InputMediaVideo(
            media=filename,
            duration=dur,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=fetched,
            supports_streaming=True,
        )
    if type == "docaudio":
        filename = await downloadaudiocli(audio_command)
        med = InputMediaDocument(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
        )
    if type == "docvideo":
        filename = await downloadvideocli(video_command)
        dur = int(time_to_seconds(duration))
        med = InputMediaDocument(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
        )
    if med:
        loop.create_task(
            send_file(
                CallbackQuery, med, filename, videoid, user_id, yturl, channel
            )
        )
    else:
        print("ᴍᴇᴅ ɴᴏᴛ ғᴏᴜɴᴅ")


def p_mark(link, channel):
    buttons = [
        [InlineKeyboardButton(text="ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ", url=f"{link}")],
    ]
    return buttons


async def send_file(
    CallbackQuery, med, filename, videoid, user_id, link, channel
):
    await CallbackQuery.edit_message_text(
        "ᴜᴘʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ...\n\nᴜᴘʟᴏᴀᴅɪɴɢ sᴘᴇᴇᴅ ᴄᴏᴜʟᴅ ʙᴇ sʟᴏᴡ ᴘʟᴇᴀsᴇ ʜᴏʟᴅ oɴ...",
        reply_markup=upl,
    )
    try:
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id, action="upload_document"
        )
        buttons = p_mark(link, channel)
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        buttons = inl_mark(videoid, user_id)
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    try:
        os.remove(filename)
    except:
        pass


import json
import subprocess as sp


def probe(vid_file_path):
    if type(vid_file_path) != str:
        raise Exception("Give ffprobe a full file path of the file")

    command = [
        "ffprobe",
        "-loglevel",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        vid_file_path,
    ]

    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return json.loads(out)


def duration(vid_file_path):
    _json = probe(vid_file_path)

    if "format" in _json:
        if "duration" in _json["format"]:
            return float(_json["format"]["duration"])

    if "streams" in _json:
        # commonly stream 0 is the video
        for s in _json["streams"]:
            if "duration" in s:
                return float(s["duration"])

    raise Exception("duration Not found")


async def downloadvideocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    filename = t_response.split("Merging formats into")[-1].split('"')[1]
    return filename


async def downloadaudiocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()

    return (
        t_response.split("Destination")[-1]
        .split("Deleting")[0]
        .split(":")[-1]
        .strip()
    )
