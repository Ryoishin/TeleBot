"""IX.IO pastebin like site
Syntax: .paste"""
import os
from datetime import datetime

import requests
from ryoishin import CMD_HELP
from ryoishin.utils import admin_cmd


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@ryoishin.on(admin_cmd(pattern="paste ?(.*)"))
@ryoishin.on(sudo_cmd(pattern="paste ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.paste <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.paste <long text to include>`"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await eor(
            event,
            "Dogged to [dogbin]({}) in {} seconds. GoTo Original URL: {}".format(
                url, ms, nurl
            ),
        )
    else:
        await eor(event, "Dogged to [dogbin]({}) in {} seconds".format(url, ms))


CMD_HELP.update(
    {"pastebin": ".paste <long text/file/reply>\nUse - Paste it to pastebin."}
)
