from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def choose_hand_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("Камень",callback_data="hand:stone"),
        InlineKeyboardButton("Ножницы",callback_data="hand:scissors"),
        InlineKeyboardButton("Бумага",callback_date="hand:paper"),
    )
    return btn