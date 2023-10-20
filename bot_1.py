from aiogram import Bot, Dispatcher, Router, types
from token_1 import TOKEN_my
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F
from parcer import our_dict

bot = Bot(token=TOKEN_my)
dp = Dispatcher()
router = Router()

buttons = [types.KeyboardButton(text='Все товары'),
           types.KeyboardButton(text='Джинсы'),
           types.KeyboardButton(text='Топы')]
kb = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)


rmkb = types.ReplyKeyboardRemove()
x = 1

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Какую одежду вы хотите посмотреть ?', reply_markup=kb)


@dp.message(F.text == 'Все товары')
async def all_products(message: types.Message):
    count_for_spis = 1
    for i in our_dict[1:]:
        count_for_spis += 1
        count = 1
        while count < len(i):
            await message.answer_photo(f'{i[count]["picture"]}')
            buttons_1 = [
                types.InlineKeyboardButton(text=f'{i[count]["price"]}', callback_data='o'),
                types.InlineKeyboardButton(text='Перейти на сайт магазина', url=f'{i[count]["url"]}'),

            ]

            inkb = types.InlineKeyboardMarkup(inline_keyboard=[[*buttons_1]])
            await message.answer(text=f'{our_dict[1][count]["name"]}', reply_markup=inkb)
    # await message.answer(text='Нужно ли вам загрузить еще товаров?', reply_markup=kb)
        # @dp.message(F.text == 'Вперед', F.text == 'Назад')
        # def fun_fuc(text):
        #     global x
        #     if not text == 'Вперед':
        #         x -= 1
        #     else:
        #         x += 1
        #     return x

            count += 1
        # x = count
        # z = fun_fuc(input('Следующий или предыдущий?'))
        # count = z

@dp.message(F.text == 'Джинсы')
async def all_products(message: types.Message):
    count = 1
    while count < len(our_dict[1]):
        if 'jeans' in our_dict[1][count]["name"]:
            await message.answer_photo(f'{our_dict[1][count]["picture"]}')
            buttons_1 = [
                types.InlineKeyboardButton(text=f'{our_dict[1][count]["price"]}', callback_data='o'),
                types.InlineKeyboardButton(text='Перейти на сайт магазина', url=f'{our_dict[1][count]["url"]}'),

            ]

            inkb = types.InlineKeyboardMarkup(inline_keyboard=[[*buttons_1]])
            await message.answer(text=f'{our_dict[1][count]["name"]}', reply_markup=inkb)


# @dp.callback_query(F.text == 'name')
# def name_(message: types.Message):


@dp.message(F.text == 'button')
async def inly(message: types.Message):
    await message.answer(text='Клава супер',reply_markup=inkb )


@dp.message(F.text == 'button')
async def inly(message: types.Message):
    await message.answer(text='Клава супер',reply_markup=inkb )


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

