import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from NIXA.queues import QUEUE, add_to_queue, get_queue, clear_queue

from NIXA.main import call_py, bot as NIXA, Test
from config import SUDO_USERS

logging.basicConfig(level=logging.INFO)

HNDLR = '/'

aud_list = [
    "./NIXA/Audio/AUDIO1",
    "./NIXA/Audio/AUDIO2",
    "./NIXA/Audio/AUDIO3",
    "./NIXA/Audio/AUDIO4",
    "./NIXA/Audio/AUDIO5",
    "./NIXA/Audio/AUDIO6",
    "./NIXA/Audio/AUDIO7",
    "./NIXA/Audio/AUDIO8",
]



@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        NIXA = await e.reply_text("**sᴛᴀʀᴛɪɴɢ ʀᴀɪᴅ...**")
        link = f"https://NIXA-robot.github.io/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await NIXA.delete()
            await e.reply_text(f"**» ʀᴀɪᴅɪɴɢ ɪɴ:** {chat.title} \n\n**» ᴀᴜᴅɪᴏ:** {songname} \n**» ᴘᴏsɪᴛɪᴏɴ:** #{pos}")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await NIXA.delete()
            await e.reply_text(f"**» ʀᴀɪᴅɪɴɢ ɪɴ:** {chat.title} \n\n**» ᴀᴜᴅɪᴏ:** {songname} \n**» ᴘᴏsɪᴛɪᴏɴ:** ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ")


@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            await e.reply_text("**» ᴠᴄ ʀᴀɪᴅ ᴇɴᴅᴇᴅ!**")
        except Exception as ex:
            await e.reply_text(f"**ᴇʀʀᴏʀ** \n`{ex}`")
    else:
        await e.reply_text("**» ɴᴏ ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ!**")


@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.pause_stream(chat_id)
            await e.reply_text(f"**» ᴠᴄ ʀᴀɪᴅ ᴘᴀᴜsᴇᴅ ɪɴ:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ᴇʀʀᴏʀ** \n`{e}`")
    else:
        await e.reply_text("**» ɴᴏ ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ!**")


@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.resume_stream(chat_id)
            await e.reply_text(f"**» ᴠᴄ ʀᴀɪᴅ ʀᴇsᴜᴍᴇᴅ ɪɴ {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ᴇʀʀᴏʀ** \n`{e}`")
    else:
        await e.reply_text("**» ɴᴏ ʀᴀɪᴅ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘᴀᴜsᴇᴅ!**")
