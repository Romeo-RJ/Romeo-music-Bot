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
    "इश्क़ है या कुछ और ये पता नहीं, पर जो तुमसे है किसी और से नहीं 😁😁",
    "मै कैसे कहू की उसका साथ कैसा है, वो एक शख्स पुरे कायनात जैसा है ",
    " तेरा होना ही मेरे लिये खास है, तू दूर ही सही मगर मेरे दिल के पास है ",
    "मुझे तेरा साथ ज़िन्दगी भर नहीं चाहिये, बल्कि जब तक तू साथ है तबतक ज़िन्दगी चाहिए 😖😖",
    "तुझसे मोहब्बत कुछ अलग सी है मेरी, तुझे खयालो में नहीं दुआओ में याद करते है😍😍",
    "तू हज़ार बार भी रूठे तो मना लूँगा तुझे",
    "मगर देख मोहब्बत में शामिल कोई दूसरा ना हो😁😁",
    "किस्मत यह मेरा इम्तेहान ले रही है😒😒",
    "तड़प कर यह मुझे दर्द दे रही है😌😌",
    "दिल से कभी भी मैंने उसे दूर नहीं किया😉😉",
    "फिर क्यों बेवफाई का वह इलज़ाम दे रही है😎😎",
    "मरे तो लाखों होंगे तुझ पर😚😚",
    "मैं तो तेरे साथ जीना चाहता हूँ😫😫",
    "वापस लौट आया है हवाओं का रुख मोड़ने वाला😣😣",
    "दिल में फिर उतर रहा है दिल तोड़ने वाला🥺🥺",
    "अपनों के बीच बेगाने हो गए हैं🥰🥰",
    "प्यार के लम्हे अनजाने हो गए हैं😘😘",
    "जहाँ पर फूल खिलते थे कभी😍😍",
    "आज वहां पर वीरान हो गए हैं🥰🥰",
    "जो शख्स तेरे तसव्वुर से हे महक जाये😁😁",
    "सोचो तुम्हारे दीदार में उसका क्या होगा😒😒",
    "मोहब्बत का एहसास तो हम दोनों को हुआ था",
    "फर्क सिर्फ इतना था की उसने किया था और मुझे हुआ था",
    "सांसों की डोर छूटती जा रही है",
    "किस्मत भी हमे दर्द देती जा रही है",
    "मौत की तरफ हैं कदम हमारे",
    "मोहब्बत भी हम से छूटती जा रही है",
    "समझता ही नहीं वो मेरे अलफ़ाज़ की गहराई",
    "मैंने हर लफ्ज़ कह दिया जिसे मोहब्बत कहते है",
    "समंदर न सही पर एक नदी तो होनी चाहिए",
    "तेरे शहर में ज़िन्दगी कही तो होनी चाहिए",
    "नज़रों से देखो तोह आबाद हम हैं",
    "दिल से देखो तोह बर्बाद हम हैं",
    "जीवन का हर लम्हा दर्द से भर गया",
    "फिर कैसे कह दें आज़ाद हम हैं",
    "मुझे नहीं मालूम वो पहली बार कब अच्छा लगा",
    "मगर उसके बाद कभी बुरा भी नहीं",
    "सच्ची मोहब्बत कभी खत्म नहीं होती",
    "वक़्त के साथ खामोश हो जाती है",
    "ज़िन्दगी के सफ़र में आपका सहारा चाहिए",
    "आपके चरणों का बस आसरा चाहिए",
    "हर मुश्किलों का हँसते हुए सामना करेंगे",
    "बस ठाकुर जी आपका एक इशारा चाहिए",
    "जिस दिल में बसा था नाम तेरा हमने वो तोड़ दिया",
    "न होने दिया तुझे बदनाम बस तेरे नाम लेना छोड़ दिया",
    "प्यार वो नहीं जो हासिल करने के लिए कुछ भी करव दे",
    "प्यार वो है जो उसकी खुशी के लिए अपने अरमान चोर दे",
    "आशिक के नाम से सभी जानते हैं😍😍",
    "इतना बदनाम हो गए हम मयखाने में🥰🥰",
    "जब भी तेरी याद आती है बेदर्द मुझे😍😍",
    "तोह पीते हैं हम दर्द पैमाने में🥰🥰",
    "हम इश्क़ के वो मुकाम पर खड़े है😁😁",
    "जहाँ दिल किसी और को चाहे तो गुन्हा लगता है😒😒",
    "सच्चे प्यार वालों को हमेशा लोग गलत ही समझते है👀👀",
    "जबकि टाइम पास वालो से लोग खुश रहते है आज कल🙈🙈",
    "गिलास पर गिलास बहुत टूट रहे हैं😋😋",
    "खुसी के प्याले दर्द से भर रहे हैं🤨🤨",
    "मशालों की तरह दिल जल रहे हैं🤭🤭",
    "जैसे ज़िन्दगी में बदकिस्मती से मिल रहे हैं😌😌",
    "सिर्फ वक़्त गुजरना हो तो किसी और को अपना बना लेना🤫🤫",
    "हम दोस्ती भी करते है तो प्यार की तरह😊😊",
    "जरूरी नहीं इश्क़ में बनहूँ के सहारे ही मिले😏😏",
    "किसी को जी भर के महसूस करना भी मोहब्बत है😚😚",
    "नशे में भी तेरा नाम लब पर आता है😘😘",
    "चलते हुए मेरे पाँव लड़खड़ाते हैं😍😍",
    "दर्द सा दिल में उठता है मेरे😘😘",
    "हसीं चेहरे पर भी दाग नजर आता है😍😍",
    "हमने भी एक ऐसे शख्स को चाहा😝😝",
    "जिसको भुला न सके और वो किस्मत मैं भी नहीं😜😜",
    "सच्चा प्यार किसी भूत की तरह होता है🥰🥰",
    "बातें तो सब करते है देखा किसी ने नहीं😚😚",
    "मत पूछ ये की मैं तुझे भुला नहीं सकता😝😝",
    "तेरी यादों के पन्ने को मैं जला नहीं सकता😜😜",
    "संघर्ष यह है कि खुद को मारना होगा🥰🥰",
    "और अपने सुकून की खातिर तुझे रुला नहीं सकता😚😚",
    "दुनिया को आग लगाने की ज़रूरत नहीं😎😎",
    "Naale Duniya Sari Ghumawa🙈🙈",
    "तो मेरे साथ चसल आग खुद लग जाएगी💙💙",
    "तरस गये है हम तेरे मुंह से कुछ सुनने को हम🙊🙊",
    "प्यार की बात न सही कोई शिकायत ही कर दे  🙈🙈",
    "तुम नहीं हो पास मगर तन्हाँ रात वही है ❤️❤️",
    "वही है चाहत यादों की बरसात वही है🙈🙈",
    "हर खुशी भी दूर है मेरे आशियाने से ❤️❤️",
    "खामोश लम्हों में दर्द-ए-हालात वही है💫💫",
    "करने लगे जब शिकवा उससे उसकी बेवफाई का😁😁",
    "रख कर होंट को होंट से खामोश कर दिया😆😆",
    "राह में मिले थे हम, राहें नसीब बन गईं😙😙",
    "ना तू अपने घर गया, ना हम अपने घर गये😉😉",
    "तुम्हें नींद नहीं आती तो कोई और वजह होगी😅😅",
    "अब हर ऐब के लिए कसूरवार इश्क तो नहीं😘😘",
    "अना कहती है इल्तेजा क्या करनी😆😆",
    "वो मोहब्बत ही क्या जो मिन्नतों से मिले💕💕",
    "न जाहिर हुई तुमसे और न ही बयान हुई हमसे💓💓",
    "बस सुलझी हुई आँखो में उलझी रही मोहब्बत🥺🥺",
    "गुफ्तगू बंद न हो बात से बात चले🥵🥵",
    "नजरों में रहो कैद दिल से दिल मिले😁😁",
    "है इश्क़ की मंज़िल में हाल कि जैसे😘😘",
    "लुट जाए कहीं राह में सामान किसी का🥰",
    "मुकम्मल ना सही अधूरा ही रहने दो😂😂",
    "ये इश्क़ है कोई मक़सद तो नहीं है🤩🤩",
    "वजह नफरतों की तलाशी जाती है😘😘",
    "मोहब्बत तो बिन वजह ही हो जाती है 😍😍",
    "सिर्फ मरी हुई मछली को ही पानी का बहाव चलाती है 😙😙",
    "जिस मछली में जान होती है वो अपना रास्ता खुद तय करती है",
    "कामयाब लोगों के चेहरों पर दो चीजें होती है 😘😘",
    "एक साइलेंस और दूसरा स्माइल🤔🤔",
    "मेरी चाहत देखनी है तो मेरे दिल पर अपना दिल रखकर देखe😌😌",
    "तेरी धड़कन ना भड्जाये तो मेरी मोहब्बत ठुकरा देना🤫🤫",
    "गलतफहमी की गुंजाईश नहीं सच्ची मोहब्बत में🤪🤪",
    "जहाँ किरदार हल्का हो कहानी डूब जाती है☺️☺️",
    "होने दो मुख़ातिब मुझे आज इन होंटो से अब्बास🤗🤗",
    "बात न तो ये समझ रहे है पर गुफ़्तगू जारी है😶😶",
    "उदासियाँ इश्क़ की पहचान है🤗🤗",
    "मुस्कुरा दिए तो इश्क़ बुरा मान जायेगा😗😗",
    "कुछ इस अदा से हाल सुनाना हमारे दिल😘😘",
    "वो खुद ही कह दे किदी भूल जाना बुरी बात है🥲",
    "माना की उससे बिछड़कर हम उमर भर रोते रहे🤔🤔",
    "पर मेरे मार जाने के बाद उमर भर रोएगा वो😅😅",
    "दिल में तुम्हारी अपनी कभी चोर जायेंगे😁😁",
    "आँखों में इंतज़ार की लकीर छोड़ जायेंगे🙈🙈",
    "किसी मासूम लम्हे मैं किसी मासूम चेहरे से🙉🙉",
    "मोहब्बत की नहीं जाती मोहब्बत हो जाती है😌😌",
    "करीब आओ तो शायद हम समझ लोगे😌😌",
    "ये दूरिया तो केवल फसले बढ़ती है🤫🤫",
    "तेरे इश्क़ में इस तरह मैं नीलाम हो जाओ🤔🤔",
    "आखरी हो मेरी बोली और मैं तेरे नाम हो जाऊ😌😌",
    "आप जब तक रहेंगे आंखों में नजारा बनकर😁😁",
    "रोज आएंगे मेरी दुनिया में उजाला बनकर👅👅",
    "उसे जब से बेवफाई की है मैं प्यार की राह में चल ना सका😅😅",
    "उसे तो किसी और का हाथ थाम लियाबस फिर कभी सम्भल नहीं सका👅👅",
    "एक ही ख़्वाब देखा है कई बार मैंने🤬🤬",
    "तेरी शादी में उलझी है चाहिए मेरे घर की😈😈",
    "तुम्हे मेरी मोहब्बत की कसम सच बताना😎😎",
    "गले में डाल कर बाहें किससे सीखाया है😍😍",
    "नहीं पता की वो कभी मेरी थी भी या नहीं😋😋",
    "मुझे ये पता है बस की माई तो था उमर बस उसी का रहा😌😌",
    "तुमने देखा कभी चाँद से पानी गिरते हुएe😏😏",
    "मैंने देखा ये मंज़र तू में चेहरा धोते हुए😉😉",
    "ठुकरा दे कोई चाहत को तू हस के सह लेना😊😊",
    "प्यार की तबियत में ज़बर जस्ती नहीं होती😉😉",
    "तेरा पता नहीं पर मेरा दिल कभी तैयार नहीं होगा😌😌",
    "मुझे तेरे अलावा कभी किसी और से प्यार नहीं होगा😍😍",
    "दिल में आहट सी हुई रूह में दस्तक गूँजी🤫🤫",
    "किस की खुशबू ये मुझे मेरे सिरहाने आई😁😁",
    "उम्र भर लिखते रहे फिर भी वारक सदा रहा😏😏",
    "जाने किया लफ्ज़ थे जो हम लिख नहीं पाये😌😌",
    "लगा के फूल हाथों से उसने कहा चुपके से😶😶",
    "अगर यहाँ कोई नहीं होता तो फूल की जगह तुम होते😆😆",
    "जान जब प्यारी थी मरने का शौक था🥵🥵",
    "अब मरने का शौक है तो कातिल नहीं मिल रहा🤫🤫",
    "सिर्फ याद बनकर न रह जाये प्यार मेरा🥲🥲",
    "कभी कभी कुछ वक़्त के लिए आया करो😎😎",
    "मुझ को समझाया ना करो अब तो हो चुकी हूँ मुझ मैं😌😌",
    "मोहब्बत मशवरा होती तो तुम से पूछ लेता😁😁",
    "उन्हों ने कहा बहुत बोलते हो अब क्या बरस जाओगे😂😂",
    "हमने कहा जिस दिन चुप हो गया तुम तरस जाओ गए😶😶",
    "कुछ ऐसे हस्दे ज़िन्दगी मैं होते है🤔🤔",
    "के इंसान तो बच जाता है मगर ज़िंदा नहीं रहता😂💓",
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


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%slr(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
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


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdlr(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
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
    
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdslr(?: |$)(.*)" % hl))
async def _(event):
   usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Deadly = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Deadly) == 3:
             user = str(Deadly[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in DEADLYSPAM:
                    text = f"I can't raid on @deadly_spam_bot's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Deadly[1])
                 sleeptimet = sleeptimem = float(Deadly[0])
                 for _ in range(counter):
                      reply = random.choice(LOVEOP)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in DEADLYSPAM:
                       text = f"I can't raid on @deadly_spam_bot's Owner"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"This guy is a owner Of this Bots."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This guy is a sudo user."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Deadly[0])
                   counter = int(Deadly[1])
                   for _ in range(counter):
                        reply = random.choice(LOVEOP)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
