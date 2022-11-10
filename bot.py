from aiogram import executor
import config
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import logging

#функции перевода
from googletrans import Translator
import googletrans

translator=Translator()

def translate_func(string,lang):
    return translator.translate(string, dest=str(lang))
#бот

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

global lang
#старт и клавиатура

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Русский','Английский','Французский','Немецкий','Испанский','Португальский','Японский','Китайский']
    keyboard.add(*buttons)
    await message.answer('Я бот-переводчик, я переведу ваш текст на язык из списка',reply_markup=keyboard)

#функции кнопок
@dp.message_handler(lambda message: message.text=='Русский' or message.text=='Английский' or
                    message.text=='Французский' or message.text=='Немецкий' or message.text=='Испанский' or 
                    message.text=='Португальский' or message.text=='Японский' or message.text=='Китайский')
async def ru_eng(message: types.Message):
    global lang
    languages={'Русский':'ru','Английский':'en','Французский':'fr',
                'Немецкий':'de','Испанский':'es','Португальский':'pt',
                'Японский':'ja','Китайский':'zh-cn'}
    lang=languages[message.text]
    await message.reply('Что перевести?')

#перевод
@dp.message_handler()
async def print_res(message:types.Message):
    global lang
    translated = translate_func (message.text,lang)
    await message.reply(translated.text)

#запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
    