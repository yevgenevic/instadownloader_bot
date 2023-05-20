import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from insta import instadownloader

logging.basicConfig(level=logging.INFO)

bot_token = 'YOUR TOKEN'
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    first_name = message.from_user.first_name
    caption = f"🙋‍♂ Salom <b>{first_name}</b>, ushbu bot sizga INSTAGRAMDAN <i>reels, photo, post</i> larni yuklab beradi.\n\n" \
              f"⚽ Boshlash uchun link yuboring!\n\n" \
              f"📎 Masalan: https://www.instagram.com/p/Cg45hlHsQb9/"
    await bot.send_photo(
        photo=open('image.jpg', 'rb'),
        caption=caption,
        parse_mode='HTML',
        chat_id=message.chat.id
    )
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)


@dp.message_handler()
async def instagram(message: types.Message):
    link = message.text
    data = instadownloader(link=link)
    if data == 'Bad':
        await bot.send_message(chat_id=message.chat.id, text="Bu url xato")
    else:
        if data['type'] == 'image':
            await bot.send_message(chat_id=message.chat.id, text='Yuklanmoqda')
            await bot.send_photo(
                photo=data['media'],
                caption="@..... Do'stlaringizga ulashing!",
                chat_id=message.chat.id
            )
        elif data['type'] == 'video':
            await bot.send_message(chat_id=message.chat.id, text='Yuklanmoqda ...')
            await bot.send_video(
                video=data['media'],
                caption="@.... Do'stlaringizga ulashing!",
                chat_id=message.chat.id
            )
        elif data['type'] == 'carusel':
            for i in data['media']:
                await bot.send_document(
                    document=i,
                    caption="@... Do'stlaringizga ulashing!",
                    chat_id=message.chat.id
                )
        else:
            await bot.send_message(chat_id=message.chat.id, text="Bu xato url")



async def on_startup(_):
    print('bot ishga tushdi')






if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
