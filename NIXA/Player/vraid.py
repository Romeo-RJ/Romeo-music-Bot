import re
import asyncio

from pyrogram import filters
from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2, IMG_6, SUDO_USERS
from NIXA.inline import stream_markup
from Process.design.thumbnail import thumb
from Process.design.chatname import CHAT_TITLE
from NIXA.filters import command, other_filters
from NIXA.queues import QUEUE, add_to_queue
from NIXA.main import call_py, Test as user
from NIXA.main import bot as NIXA, Test
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch
IMAGE_THUMBNAIL = "https://telegra.ph/file/046a3e53fc04fa3de84e0.jpg"
HNDLR = '/'

def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["videoraid", "vraid"], prefixes=HNDLR))
async def vraid(c: NIXA, m: Message):
    await m.delete()
    replied = m.reply_to_message
    inp = m.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    if replied:
        if replied.video or replied.document:
            loser = await replied.reply("📥 **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ʀᴀɪᴅ ғɪʟᴇ...**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await loser.edit(
                        "» __ᴏɴʟʏ 720, 480, 360 ᴀʟʟᴏᴡᴇᴅ__ \n💡 **ɴᴏᴡ sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ɪɴ 720ᴘ**"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                elif replied.document:
                    songname = replied.document.file_name[:70]
            except BaseException:
                songname = "Video"

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                buttons = stream_markup
                await m.reply_photo(
                    photo=thumbnail,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"» **ʀᴀɪᴅ ɪɴ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🗂 **ɴᴀᴍᴇ:** [{songname}]({link}) | `ᴠɪᴅᴇᴏ`\n💭 **ᴄʜᴀᴛ:** `{chat_id}`\n🧸 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                await loser.edit("🔄 **ᴘʀᴏᴄᴇssɪɴɢ...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(
                        dl,
                        HighQualityAudio(),
                        amaze,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                buttons = stream_markup
                await m.reply_photo(
                    photo=thumbnail,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"🗂 **ʀᴀɪᴅ:** [{songname}]({link}) | `ᴠɪᴅᴇᴏ`\n💭 **ᴄʜᴀᴛ:** `{chat_id}`",
                )
        else:
            if len(m.command) < 2:
                await m.reply_photo(
                     photo=f"{IMG_6}",
                    caption="💬**ᴜsᴀɢᴇ: /vraid (ᴄʜᴀᴛ ɪᴅ @username) ʏᴏᴜʀ ǫᴜᴇʀʏ ʏᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ғɪʟᴇ ᴛᴏ ʀᴀɪᴅ ɪɴ ᴄʜᴀᴛ**"
                    ,
                      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/{GROUP_SUPPORT}"),
                            InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/{UPDATES_CHANNEL}")
                        ],
                        [
                            InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="cls")
                        ]
                    ]
                )
            )
            else:
                loser = await c.send_message(chat_id, "🔍 **sᴇᴀʀᴄʜɪɴɢ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                Q = 720
                amaze = HighQualityVideo()
                if search == 0:
                    await loser.edit("❌ **ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ.**")
                else:
                    songname = search[0]
                    title = search[0]
                    url = search[1]
                    duration = search[2]
                    thumbnail = search[3]
                    userid = m.from_user.id
                    gcname = m.chat.title
                    ctitle = await CHAT_TITLE(gcname)
                    image = await thumb(thumbnail, title, userid, ctitle)
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await loser.edit(f"❌ ʏᴛ-ᴅʟ ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Video", Q
                            )
                            await loser.delete()
                            buttons = stream_markup
                            await m.reply_photo(
                                photo=image,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"» **ʀᴀɪᴅ ɪɴ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🗂 **ɴᴀᴍᴇ:** [{songname}]({url}) | `ᴠɪᴅᴇᴏ`\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🧸 **ᴄʜᴀᴛ:** {chat_id}",
                            )
                        else:
                            try:
                                await loser.edit("🔄 **ᴘʀᴏᴄᴇssɪɴɢ...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioVideoPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                        amaze,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                                await loser.delete()
                                buttons = stream_markup
                                await m.reply_photo(
                                    photo=image,
                                    reply_markup=InlineKeyboardMarkup(buttons),
                                    caption=f"🗂 **ʀᴀɪᴅ:** [{songname}]({url}) | `ᴠɪᴅᴇᴏ`\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🧸 **ᴄʜᴀᴛ:** {chat_id}",
                                )
                            except Exception as ep:
                                await loser.delete()
                                await m.reply_text(f"sᴛᴀʀᴛᴇᴅ ʀᴀɪᴅ ᴏɴ {chat_id}")

    else:
        if len(m.command) < 2:
            await m.reply_photo(
                     photo=f"{IMG_6}",
                    caption="💬**ᴜsᴀɢᴇ: /vraid ɢɪᴠᴇ ᴀ ᴛɪᴛʟᴇ ᴏʀ ʀᴇᴘʟɪᴇᴅ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴛᴏ ʀᴀɪᴅ ɪɴ ᴀ ᴄʜᴀᴛ**"
                    ,
                      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/{GROUP_SUPPORT}"),
                            InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/{UPDATES_CHANNEL}")
                        ],
                        [
                            InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="cls")
                        ]
                    ]
                )
            )
        else:
            loser = await c.send_message(chat_id, "🔍 **sᴇᴀʀᴄʜɪɴɢ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            amaze = HighQualityVideo()
            if search == 0:
                await loser.edit("❌ **ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ.**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                image = await thumb(thumbnail, title, userid, ctitle)
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await loser.edit(f"❌ ʏᴛ-ᴅʟ ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await loser.delete()
                        buttons = stream_markup
                        await m.reply_photo(
                            photo=image,
                            reply_markup=InlineKeyboardMarkup(buttons),
                            caption=f"» **ʀᴀɪᴅ ɪɴ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🗂 **ɴᴀᴍᴇ:** [{songname}]({url}) | `ᴠɪᴅᴇᴏ`\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🧸 **ᴄʜᴀᴛ:** {chat_id}",
                        )
                    else:
                        try:
                            await loser.edit("🔄 **ᴘʀᴏᴄᴇssɪɴɢ...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                    amaze,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await loser.delete()
                            buttons = stream_markup
                            await m.reply_photo(
                                photo=image,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"🗂 **ʀᴀɪᴅ:** [{songname}]({url}) |`ᴠɪᴅᴇᴏ`\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🧸 **ᴄʜᴀᴛ:** {chat_id}",
                            )
                        except Exception as ep:
                            await loser.delete()
                            await m.reply_text(f"sᴛᴀʀᴛᴇᴅ ʀᴀɪᴅ ᴏɴ {chat_id}")


@NIXA.on_message(filters.user(SUDO_USERS) & filters.command(["vraidlive", "vraidstream"], prefixes=HNDLR))
async def raidlive(c: NIXA, m: Message):
    await m.delete()
    chat_id = m.chat.id
    user_id = m.from_user.id

    if len(m.command) < 2:
        await m.reply("» /vraidlive (ᴄʜᴀᴛ ɪᴅ ᴏʀ @Username) ᴛʜᴇɴ ɢɪᴠᴇ ᴍᴇ ᴀ ʟɪᴠᴇ-ʟɪɴᴋ/m3u8 ᴜʀʟ/ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴛᴏ ʀᴀɪᴅsᴛʀᴇᴀᴍ.")
    else:
        if len(m.command) == 2:
            link = m.text.split(None, 1)[1]
            Q = 720
            loser = await c.send_message(chat_id, "🔄 **ᴘʀᴏᴄᴇssɪɴɢ sᴛʀᴇᴀᴍ...**")
        elif len(m.command) == 3:
            op = m.text.split(None, 1)[1]
            link = op.split(None, 1)[0]
            quality = op.split(None, 1)[1]
            if quality == "720" or "480" or "360":
                Q = int(quality)
            else:
                Q = 720
                await m.reply(
                    "» __ᴏɴʟʏ 720, 480, 360 ᴀʟʟᴏᴡᴇᴅ__ \n» **ɴᴏᴡ sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ɪɴ 720ᴘ**"
                )
            loser = await c.send_message(chat_id, "🔄 **ᴘʀᴏᴄᴇssɪɴɢ ʟɪᴠᴇʀᴀɪᴅ...**")
        else:
            await m.reply("**/vraidlive {link} {720/480/360}**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            veez, livelink = await ytdl(link)
        else:
            livelink = link
            veez = 1

        if veez == 0:
            await loser.edit(f"❌ ʏᴛ-ᴅʟ ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = stream_markup
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"» **ʀᴀɪᴅ ɪɴ ǫᴜᴇᴜᴇ »** `{pos}`\n\n💭 **ᴄʜᴀᴛ:** `{chat_id}",
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                try:
                    await loser.edit("🔄 **ᴘʀᴏᴄᴇssɪɴɢ...**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            livelink,
                            HighQualityAudio(),
                            amaze,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                    await loser.delete()
                    buttons = stream_markup
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=f"» **[__ʟɪᴠᴇ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ__]({link}) **\n\n💭 **ᴄʜᴀᴛ:** `{chat_id}`",
                    )
                except Exception as ep:
                    await loser.delete()
                    await m.reply_text(f"» sᴛᴀʀᴛᴇᴅ ʀᴀɪᴅ ᴏɴ {chat_id}")
