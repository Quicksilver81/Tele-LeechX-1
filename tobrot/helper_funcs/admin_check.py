#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | MaxxRider | 5MysterySD | Other Contributors 
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

from pyrogram import enums
from tobrot import (
    AUTH_CHANNEL,
    DOWNLOAD_LOCATION,
    CLONE_COMMAND_G,
    GLEECH_COMMAND,
    GLEECH_UNZIP_COMMAND,
    GLEECH_ZIP_COMMAND,
    LEECH_COMMAND,
    LEECH_UNZIP_COMMAND,
    LEECH_ZIP_COMMAND,
    LOGGER,
    YTDL_COMMAND,
    GPYTDL_COMMAND,
    PYTDL_COMMAND,
    STATUS_COMMAND,
    UPDATES_CHANNEL,
    LEECH_LOG,
    BOT_PM,
    EXCEP_CHATS
)

async def AdminCheck(client, chat_id, user_id):
    chat = await client.get_chat(chat_id)
    if chat.type == enums.ChatType.PRIVATE and chat_id in AUTH_CHANNEL:
        return True
    SELF = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if SELF.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return False
    else:
        return True
