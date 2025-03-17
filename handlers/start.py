from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

from create_bot import bot, db, CHANNEL_ID
from keyboards.inline.buttons import follow_btn
from keyboards.deault.mainMarkup import main_markup


start_router = Router()


async def is_subscribed(user_id: int) -> bool:
    try:
        chat_member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except TelegramBadRequest:
        return False


@start_router.message(CommandStart())
async def cmd_start(msg: Message):
    user_id = msg.from_user.id
    fullname = msg.from_user.full_name
    db.add_user(user_id, fullname, msg.from_user.username)
    if len(msg.text) > 6:
        inviter_id = msg.text.replace('/start ', '')
        follower_id = msg.from_user.id
        if int(inviter_id) == follower_id:
            await msg.answer("Havolani do'stlaringiz bilan ulashing!")
            return
        else:
            db.add_referral(inviter_id, follower_id)
    if await is_subscribed(user_id):
        await msg.answer(text='Asosiy menyu', reply_markup=main_markup)
    else:
        await msg.answer(text=f"Assalomu alaykum {fullname}!\n"
                              f"<b>Aksiyada qatnashish uchun @Major_Zone kanaliga a'zo bo'ling</b>",
                         reply_markup=follow_btn)
