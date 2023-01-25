import asyncio
import time
import logging
from aiogram import Bot, Dispatcher, types
from config import token_bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from handlers import get_all_miners, power_managment, power_pass_set_true, power_pass_check, power_pass_set_false, \
    power_check

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    # filename='whats-log.txt',
    format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s'
)
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
        "/power - manage power options\n" +
        "/check_power - check on/off power\n" +
        "/show - show all miners\n" +
        "/ping - ping network items\n"
        # "/log - read logs"
    )


@dp.message_handler(commands=["power"])
async def cmd_pwer(message: types.Message):
    await message.answer('Power options:   🔌', reply_markup=kb_power_options)


@dp.message_handler(commands=["check_power"])
async def checker_power_all_farm_to_snmp(message: types.Message):
    bot_logger.info('user enter check_power command')
    if power_check() is True:
        await message.answer('Power is On 🟢')
        bot_logger.info('power is on')
    elif power_check() is False:
        await message.answer('Power is Off 🔴')
        bot_logger.info('power is off')
    # this part not work
    elif power_check() is None:
        msg_error = ' ERD-3s api has problem ⚠️'
        await message.answer(msg_error)
        bot_logger.error(msg_error)


# for show cmd
@dp.message_handler(commands=["show"])
async def show_all(message: types.Message):
    bot_logger.info('user enter show all miners command')
    await message.answer('-- all miners --')
    all_miners = get_all_miners()
    for one_miner in all_miners:
        if one_miner is not None:
            await message.answer(one_miner.get_info())
        if one_miner is None:
            await message.answer('miner is not available..')
    await message.answer('-- end --')


# @dp.message_handler(commands=["log"])
# async def download_log_file(message: types.Message):
#     await message.answer('take the log file')
#     # file_path = file.file_path
#     destination = r'C:\Users\Maksik\Documents\whats_monitor\whats-log.txt'


@dp.callback_query_handler(text='on/off')
async def power_manager(callback: types.CallbackQuery):
    bot_logger.info('user enter ON/OFF farm')
    await callback.message.answer('Please input password: 🔑')
    power_pass_set_true()


@dp.message_handler(content_types=['text'])
async def check_password(message: types.Message):
    if message.text == '123' and power_pass_check():
        if power_managment():
            await message.answer('Done ✅')
        else:
            msg_error = ' ERD-3s api has problem ⚠️'
            bot_logger.error(msg_error)
            await message.answer(msg_error)
    elif power_pass_check():
        power_pass_set_false()
        await message.answer('Password incorrect 🚫')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
