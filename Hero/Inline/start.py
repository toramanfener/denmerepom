from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Hero import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Düzeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Yetkili Kullanıcılar", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="🗑️ Kapat", callback_data="close"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Ayarlar", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  ** {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Ayarlar", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Eğlence Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Ayarlar", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌺 Resmi kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Ayarlar", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="🌺 Eğlence Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/keyfimusicbot?startgroup=true",
                )
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/keyfimusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Eğlence Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Bir Gruba Ekle ➕",
                    url=f"https://t.me/keyfimusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌺 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Bir Gruba Ekle ➕",
                    url=f"https://t.me/keyfimusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="🌺 Eğlence Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Düzeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖🗑 Kapat", callback_data="close"),
            InlineKeyboardButton(text="🔙 Geri Dön", callback_data="okaybhai"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Ses Düzeyi Sıfırlanıyor 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Düşük Ses", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Orta Düzey ses", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Yüksek Ses", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Çok Yüksek Ses", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Sesi Ayarla 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri Dön", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Sesi Ayarla 🔼", callback_data="AV")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Herkes", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Adminler", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Yetki Kullanıcıların Listesi", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri Dön", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="📡️ ᴜᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 ʀᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 ᴅɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Geri Dön", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons
