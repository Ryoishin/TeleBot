"""Get weather data using OpenWeatherMap
Syntax: .weather <Location>
.wttr <location> """

import io
import time

import aiohttp
from ryoishin.utils import admin_cmd


@ryoishin.on(admin_cmd(pattern="weathers (.*)"))
@ryoishin.on(sudo_cmd(pattern="weathers (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sample_url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    )
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(
            sample_url.format(input_str, Config.OPEN_WEATHER_MAP_APPID)
        )
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await eor(
            event,
            """{}
**Temperature**: {}°С
    __minimium__: {}°С
    __maximum__ : {}°С
**Humidity**: {}%
**wind**: {}m/s
**clouds**: {}hpa
**Sunrise**: {} {}
**Sunset**: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code,
            ),
        )
    else:
        await eor(event, response_api["message"])


@ryoishin.on(admin_cmd(pattern="wttr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "https://wttr.in/{}.png"
    # logger.info(sample_url)
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        # logger.info(response_api_zero)
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(file=out_file)
    await eor(event, input_str)
