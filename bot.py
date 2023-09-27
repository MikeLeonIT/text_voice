import logging
from back import update_user
from back.text_to_voice.text_to_voice import voice_handler
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types.web_app_info import WebAppInfo


token = '6392530153:AAEc8dqRIfGZyTfq0YHomRN3P5qoqoZRrAg'
url = 'https://mikeleonit.github.io/'
users = update_user.get_users()
bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
print(users)


@dp.message_handler(commands=['ipm_support'])
async def start(message: types.Message):
    try:
        user_name = message.from_user.first_name + ' ' + message.from_user.last_name if message.from_user.last_name \
            else message.from_user.first_name
        print(message.from_user.id)
        print(users[message.from_user.id])
        if message.from_user.id in users:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('IPM Support', web_app=WebAppInfo(url=url)))
            await message.answer(f"Привет {user_name}", reply_markup=markup)
        else:
            await message.answer(f"{user_name} не является специалистом тех. поддержки")
    except:
        await message.answer("Данная команда должна отправляться непосредственно боту")


@dp.message_handler(text='voice0')
async def start(message: types.Message):
    global users
    print(users)
    if message.from_user.id in users and message.text == 'voice0':
        users[message.from_user.id]['voice_prompt'] = 0
        update_user.update_user(users)
        await message.answer("Голосовой помощник выключен")
    else:
        await message.answer("Вы не являетесь сотрудником тех. поддержки")


@dp.message_handler(text='voice1')
async def start(message: types.Message):
    global users
    print(users)
    if message.from_user.id in users and message.text == 'voice1':
        users[message.from_user.id]["voice_prompt"] = 1
        update_user.update_user(users)
        await message.answer("Голосовой помощник включен. "
                             "\nСообщения озвучиваются автоматически на компе")
    else:
        await message.answer("Вы не являетесь сотрудником тех. поддержки")


@dp.message_handler(text='voice2')
async def start(message: types.Message):
    global users
    print(users)
    if message.from_user.id in users and message.text == 'voice2':
        users[message.from_user.id]['voice_prompt'] = 2
        update_user.update_user(users)
        await message.answer("Голосовой помощник включен. Сообщения приходят в личку")
    else:
        await message.answer("Вы не являетесь сотрудником тех. поддержки")


@dp.message_handler(text='voice-1')
async def start(message: types.Message):
    global users
    print(users)
    if message.from_user.id in users and message.text == 'voice-1':
        users[message.from_user.id]['voice_prompt'] = -1
        update_user.update_user(users)
        await message.answer("Голосовой помощник включен. Работает только на Web")
    else:
        await message.answer("Вы не являетесь сотрудником тех. поддержки")


@dp.message_handler(content_types=['any'])
async def handle_message(message: types.message):
    if message.from_user.id in users:
        if message.text or message.caption:
            print(message)
            data = str(message.forward_date).split()[0].split('-') if message.forward_date else str(message.date).split()[0].split('-')
            data = '.'.join(data[::-1])
            times = str(message.forward_date).split()[-1].split(':')[:2] if message.forward_date else str(message.date).split()[-1].split(':')[:2]
            times = ':'.join(times)
            if message.forward_from_chat:
                label = f"{message.forward_from_chat.title}\n{data}\n{times}\n\n"
            elif message.forward_from:
                label = f"{message.forward_from.first_name + ' ' + message.forward_from.last_name}\n{data}\n{times}\n\n"\
                    if message.forward_from.last_name else f"{message.forward_from.first_name}\n{data}\n{times}\n\n"
            elif message.forward_sender_name:
                label = f"{message.forward_sender_name}\n{data}\n{times}\n\n"
            else:
                label = f"{message.from_user.first_name} {message.from_user.last_name}\n{data}\n{times}\n\n" \
                    if message.from_user.first_name else f"{message.from_user.first_name}\n{data}\n{times}\n\n"
            text1 = ' '
            if message.text:
                text1 = message.text
            text2 = ' '
            if message.caption:
                text2 = message.caption
            result = str(label) + str(text1) + str(text2)
            print(result)
            prompt = users[message.from_user.id]['voice_prompt']
            result = voice_handler(result, prompt)
            if result:
                await bot.send_audio(message.chat.id, open(result, "rb"),
                                     performer=f"{message.from_user.first_name}", title="Отголосок")
    else:
        await message.answer("Иди нахуй")


executor.start_polling(dp)
