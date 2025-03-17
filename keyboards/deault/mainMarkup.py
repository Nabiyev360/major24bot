from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔗 Taklif havolani olish")
        ],
        [
            KeyboardButton(text="✅ Natijalarim")
        ]
    ],
    resize_keyboard=True
)
