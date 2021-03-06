import os
import random
from asyncio import sleep

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from . import *
from . import mention

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

FANAN = "<b> π© π¦π’π¨π₯ππ almheb - ππ€΅π πͺ </b>"
VANAN = "<b> βοΈΨ§ΩΩΨ΄Ψ΄ π₯Ίπ </b>"
sts_fanan = "https://telegra.ph/file/50caf0efa9a2453985364.jpg"
sts_fanan2 = "https://telegra.ph/file/dda7dd09f7d697fe92ff6.jpg" 
sts_fanan3 = "https://telegra.ph/file/007f130ef1028d15c3596.jpg"
sts_fanan4 = "https://telegra.ph/file/593c7e83d4eb25f7b0e55.jpg"
sts_fanan5 = "https://telegra.ph/file/48f567da3417c581446dc.jpg"
sts_fanan6 = "https://telegra.ph/file/165c9405bddc89cf818be.jpg"
sts_fanan7 = "https://telegra.ph/file/7217fc9ebe7c92b1e42c3.jpg"
sts_fanan8 = "hhttps://telegra.ph/file/de70edbf7e01440c6e7bd.jpg"
sts_fanan9 = "https://telegra.ph/file/63e1b87537e92c05da46d.jpg"
sts_fanan10 = "https://telegra.ph/file/d58d68c118d862437f66a.jpg"
sts_fanan11 = "https://telegra.ph/file/28c209102abe082b97e99.jpg"
sts_fanan12 = "https://telegra.ph/file/53f4c117abcfc24934337.jpg"
sts_fanan13 = "https://telegra.ph/file/739a13b944c62412e908b.jpg"
sts_fanan14 = "https://telegra.ph/file/291a667b5bc7e7f15895d.jpg"
sts_fanan15 = "https://telegra.ph/file/e83874718d4eb829fc0e7.jpg"
sts_fanan16 = "https://telegra.ph/file/f2683a9c2f6aec9f16850.jpg"
sts_fanan17 = "https://telegra.ph/file/8775bf7b8edde56243897.jpg"
sts_fanan18 = "https://telegra.ph/file/b544499b6853568ce475f.jpg"

ZEED_IMG = sts_fanan or sts_fanan2 or sts_fanan3 or sts_fanan4 or sts_fanan5

@bot.on(admin_cmd(pattern="ΩΨ΄ΩΩΨ±(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ΩΨ΄ΩΩΨ±(?: |$)(.*)", allow_sudo=True))
async def who(event):
    zed = await eor(event, "β")
    replied_user = await get_user(event)
    try:
        ZEED_IMG, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await eor(zed, "..")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            ZEED_IMG,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
    except TypeError:
        await zed.edit(caption, parse_mode="html")


async def get_user(event):
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    ZEED_IMG
    x = random.randrange(1, 18)
    if x == 1:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ₯ΩΨ¬ΩΩ Ψ£ΩΩΩΨ±ΩΩ π₯Ίπ. </b>"
       return sts_fanan, caption
    if x == 2:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΩΩΨ§ΩΨ΄ ΨͺΨ§ΨͺΩΩΨͺΩΨΊ π₯Ίπ. </b>"
       return sts_fanan2, caption
    if x == 3:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ΄Ψ§ΨͺΨ§Ω Ψ£ΩΩΨ³ΩΩ π₯Ίπ. </b>"
       return sts_fanan3, caption
    if x == 4:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ₯ΩΨ¬ΩΩ Ψ£ΩΨͺΨ§Ω Ψ―ΩΨ²ΩΨ§ΨͺΨ§Ω π₯Ίπ. </b>"
       return sts_fanan4, caption
    if x == 5:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ¨ΩΨ±Ψ§Ω Ψ£ΩΨ²Ψ¬ΩΩΨͺ π₯Ίπ. </b>"
       return sts_fanan5, caption
    if x == 6:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ£Ψ±Ψ§Ψ³ Ψ¨ΩΩΩΨͺ Ψ₯ΩΩΨ§ΩΩΩ π₯Ίπ. </b>"
       return sts_fanan6, caption
    if x == 7:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ϊ―Ψ±ΩΨ³ΨͺΩΨ§ΩΩ Ψ±ΩΩΨ§ΩΨ―Ω π₯Ίπ. </b>"
       return sts_fanan7, caption
    if x == 8:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ³ΩΨ±ΩΨ§Ω Ψ΄Ψ§Ω Ψ£ΩΨΊΩΩ π₯Ίπ. </b>"
       return sts_fanan8, caption
    if x == 9:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΨ±Ω Ψ¨ΩΨ±Ψ³ΩΩπ₯Ίπ. </b>"
       return sts_fanan9, caption
    if x == 10:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΨͺΩΩ Ϊ―ΩΩΨ±ΩΨ²π₯Ίπ. </b>"
       return sts_fanan10, caption
    if x == 11:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ΄Ψ§ΩΩΨ― Ϊ―ΩΩΨ§Ψ¨ΩΨ±π₯Ίπ. </b>"
       return sts_fanan11, caption
    if x == 12:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΩΩΩ ΩΩΨ³ΩΩπ₯Ίπ. </b>"
       return sts_fanan12, caption
    if x == 13:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΨ­ΩΨ― Ψ­ΩΨ§ΩΩπ₯Ίπ. </b>"
       return sts_fanan13, caption
    if x == 14:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ΄ΩΨ§Ψ±ΩΨ?ΩΩΨ§Ωπ₯Ίπ. </b>"
       return sts_fanan14, caption
    if x == 15:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ³ΩΩΩ ΩΨ¨ΩΩπ₯Ίπ. </b>"
       return sts_fanan15, caption
    if x == 16:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΩΩΩΨ§Ψ±Ψ―Ω Ϊ―ΩΨ§Ψ¨Ψ±ΩΩ π₯Ίπ. </b>"
       return sts_fanan16, caption
    if x == 17:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ ΩΨ­ΩΨ― Ψ±ΩΩΨΆΨ§Ωπ₯Ίπ. </b>"
       return sts_fanan17, caption
    if x == 18:
       caption = f"<b> {FANAN} </b>\n\n\n"
       caption += f"<b> {VANAN} </b>"
       caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
       caption += f"\n\n<b> βοΈΩΨ¨ΰ’ͺΩΪͺ Ψ²ΩΨ§Ψ¬Ψ¬ ΩΩΩΩ Ψ³ΨΉΩΩΨ― Ψ§ΩΩΨ¬Ψ±Ψ― π₯Ίπ. </b>"
       return sts_fanan18, caption


CMD_HELP.update(
    {
        "ΩΨ΄ΩΩΨ±": """**Ψ§Ψ³Ω Ψ§ΩΨ§ΨΆΨ§ΩΩΩ : **`ΩΨ΄ΩΩΨ±`
**β?β’β Ψ§ΩΨ§ΩΩΨ± β¦**
  β’  `.ΩΨ΄ΩΩΨ±` Ψ¨Ψ§ΩΨ±Ψ― / Ψ§ΩΩΨΉΨ±Ω / Ψ§ΩΨ§ΩΨ―Ω
**β’  Ψ§ΩΨ΄ΩΨ±Ψ­ β’β’ **__Ψ§ΩΩΨ± ΨͺΨ³ΩΩΩΨ© Ψ²ΩΨ¬ΩΩΩ ΩΩΩ ΩΨ΄ΩΩΩΨ±__"""
    }
)
