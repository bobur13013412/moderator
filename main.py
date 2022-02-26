import logging
from aiogram import Bot, Dispatcher, executor, types


import config as cfg
import markups as nav


logging.basicConfig(level=logging.INFO)
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def on_user_joined(message: types.Message):
    await message.delete()

def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'


@dp.message_handler(content_types=['new_chat_members'])
async def user_joined(message: types.Message):
    await message.answer("Salom bizning chat guruhimizga xush kelibsiz!\nGuruhda yozish uchun bizning kanalimizga a\'zo bo\'lib qo\'ying",reply_markup=nav.channelMenu)

@dp.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
async def delete(message):
    await message.delete(message.chat.id, message.message_id)


@dp.message_handler()
async def mess_handler(message:types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=cfg.CHANNEL_ID, user_id=message.from_user.id)):
        text = message.text.lower()
        for word in cfg.WORDS:
            if word in text:
                await message.delete()
    else:
        await message.answer("Xabar yozish uchun kanalga a\'zo bo\'ling",reply_markup=nav.channelMenu)
        await message.delete()
asyncio.run(main())
