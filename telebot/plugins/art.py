# For Ryoishin
# By @AKASH_AM1 and @xditya
# Kangers keep cr eors
from ryoishin import ALIVE_NAME
from ryoishin.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

# @command(outgoing=True, pattern="^.ded$")


@ryoishin.on(admin_cmd(pattern=r"ded"))
@ryoishin.on(sudo_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await eor(
        ded,
        n + " ==             |\n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


M = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)
P = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)
K = r"_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" r"_/﹋\_\n"
G = (
    "........___________________\n"
    "....../ `-___________--_____|] - - - - - -\n"
    " - - ░ ▒▓▓█D \n"
    "...../==o;;;;;;;;______.:/\n"
    ".....), -.(_(__) /\n"
    "....// (..) ), —\n"
    "...//___//\n"
)
D = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
H = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, my friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)


@ryoishin.on(admin_cmd(pattern=r"monster"))
@ryoishin.on(sudo_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await eor(monster, M)


@ryoishin.on(admin_cmd(pattern=r"pig"))
@ryoishin.on(sudo_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    await eor(pig, P)


@ryoishin.on(admin_cmd(pattern=r"kiler"))
@ryoishin.on(sudo_cmd(pattern=r"kiler"))
async def bluedevikiller(kiler):
    await eor(killer, K)


@ryoishin.on(admin_cmd(pattern=r"gun"))
@ryoishin.on(sudo_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    await eor(gun, G)


@ryoishin.on(admin_cmd(pattern=r"dog"))
@ryoishin.on(sudo_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    await eor(dog, D)


@ryoishin.on(admin_cmd(pattern=r"hmf"))
@ryoishin.on(sudo_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf):
    await eor(hmf, H)
