"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3
By : - @Zero_cool7870

"""
import asyncio

from ryoishin import CMD_HELP
from ryoishin.utils import admin_cmd


@ryoishin.on(admin_cmd(pattern=r"meme", outgoing=True))
@ryoishin.on(sudo_cmd(pattern=r"meme", allow_sudo=True))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:]

    await eor(event, "-------------" + memeVar)
    await eor(event, "------------" + memeVar + "-")
    await eor(event, "-----------" + memeVar + "--")
    await eor(event, "----------" + memeVar + "---")
    await eor(event, "---------" + memeVar + "----")
    await eor(event, "--------" + memeVar + "-----")
    await eor(event, "-------" + memeVar + "------")
    await eor(event, "------" + memeVar + "-------")
    await eor(event, "-----" + memeVar + "--------")
    await eor(event, "----" + memeVar + "---------")
    await eor(event, "---" + memeVar + "----------")
    await eor(event, "--" + memeVar + "-----------")
    await eor(event, "-" + memeVar + "------------")
    await eor(event, memeVar + "-------------")
    await eor(event, memeVar)
    await asyncio.sleep(sleepValue)


"""
Bonus : Flower Boquee Generater
usage:- .flower

"""


@ryoishin.on(admin_cmd(pattern=r"flower", outgoing=True))
@ryoishin.on(sudo_cmd(pattern=r"flower", allow_sudo=True))
async def meme(event):
    if event.fwd_from:
        return
    flower = " 🌹"
    sleepValue = 5

    await eor(event, flower + "        ")
    await eor(event, flower + flower + "       ")
    await eor(event, flower + flower + flower + "      ")
    await eor(event, flower + flower + flower + flower + "     ")
    await eor(event, flower + flower + flower + flower + flower + "    ")
    await eor(
        event, flower + flower + flower + flower + flower + flower + flower + "   "
    )
    await eor(
        event,
        flower + flower + flower + flower + flower + flower + flower + flower + "  ",
    )
    await eor(
        event,
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + " ",
    )
    await eor(
        event,
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower,
    )
    await asyncio.sleep(sleepValue)


CMD_HELP.update({"meme": ".meme <x> (x = anyhting)\n.flower"})
