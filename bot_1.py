from aiogram import Bot, Dispatcher, Router, types
from token_1 import TOKEN_my
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F

bot = Bot(token=TOKEN_my)
dp = Dispatcher()
router = Router(name=__name__)

b1 = types.KeyboardButton(text='Money')
b2 = types.KeyboardButton(text='Honey')
kb = types.ReplyKeyboardMarkup(keyboard=[[b1, b2]], resize_keyboard=True)




@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer('hi', reply_markup=kb)

@dp.message(Command(commands='stop'))
async def echo(message: types.Message):
    await message.answer(text='Salamchick')


@dp.message(F.photo)
async def echo(message: types.Message):
    await message.answer('Крутая фотка')


@router.message(F.text(equals='Money'))
async def but_money(message: types.Message):
    await message.answer(text=f'Была нажата кнопка {message}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling(bot, skip_updates=True))

