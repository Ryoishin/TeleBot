import sys

from ryoishin.utils import admin_cmd
from telethon import __version__, functions


@ryoishin.on(admin_cmd(pattern="mf ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    help_string = """
......................................../´¯/)
......................................,/¯../
...................................../..../
..................................../´.¯/
..................................../´¯/
..................................,/¯../
................................../..../
................................./´¯./
................................/´¯./
..............................,/¯../
............................./..../
............................/´¯/
........................../´¯./
........................,/¯../
......................./..../
....................../´¯/
....................,/¯../
.................../..../
............./´¯/'...'/´¯¯`·¸
........../'/.../..../......./¨¯\
........('(...´...´.... ¯~/'...')
.........\\.................'...../
..........''...\\.......... _.·´
............\\..............(
..............\\.............\\...
    """.format(
        sys.version, __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername, help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string + "\n\n" + s_help_string)
        await event.delete()


@ryoishin.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@ryoishin.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Ryoishin - A Telethon UserBot powered by @UniBorg""")
