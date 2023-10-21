from aiogram import types


def reply_keyboard():
    buttons = [types.KeyboardButton(text='Каталог 1'),
               types.KeyboardButton(text='Каталог 2'),
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True,)
    return keyboard


def reply_keyboard_1():
    buttons = [types.KeyboardButton(text='Брюки'),
               types.KeyboardButton(text='Топы'),
               types.KeyboardButton(text='Платья'),
               types.KeyboardButton(text='Джинсы'),
               types.KeyboardButton(text='Вернуться в выбор каталога')

               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    return keyboard


def back_catalog_1():
    buttons = [types.KeyboardButton(text='Вернуться в каталог 1'),
               types.KeyboardButton(text='Вернуться в выбор каталога')

               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[*buttons]], resize_keyboard=True)
    return keyboard
def inline_keyboard(price, url):
    buttons_1 = [
                types.InlineKeyboardButton(text=f'{price}', callback_data='discount'),
                types.InlineKeyboardButton(text='Перейти на сайт магазина', url=f'{url}'),]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[*buttons_1]])
    return keyboard


rmkb = types.ReplyKeyboardRemove()




# def test(function):
#     x = function(first='sdsd')
#     print(x)
#
#
#
#
#
# test(reply_keyboard)

