# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

import asyncio
from collections import deque

from ryoishin import CMD_HELP
from ryoishin.utils import admin_cmd


@ryoishin.on(admin_cmd(pattern=r"earth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update({"earth": ".earth\nUse - useless."})
