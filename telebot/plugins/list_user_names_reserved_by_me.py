# For @UniBorg
# (c) Shrimadhav U K

from ryoishin import CMD_HELP
from ryoishin.utils import admin_cmd
from telethon import functions


@ryoishin.on(admin_cmd(pattern=r"listmyusernames", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "list_user_names_reserved_by_me": ".listmyusernames\nUse - List all usernames you have reserved."
    }
)
