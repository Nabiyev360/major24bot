from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from create_bot import bot
from keyboards.inline import follow_btn

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer(text="Assalomu alaykum! Aksiyada qatnashish uchun @Major_Zone kanaliga a'zo bo'ling",
                     reply_markup=follow_btn)
    link = await bot.create_chat_invite_link(chat_id=-1002380405911)

# @start_router.message(Command('start_2'))
# async def cmd_start_2(message: Message):
#     await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
#
#
# @start_router.message(F.text == '/start_3')
# async def cmd_start_3(message: Message):
#     await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')
