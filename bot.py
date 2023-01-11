import asyncio
import time
import logging
from aiogram import Bot, Dispatcher, types
from config import token_bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from handlers import get_all_miners, power_managment, password_handler

logging.basicConfig(level=logging.INFO)
bot_logger = logging.getLogger('[bot_logger]')
bot = Bot(token=token_bot)
dp = Dispatcher(bot)

# buttons
button_reset_all = KeyboardButton('Reset all miners')
button_turn_off = InlineKeyboardButton('Press on/off all miners', callback_data='on/off')
button_yes = InlineKeyboardButton('Yes', callback_data='yes')
button_no = InlineKeyboardButton('No', callback_data='no')

kb_power_options = InlineKeyboardMarkup().add(button_turn_off)

kb_yes_or_no = InlineKeyboardMarkup().add(button_yes, button_no)


@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    bot_logger.info('user enter help command')
    await message.answer(
        "Actions for asic farm:\n" +
        "/power - for manage power options\n" +
        "/show - show all miners\n" +
        "/ping - ping network items"
    )


#  cmd for power func
@dp.message_handler(commands=["power"])
async def cmd_pwer(message: types.Message):
    await message.answer('Power options:   🔌', reply_markup=kb_power_options)


# for show cmd
@dp.message_handler(commands=["show"])
async def show_all(message: types.Message):
    bot_logger.info('user enter show all miners command')
    await message.answer('-- all miners --')
    all_miners = get_all_miners()
    for one_miner in all_miners:
        await message.answer(one_miner.get_info())
    await message.answer('-- end --')


@dp.callback_query_handler(text='on/off')
async def power_manager(callback: types.CallbackQuery):
    # await message.answer('ON/OFF')
    bot_logger.info('user enter ON/OFF farm')
    await callback.message.answer('Please input password: 🔑')
    dp.register_callback_query_handler(check_password)
    #
    # if not power_managment():
    #     msg_error = ' ⚠️ ERD-3s api has problem ⚠️'
    #     bot_logger.error(msg_error)
    #     await callback.message.answer(msg_error)
    # await callback.message.answer('- done -')


@dp.message_handler()
async def check_password(message: types.Message):
    bot_logger.info('check_pass')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
