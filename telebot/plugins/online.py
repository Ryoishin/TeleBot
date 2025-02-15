# Copyright Ryoishin
# For @RyoishinHelp coded by @TeamRyoishin
# Kangers keep credits else I'll take down 🧐

import random
import sys

from ryoishin import ALIVE_NAME
from ryoishin.utils import admin_cmd
from telethon import version

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ryoishin User"

ONLINESTR = [
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**Ryoishin is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Aditya 🇮🇳](tg://user?id=719195224) \n\n**More help -** @RyoishinHelpChat \n\n           [🚧 GitHub Repository 🚧](https://github.com/TeamRyoishin/Ryoishin)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to Ryoishin**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @RyoishinHelpChat \n\n✔️ Created by: [Aditya 🇮🇳](tg://user?id=719195224) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/TeamRyoishin/Ryoishin)",
]


@ryoishin.on(admin_cmd(outgoing=True, pattern="online"))
@ryoishin.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """Greet everyone!"""
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
