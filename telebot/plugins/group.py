from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(outgoing=True, pattern="group"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(
            e,
            "This is my community.\n\n[Channel](http://t.me/giveaways_24hrs)\n\n[Chat Group](https://t.me/giveaways24hrsdiscuss)\n\n[UserBot Tutorial - Ryoishin](https://t.me/RyoishinHelp)\n\n[Ryoishin Chat](https://t.me/RyoishinHelpChat)\n\n[Github](https://github.com/xditya)\n\n[YouTube](https://bit.ly/adityas7)",
        )


CMD_HELP.update({"group": ".group\nUse - None."})
