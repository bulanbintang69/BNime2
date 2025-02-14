from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 １", url=client.invitelink),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ２", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ３", url = f'https://t.me/tutorial_anime/6'),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ４", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ５", url=client.invitelink2),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ６", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data="close")
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟮", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟", callback_data="about"),
                InlineKeyboardButton(text="𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟭", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟", callback_data="about"),
                InlineKeyboardButton(text="𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 １", url=client.invitelink),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ２", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ３", url = f'https://t.me/tutorial_anime/6'),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ４", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ５", url=client.invitelink2),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ６", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data="close")
            ],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 １", url=client.invitelink),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ２", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ３", url = f'https://t.me/tutorial_anime/6'),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ４", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ５", url=client.invitelink2),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ６", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗧𝗨𝗧𝗢𝗥𝗜𝗔𝗟", callback_data="about"),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️𝐀𝐦𝐛𝐢𝐥 𝐅𝐢𝐥𝐞♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 １", url=client.invitelink),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ２", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ３", url = f'https://t.me/tutorial_anime/6'),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ４", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ５", url=client.invitelink2),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ６", url = f'https://t.me/tutorial_anime/6'),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️𝐀𝐦𝐛𝐢𝐥 𝐅𝐢𝐥𝐞♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 １", url=client.invitelink),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ２", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ３", url = f'https://t.me/tutorial_anime/6'),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ４", url = f'https://t.me/tutorial_anime/6'),
            ],
            [
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ５", url=client.invitelink2),
                InlineKeyboardButton(text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ６", url = f'https://t.me/tutorial_anime/6'),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️𝐀𝐦𝐛𝐢𝐥 𝐅𝐢𝐥𝐞♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return 
