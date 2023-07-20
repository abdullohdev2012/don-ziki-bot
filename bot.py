import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import * 
from aiogram.types import *
from keyboards import *
import random

logging.basicConfig(level=logging.INFO)

BOT_TOKEN="5965513698:AAHKpQXm0NxohEE2_slxRn67nDmilnVpX8k"

hands = ["stone", "scissors","paper"]
hands_emoji = {
    "stone": "👊",
    "scissors": "✌️",
    "paper": "🤚",
}
bot_choose = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message: Message):
    await message.answer("Привет я бот Зики")

@dp.message_handler(commands=["game"])
async def start_bott(message: Message):
    global bot_choose
    btn = await choose_hand_btn()
    bot_choose = random.choice(hands)
    await message.answer("Tanlang: ", reply_markup=btn)

@dp.callback_query_handler(text_contains="hand:")
async def check_hands(call: CallbackQuery):
    user_choose = call.data.split(":")[1]
    # [hand, stone]
    # hand:stone

    if user_choose == bot_choose:
        await call.message.edit_text(f"Bir xil!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
    elif user_choose == 'stone':
        if bot_choose == 'scissors':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")

    elif user_choose == 'scissors':
        if bot_choose == 'paper':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
    
    elif user_choose == 'paper':

        if bot_choose == 'stone':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")

if name=="main":
    executor.start_polling(dp)