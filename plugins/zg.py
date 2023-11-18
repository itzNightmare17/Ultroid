
"""
✘ Commands Available -

• `{i}zg <reply to a user><username/id>`
    Get His Name History of the replied user.
"""
import glob
import io
import os
import secrets
from asyncio import TimeoutError

try:
    import cv2
except ImportError:
    cv2 = None

try:
    from playwright.async_api import async_playwright
except ImportError:
    async_playwright = None
try:
    from htmlwebshot import WebShot
except ImportError:
    WebShot = None

from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantsBots,
    DocumentAttributeVideo,
)

from pyOreo.fns.tools import metadata, translate

from . import (
    HNDLR,
    LOGS,
    OREConfig,
    async_searcher,
    bash,
    check_filename,
    con,
    download_file,
    eor,
    get_string,
)
from . import humanbytes as hb
from . import inline_mention, is_url_ok, json_parser, mediainfo, oreo_cmd

CHAT = "SangMata_beta_bot"

@oreo_cmd(
    pattern="zg( (.*)|$)",
)
async def sangmata_beta(e):
    args = e.pattern_match.group(2)
    reply = await e.get_reply_message()
    if args:
        try:
            user_id = await e.client.parse_id(args)
        except ValueError:
            user_id = args
    elif reply:
        user_id = reply.sender_id
    else:
        return await e.eor("Use this command with reply or give Username/id...")

    lol = await e.eor(get_string("com_1"))
    try:
        async with e.client.conversation(CHAT, total_timeout=15) as conv:
            msg = await conv.send_message(f"allhistory {user_id}")
            response = await conv.get_response()
            if response and "no data available" in response.text.lower():
                await lol.edit("okbie, No records found for this user")
            elif str(user_id) in response.message:
                await lol.edit(response.text)
    except YouBlockedUserError:
        return await lol.edit(f"Please unblock @{CHAT} and try again.")
    except TimeoutError:
        await lol.edit("Bot didn't respond in time.")
    except Exception as ex:
        LOGS.exception(ex)
        await lol.edit(f"Error: {ex}")
    finally:
        await lol.edit(response.text)
        await e.client.send_read_acknowledge(CHAT)