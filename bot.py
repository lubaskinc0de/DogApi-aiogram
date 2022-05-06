from aiogram import Bot,Dispatcher,executor,types
from dog_api.dog import DogApi

bot = Bot(token='5128933135:AAGBbc-HXhpUjj7t8aLKqILukMEIbROekoE')

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def get_dog(message: types.Message):
    await message.reply('я тут!')

@dp.message_handler(commands=['dog'])
async def get_dog(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=DogApi.get_dog())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)