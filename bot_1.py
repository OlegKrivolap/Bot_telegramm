from aiogram.methods.answer_callback_query import AnswerCallbackQuery
from aiogram import Bot, Dispatcher, Router, types
from token_1 import TOKEN_my
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F

bot = Bot(token=TOKEN_my)
dp = Dispatcher()
router = Router()

buttons = [types.KeyboardButton(text='Money'),
           types.KeyboardButton(text='Honey')
           ]
kb = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)

buttons_1 = [
    types.InlineKeyboardButton(text='Super', callback_data='send'),
    types.InlineKeyboardButton(text='Puper', url='https://www.youtube.com/watch?v=ce1idtN6-wQ&t=3493s')
]

inkb = types.InlineKeyboardMarkup(inline_keyboard=[[*buttons_1]])

rmkb = types.ReplyKeyboardRemove()



@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer('hi', reply_markup=kb)

@dp.message(Command(commands='stop'))
async def echo(message: types.Message):
    await message.answer(text='До свидания', reply_markup=rmkb)


@dp.message(F.text == 'button')
async def inly(message: types.Message):
    await message.answer(text='Клава супер',reply_markup=inkb )

@dp.message(F.photo)
async def echo(message: types.Message):
    await message.answer('Крутая фотка')


@dp.message(F.text == 'Money')
async def but_money(message: types.Message):
    await message.answer(text=f'Была нажата кнопка Money')


@dp.callback_query(F.data == 'send')
async def inkey(callback: types.CallbackQuery):
    await callback.message.answer('Наконец-то')
    await callback.answer('Запрос обработан')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling(bot, skip_updates=True))

