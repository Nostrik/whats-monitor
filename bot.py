import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import token_bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.DEBUG)
# Объект бота
bot = Bot(token=token_bot)
# Диспетчер
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


@dp.message_handler(commands=["power"])
async def cmd_pwer(message: types.Message):
    await message.answer('-- power options --', reply_markup=kb_power_options)
    await message.answer('Are you sure?', reply_markup=kb_yes_or_no)


@dp.message_handler(commands=["show"])
async def cmd_pwer(message: types.Message):
    await message.answer('-- all miners --')


async def turn_reset_miners(message: types.Message):
    await message.answer('Reset all miners')
    await message.answer('Are you sure?', reply_markup=kb_yes_or_no)


async def turn_on_of_miners(message: types.Message):
    await message.answer('On/Off all miners')
    await message.answer('Are you sure?', reply_markup=kb_yes_or_no)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())