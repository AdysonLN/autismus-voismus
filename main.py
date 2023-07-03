# Не удалять, базируется на pyTelegramBotAPI (pip install pyTelegramBotAPI)
import random
import telebot

# Сюда токен из @BotFather между кавычек
token = ''
bot = telebot.TeleBot(token)

# Стартуем, только зачем?
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Поиск любителей голосовых сообщений активирован \nУбедись, что выдал мне все права, кожанный мешок'
    bot.reply_to(message, mess, parse_mode='html')
    print('Меня запустил username:', message.from_user.username)
    if message.chat.id < 1:
        print('Меня запустили в конфе:', message.chat.id)
    else:
        print('Айди запустившего:', message.chat.id)

# Когда-нибудь доделается, когда-нибудь
@bot.message_handler(commands=['luckyguy'])
def potd(message):
    bot.reply_to(message, 'В разработке :(')
    print('Релиз функции "счастливого человека" ждет:', message.from_user.username)


# Ругаемся на войсолюбителей
@bot.message_handler(content_types=['voice'])
def voice_trolling(message):
    voice1 = f'Любитель голосовых, уймись'
    voice2 = f'Для кого Кирилл и Мефодий потели ночами?'
    voice3 = f'У нас таких не любят, гений'
    voice4 = f'Я бы с мылом тебе язык помыл :)'
    voice5 = f'Клуб любящих поговорить - два блока вниз'
    voice6 = f'А я смотрю, когда ж ты голосовое запишешь, чтоб тебя поругать'
    voice7 = f'Кожанный мешок, я тебя забаню когда-нибудь, обещаю'
    voice8 = f'Если рот открывать любишь, может, и на текст перейдешь, ок, да?'
    bot.reply_to(message, random.choice([voice1, voice2, voice3, voice4, voice5, voice6, voice7, voice8]))
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def miui_trolling(message):
    list_of_miui = ['miui', 'MIUI', 'мьюай', 'миуи', 'МИУИ', 'МЬЮАЙ', 'МИУЙ', 'миуй', 'мию', 'МИЮ', 'миюай', 'МИЮАЙ']
    for substring in list_of_miui:
        if substring in message.text:
            miuistick = open('sticker/miui.webp', 'rb')
            bot.reply_to(message, 'А почему мне нравятся плохие прошивки?')
            bot.send_sticker(message.chat.id, miuistick)


# @bot.message_handler()
# def get_user_text(message):
# bot.send_message(message.group.id, message, parse_mode='html')


bot.polling(none_stop=True)
