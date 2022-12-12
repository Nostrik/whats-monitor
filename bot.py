import asyncio
import time
import logging
from aiogram import Bot, Dispatcher, types
from config import token_bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from handlers import get_all_miners

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token_bot)
dp = Dispatcher(bot)

# buttons
button_reset_all = KeyboardButton('Reset all miners')
button_turn_off = KeyboardButton('Turn on/off all miners')
button_yes = InlineKeyboardButton('Yes', callback_data='yes')
button_no = InlineKeyboardButton('No', callback_data='no')

kb_power_options = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_power_options.add(button_reset_all, button_turn_off)

kb_yes_or_no = InlineKeyboardMarkup().add(button_yes, button_no)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "Some actions for asic farm:\n"+
        "/power - for manage power options\n"+
        "/show - show all miners"
    )


#  cmd for power func
@dp.message_handler(commands=["power"])
async def cmd_pwer(message: types.Message):
    await message.answer('-- power options --', reply_markup=kb_power_options)


# for show cmd
@dp.message_handler(commands=["show"])
async def show_all(message: types.Message):
    await message.answer('-- all miners --')
    all_miners = get_all_miners()
    for one_miner in all_miners:
        await message.answer(
            f"Miner type: {one_miner.name}, ip: {one_miner.ip_address}\n"
            f"Errors: {one_miner.error_code}, Up Time: {one_miner.up_time}\n"
            f"Power: {one_miner.power_w}, Hash-rate: {one_miner.ths_rt}\n"
            f"Speed In: {one_miner.speed_in}, Speed out: {one_miner.speed_out}\n"
            f"Temperature: {one_miner.temperature}"
        )
    await message.answer('-- end --')


# handler
@dp.message_handler()
async def handler(message: types.Message):
    if message.text == 'Reset all miners':
        await message.reply('Are you sure?', reply_markup=kb_yes_or_no)
    elif message.text == 'Turn on/off all miners':
        await message.reply('Are you sure?', reply_markup=kb_yes_or_no)


@dp.callback_query_handler(text='yes')
async def sure_handler(message: types.Message):
    await message.answer('you sad yes')


@dp.callback_query_handler(text='no')
async def sure_handler(message: types.Message):
    await message.answer('you sad no')


async def main():
    await dp.start_polling(bot)


def get_miners():
    ...


if __name__ == "__main__":
    asyncio.run(main())
