import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

import Hero
from Hero import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Hero.Core.PyTgCalls.Converter import convert
from Hero.Core.PyTgCalls.Downloader import download
from Hero.Core.PyTgCalls.Tgdownloader import telegram_download
from Hero.Database import (get_active_video_chats, get_video_limit,
                            is_active_video_chat)
from Hero.Decorators.assistant import AssistantAdd
from Hero.Decorators.checker import checker
from Hero.Decorators.logger import logging
from Hero.Inline import (livestream_markup, playlist_markup, search_markup,
                          search_markup2, url_markup, url_markup2)
from Hero.Utilities.changers import seconds_to_min, time_to_seconds
from Hero.Utilities.chat import specialfont_to_normal
from Hero.Utilities.command import commandpro
from Hero.Utilities.stream import start_stream, start_stream_audio
from Hero.Utilities.theme import check_theme
from Hero.Utilities.thumbnails import gen_thumb
from Hero.Utilities.url import get_url
from Hero.Utilities.videostream import start_stream_video
from Hero.Utilities.youtube import (get_yt_info_id, get_yt_info_query,
                                     get_yt_info_query_slider)

from Hero.Utilities.func import mplay_stream, vplay_stream

@app.on_message(
    commandpro(["/p", "/oynat", "/play", "/oynat@{BOT_USERNAME}"]) & filters.group
)
@checker
@logging
@AssistantAdd
async def mplayaa(_, message: Message):    
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "???"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit(
                    "Canl?? Ak???? Oynat??l??yor...M??zik ??almak i??in durdurun"
                )
            else:
                pass
        except:
            pass
        if audio.file_size > 1073741824:
            return await mystic.edit_text(
                "ses dosyas?? boyutu ???????????? mb'den az olmal??d??r"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT:
            return await mystic.edit_text(
                f"s??re s??n??r?? a????ld??\n\izin verilen s??re: {DURATION_LIMIT_MIN} dakika\nal??nan s??re: {duration_min} dakika(s)"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "Given Audio Via Telegram",
            duration_min,
            duration_sec,
            mystic,
        )
    elif video:
        return await message.reply_text("Kullan??m `/oynat` veya `/vplay` sesli sohbette video veya m??zik oynat??r")
    elif url:
        mystic = await message.reply_text("???")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()        
        MusicData = f"M??zik Yay??n?? {videoid}|{duration_min}|{message.from_user.id}"
        return await mplay_stream(message,MusicData)
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**Kullan??m:** `/oynat` [M??zik ad?? veya yt link veya ses dosyas??na yan??t verme]\n\nSesli Sohbette video veya m??zik oynat??r..."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("???")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        MusicData = f"MusicStream {videoid}|{duration_min}|{message.from_user.id}"
        return await mplay_stream(message,MusicData)


@app.on_message(
    commandpro(["/izle", "/vplay", "/izlet", "/vplay@{BOT_USERNAME}"]) & filters.group
)
@checker
@logging
@AssistantAdd
async def vplayaaa(_, message: Message):
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "Bu sohbet grubunda anonim bir y??neticisiniz...\nY??netici haklar??ndan kullan??c?? hesab??na geri d??n??n..."
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        return await message.reply_text("Kullan??m `/play` veya `/izle` Sesli Sohbette Video Veya M??zik Oynat??r")
    elif video:
        limit = await get_video_limit(141414)
        if not limit:
            return await message.reply_text(
                "**video aramalar?? i??in s??n??r tan??mlanmad??**\n\n`/set_video_limit` ile maximum video limitini ayarlayabilirsiniz."
            )
        count = len(await get_active_video_chats())
        if int(count) == int(limit):
            if await is_active_video_chat(message.chat.id):
                pass
            else:
                return await message.reply_text(
                    "??zg??n??m bot, i??lemci y??k?? sorunlar?? nedeniyle yaln??zca s??n??rl?? say??da g??r??nt??l?? g??r????meye izin verir. di??er bir??ok sohbet ??u anda g??r??nt??l?? aramay?? kullan??yor. sese ge??meyi deneyin veya daha sonra tekrar deneyin..."
                )
        mystic = await message.reply_text(
            "???"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit(
                    "??????????s s????????????????????.../ns????????? ????? ?????? ?????????? ??????s?????..."
                )
            else:
                pass
        except:
            pass
        file = await telegram_download(message, mystic)
        return await start_stream_video(
            message,
            file,
            "Given Video Via Telegram",
            mystic,
        )
    elif url:
        mystic = await message.reply_text("???? Url ????leniyor...")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)               
        
        VideoData = f"???????????s??? {videoid}|{duration_min}|{message.from_user.id}"
        return await vplay_stream(message,VideoData,mystic)
    else:        
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**Kullan??m:** `/izle` [Video Ad?? Veya Youtube Link Veya Bir Videoyu Yan??tlama]\n\nSesli Sohbette Video Oynat??r."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("???")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)       
        VideoData = f"???????????s??? {videoid}|{duration_min}|{message.from_user.id}"
        return await vplay_stream(message,VideoData,mystic)
