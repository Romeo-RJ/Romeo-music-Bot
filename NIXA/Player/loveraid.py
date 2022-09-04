
import asyncio
import base64
import os
import random        
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from NIXA.data import RAID, REPLYRAID, DEADLYSPAM
from NIXA.main import BOT
from config import SUDO_USERS

OWNER_ID = SUDO_USERS
que = {}
hl = '/'


NUMBER = ["0", "1"]

LOVEOP = [
    "JAANU I LOVE U NA🥺",
    "TU HI HAIN MERI JAAN KISI AUKAT NAI HAIN JO HUMARE BICH ME AAYE🥺😏",
   "SKY IS BLUE I GOT FLU I LOVE TOO🥺",
   "TU HI MERI JAAN HAIN JANUDI🥺",
   "KYU TUMHARE ANKHEN ITNI SUNDAR HAIN🥺",
    "MISS U BABY LOVE BABY I TRUST U BABY🥺",
    "BHAGWAN NE TUMHE MERE LIYE BANAYA HAIN SACHI 🥺",
    "BABY ANKHEN BAND KARO AUR DEKHO KYA DIKH RAHA JO DIKH RAHA HAIN VO MY LIFE WITHOUT 🥺",
    "PATA NAI MERE DOST TUMHE SUBAH SE BHABHI BOL RAHE HAIN SAYAD UNHE HUMARE BARE PATA CHAL GAYA😍",
    "JAAN SE JYADA TUM PYAARI HO BABY🥺",
    "KYA MATLAB TUM MERI HO GYI HO🥺",
    "MERE BACCHON KI MAA BANOGI 🥺",
    "TUNE MERI ZINGADI BANA DI🥺",
    "KYA MATLAB HUM SHADI KAR RAHE HAIN 😍",
    "BABY TUM NA MILI TOH ME FIRSE TRY KARUNGA 😏",
    "YUN TOH KISI CHEEJ KE MOHTAAJ NAI HUM BAS EK TERI AADAT SI HO GAYI HAIN 🥺",
    "KOI NAI THA AUR NA HOGA TERE JITNA TERE KREEB MERE DIL KE😍",
    "TU HI MERI SHAMO SUBAH",
    "TU HI MERI FIRST AND LAST CHOICE🥺😍",
    "TERA HAR ANDAZ PASAND HAI SIWAYE NARAZ ANDAZ KARNE KA🥺😍",
    "TU JAB NARAZ HOTI HAIN TAB MERE DIL KO KUCH KUCH HOTA HAIN🥺",
    "KYU MERE DIL MEIN TUMHARE KHAYAL AATE HAIN🥺",
    "TUNE MERI LIFE AUR DIL KO FIRSE KHUSH KAR DIYA😍",
    "EK DIN NA DEKHON TUJHE TOH MUJHE HURT HOTA HAIN🥺",
    "YE SPAM NAI MERE DIL KE BAATE HAIN TUMHARE LIYE🥺",
    "LIFE KA PATA NAI BUT TUMHARA AUR MERA DIL KA CONNECTION EK HAIN😍",
    "MERE LIYE SABKUCH TUM HO🥺",
    "AGAR TUM CHALI GAYI TOH MERA KYA HOGA🥺",
    "LOVE KARLO BAS EK BAAR FIR KABHI NAI CHHODUNGA🥺",
    "EK BAAR DIL KA CONNECTION EK KARLU FIR SURNAME EK HI HONE WALA HAIN",
    "DIMAAG KA PATA NAI LEKIN DIL TUMHARE PAS LE AAYA 🥺",
    "TU HI MERI JAAN SHAAN DIL KI ARMAAN 🥺❤️",
    "TERI DIL ME JAGAH BANAUNGA AAJ PLEASE MAAN JAO NA 🥺❤️",
    "ME TERA RAJA TU MERI RANI DO MILKE EK PREM KAHANI ❤️",
    "YE LOVE NAI TOH KYA HAIN 🥺❤️",
    "AAJ TAK ME KISIKE SAMNE NAI JHUKA BUT APNE PYAAR KE SAMNE ME HAAR GAYA🥺",
    "KYUN TUJHE ME ITNA CHAHANE LAGA ❤️🥺",
    "PYAAR TOH EK DIL KA PART HAIN AUR TU MERI HAIN",
    "DIMAAG KA PATA NAI LEKIN DIL TUMHARE PAS LE AAYA 🥺",
    "TU KYUN MERE SEEDHA DIL ME AATI HAIN ❤️🥺",
    "DIL AUR DIMAAG EK KAR DUNGA TERKO WIFE BANANE MEIN 🥺❤️",
    "MERI LIFE MEIN PEHLE BOHOT TENSION THI JABSE TUMKO DEKHA MERA PROBLEM SOLVE HO GAYA 🥺",
    "MERI MUMMY TUMHARA GHARPE INTZAAR KAR RAHI HAIN PLEASE AAJAO❤️🥺",
    "HATE ME I DONT CARE",
    "LEAVE ME I DONT CARE",
    "EK TU H TU H RHYGII",
    "TERE BIN MAR JAUNGA",
    "TU MERI H SMJI?",
    "KOI TERE MERE BEECH AYA MARDUNGA OSE",
    "TERE LIYE MAR B SKTA HU MAR B SKTA HU",
    "TERE SE JITNA MRJI GUSSA HO JAUN BUT I LOVE U YARR",
    "TERE LIE IS DUNIA SE LAD JAUNGA",
    "ANKO SE ANKHE MILAKE KHWAB CHURA LU TERE",
    "TERA ISHQ PANE LIE KITNE BETAN HU KESE BATAU TUJE",
    "ME JO JEE RHA HU WAJH TUM HO",
    "TU H TO M HU TUJSE M HU",
    "TUJE KITNA CHAHNE LAGE HAM KI SHBO M BYAN NA KAR PAYNGE",
    "CURRENT STATUS  I WANT TO HUG YOU AND WANAA CARRY LOUD",
    "I NEED YOU IN MY BAD IN MY GOOD",
    "HMESHA TERE SATH HU",
    "TERE SE KADM SE KDM MILAKE CHALNA CHHTA HU",
    "TUJE APNI SHOTI SI DUNIA KA EK BHT BADA HISA BANANA CHAHTA HU",
    "KYA JANE TU MERE IRADHE LE JAUNGA TERI SANSE CHURAKE",
    "DIL KHE RHA KI GUNHGAGAR BAN JA BADA SKOON H IN GUNAHO M",
    "MERI KHUSHNMA SUBH H TU",
    "MERI JAAN H TU",
    "EVEN TUJE IDEA B NHI H KI TERE EK SINGLE MESSAGE KA WAIT KRTE KRTE KITAN ROYA HU",
    "TUJE PANE LIE BHT TDFA HU",
    "KABI KABI LGTA H KI TUN MUJSE NHT DUR JA RHI H",
    "I DONT CARE ABOUT WORD BS I NEED YOU",
    "TUN BAS MERI H MERI RHNA",
    "BHT ROTA HU TERE LIE AKELA ME",
    "H YE NSHA YAN H JEHAR IS PYAR KO KYA NAM DU",
    "HMARE PYAR KI H YE ADHURI DASTA KI TUN PASS HOKE B BHT DOOR H",
    "Doctor Ne Advice Kia Hai Ki Sone Se Pahle Apki Pic Dekh, Kar Sona Jaroori Hai Warna Heart Attack Aa Sakta Hai."
]


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sloveraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Love Raid\n\nCommand:\n\n.loveraid <count> <Username of User>\n\n.loveraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deadly:
                text = f"I can't raid on @deadly_spam_bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DEADLYSPAM:
                text = f"I can't raid on @deadly_spam_bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(LOVEOP)),
            reply_to=event.message.id,
        )


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Love ReplyRaid\n\nCommand:\n\n.lovereplyraid <Username of User>\n\n.lovereplyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in Deadly:
                text = f" can't raid on @deadly_spam_bot's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in DEADLYSPAM:
                text = f" can't raid on @deadly_spam_bot's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdlovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Deactivate Raid\n\nCommand:\n\n.dlovereplyraid <Username of User>\n\n.dlovereplyraid <reply to a User>"
    global que
    if e.sender_id in SUDO_USERS:    
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
