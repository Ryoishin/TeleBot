# credits: SNAPDRAGON (@s_n_a_p_s)
import asyncio
import time

from ryoishin.utils import admin_cmd


@ryoishin.on(
    admin_cmd(
        pattern="webupload ?(.+?|) (?:--)(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles)"
    )
)
@ryoishin.on(
    sudo_cmd(
        pattern="webupload ?(.+?|) (?:--)(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    await eor(event, "Processing ...")
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await bot.download_media(reply.media, Var.TEMP_DOWNLOAD_DIRECTORY)
    event.message.id
    CMD_WEB = {
        "anonfiles": 'curl -F "file=@{}" https://anonfiles.com/api/upload',
        "transfer": 'curl --upload-file "{}" https://transfer.sh/{os.path.basename(file_name)}',
        "filebin": 'curl -X POST --data-binary "@test.png" -H "filename: {}" "https://filebin.net"',
        "anonymousfiles": 'curl -F file="@{}" https://api.anonymousfiles.io/',
        "megaupload": 'curl -F "file=@{}" https://megaupload.is/api/upload',
        "bayfiles": '.exec curl -F "file=@{}" https://bayfiles.com/api/upload',
    }
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except KeyError:
        await eor(event, "Invalid selected Transfer")
    cmd = selected_one
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await eor(event, f"{stdout.decode()}")
