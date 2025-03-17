from aiogram import Router, F
from aiogram.types import Message, ChatMemberUpdated

from data.config import CHANNEL_ID
from create_bot import bot, db
from keyboards.deault.mainMarkup import main_markup


referral_router = Router()


@referral_router.chat_member()
async def on_user_joined(event: ChatMemberUpdated):
    if event.chat.id == CHANNEL_ID:
        new_status = event.new_chat_member.status  # Yangi holat
        old_status = event.old_chat_member.status  # Oldingi holat
        user = event.from_user  # Foydalanuvchi ma’lumotlari

        if old_status in ["left", "kicked"] and new_status == "member":
            welcome_text = (f"🎉 Tabriklaymiz, siz aksiya ishtirokchisiga aylandingiz!\n\n"
                            f"Taklif havolangiz orqali do'stlaringizni kanalga taklif qiling va bepul muzqaymoqlarga ega bo'ling!\n\n")
            await bot.send_message(user.id, welcome_text, reply_markup=main_markup)
            db.update_follower_status(follower_id=user.id, status='subscribed')
            await bot.send_message(chat_id=db.get_inviter(follower_id=user.id)[0],
                                   text=f"✅ Sizning taklifingiz orqali {user.full_name} kanalga qo'shilgani uchun sizga 1 bal taqdim etildi!")

        elif old_status == "member" and new_status in ["left", "kicked"]:
            goodbye_text = f"Sizni yana kutib qolamiz! @Major_Zone"
            await bot.send_message(user.id, goodbye_text)
            db.update_follower_status(follower_id=user.id, status='left')
            await bot.send_message(chat_id=db.get_inviter(follower_id=user.id)[0],
                                   text=f"⭕️ Siz taklif qilgan {user.full_name} kanalni tark etgani uchun sizdan 1 bal olindi!")


@referral_router.message(F.text == "🔗 Taklif havolani olish")
async def get_my_link(msg: Message):
    await msg.answer(f"🥳 <b>Vauv, <a href='t.me/major_zone'>Major</a>da TEKIN MUZQAYMOQ tarqatishyapti!</b> 🍦\n\n"
                     f"🚀 Shoshiling! Atiga 20 do‘stlaringizni taklif qiling va bepul muzqaymoq oling! 🎁\n\n"
                     f"👇 Qatnashish uchun bosing👇 \n"
                     f"t.me/Major24Bot?start={msg.from_user.id}")


@referral_router.message(F.text == "✅ Natijalarim")
async def my_results(msg: Message):
    await msg.answer(f"Siz {db.get_inviter_balls(msg.from_user.id)} ta do'stingizni taklif qildingiz!")