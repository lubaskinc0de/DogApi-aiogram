from aiogram import Bot,Dispatcher,executor,types
from dog_api.dog import DogApi

bot = Bot(token='your_token')

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['dogs'])
async def get_dog(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=DogApi.get_dog())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
