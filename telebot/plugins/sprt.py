# python 3.7.1

"""Available Commands:
.support"""


import asyncio

from ryoishin.utils import admin_cmd


@ryoishin.on(admin_cmd(pattern="(.*)"))
@ryoishin.on(sudo_cmd(pattern="(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "support":
        await eor(event, input_str)
        animation_chars = [
            "Hello,",
            "Hello, do you need support?",
            "Then join the support group.",
            "[Join Now](t.me/RyoishinHelpChat)",
            "[SUPPORT GROUP](t.me/RyoishinHelpChat)",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await eor(event, animation_chars[i % 5])
