from aiogram import Bot, Dispatcher, types
from token_1 import TOKEN_my
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F
from Data import (select_jeans, conn, select_dress,
                  select_slacks, select_top, select_jumpsuit, select_jacket,
                  select_sweatshirt, select_blouse)
from Key_board import (inline_keyboard, reply_keyboard,
                       reply_keyboard_1,back_catalog_1,rmkb)
import time

bot = Bot(token=TOKEN_my)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    buttons = [types.KeyboardButton(text='Каталог 1'),
               types.KeyboardButton(text='Каталог 2'),
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    await message.answer(text=f'Здравствуйте {message.from_user.first_name}!\n'
                              f'Выберете каталог',
                         reply_markup=reply_keyboard())


@dp.message(F.text == 'Каталог 1')
async def catalog_1(message: types.Message):
    buttons = [types.KeyboardButton(text='Брюки'),
               types.KeyboardButton(text='Топы'),
               types.KeyboardButton(text='Платья'),
               types.KeyboardButton(text='Джинсы'),
               types.KeyboardButton(text='Вернуться в выбор каталога')

               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    await message.answer(text='Пожалуйста выберете какую одежду вы хотите посмотреть', reply_markup=keyboard)


@dp.message(F.text == 'Каталог 2')
async def catalog_2(message: types.Message):
    buttons = [types.KeyboardButton(text='Комбинезоны'),
               types.KeyboardButton(text='Куртки'),
               types.KeyboardButton(text='Толстовки'),
               types.KeyboardButton(text='Блузки'),
               types.KeyboardButton(text='Вернуться в выбор каталога')
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    await message.answer(text='Пожалуйста выберете какую одежду вы хотите посмотреть', reply_markup=keyboard)


@dp.message(F.text == 'Джинсы')
async def jeans(message: types.Message):
    for name, price, picture, url in select_jeans(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Платья')
async def dress(message: types.Message):
    buttons = [types.KeyboardButton(text='Платья часть 2'),
               types.KeyboardButton(text='Вернуться в выбор каталога')
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    for name, price, picture, url in select_dress(conn)[0:6]:
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это не весь ассортимент выбранного вами товара')
    await message.answer(text='Вы можете просмотреть еще платья либо вернуться в каталог', reply_markup=keyboard)


@dp.message(F.text == 'Платья часть 2')
async def dress_part_2(message: types.Message):
    for name, price, picture, url in select_dress(conn)[6:12]:
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара', reply_markup=back_catalog_1())


@dp.message(F.text == 'Топы')
async def Tops(message: types.Message):
    for name, price, picture, url in select_top(conn)[:6]:
        buttons = [types.KeyboardButton(text='Топы часть 2'),
                   types.KeyboardButton(text='Вернуться в выбор каталога')
                   ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это не весь ассортимент выбранного вами товара', reply_markup=keyboard)


@dp.message(F.text == 'Топы часть 2')
async def Tops_2(message: types.Message):
    for name, price, picture, url in select_top(conn)[6:]:
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара', reply_markup=back_catalog_1())


@dp.message(F.text == 'Брюки')
async def pants(message: types.Message):
    for name, price, picture, url in select_slacks(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Комбинезоны')
async def jumpsuit(message: types.Message):
    for name, price, picture, url in select_jumpsuit(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Куртки')
async def jacket(message: types.Message):
    for name, price, picture, url in select_jacket(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Толстовки')
async def sweatshirt(message: types.Message):
    for name, price, picture, url in select_sweatshirt(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Блузки')
async def blouse(message: types.Message):
    for name, price, picture, url in select_blouse(conn):
        await message.answer_photo(photo=f'{picture}', caption=f'{name}',
                                   reply_markup=inline_keyboard(price=price, url=url))
        time.sleep(1)
    await message.answer(text='Это весь ассортимент выбранного вами товара')


@dp.message(F.text == 'Вернуться в выбор каталога')
async def back(message: types.Message):
    await message.answer(text='Выберете каталог', reply_markup=reply_keyboard())


@dp.message(F.text == 'Вернуться в каталог 1')
async def back(message: types.Message):
    await message.answer(text='Выберете каталог', reply_markup=reply_keyboard_1())

@dp.message(Command('stop'))
async def stop(message: types.Message):
    await message.answer(text=f'До свидания {message.from_user.first_name}!', reply_markup=rmkb)


@dp.callback_query(F.data == 'discount')
async def query(callback: types.CallbackQuery):
    await callback.answer(text='К сожаленью скидки в данный момент нету')


if __name__ == '__main__':
    print('[INFO] Бот успешно подключен')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling(bot, skip_updates=True))
