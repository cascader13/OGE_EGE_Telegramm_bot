import telebot
from telebot import types
bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    file = open('grammatick_servis.jpg', 'rb')
    mess = "<b>Привет!</b> Рады приветствовать тебя в нашем боте для помощи в изучении русского языка и подготовке к экзаменам по этому предмету. Что тебя интересует?"
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ОГЭ", callback_data="OGE")
    button2 = types.InlineKeyboardButton("ЕГЭ", callback_data="EGE")
    button3 = types.InlineKeyboardButton("Итоговое собеседование", callback_data="it_sob")
    button4 = types.InlineKeyboardButton("Итоговое сочинение", callback_data="it_soch")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    bot.send_photo(message.chat.id, file, mess, reply_markup=markup, parse_mode='HTML')


@bot.message_handler(commands=['help'])
def help(message):
    mess = "По ссылке ниже ты получишь доступ к словарям и форумам, на которых обсуждаются трудные вопросы языкознания: https://clck.ru/33o2aH"
    bot.send_message(message.chat.id, mess, disable_web_page_preview=True)

@bot.message_handler(commands=['question'])
def question(message):
    mess = "Мы с радостью поможем тебе в кратчайшие сроки! Напиши нам в Telegram: @ts_gramotnyeservisy_bot."
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=["text"])
def message_user(message):
    if message != "/start" and message != "/help" and message != "/question":
        bot.send_message(message.chat.id, "Я ещё не знаю как ответить на эту команду 👾")

@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    data = str(call.data)
    if data == "OGE":
        file = open('oge.jpg', 'rb')
        mess = 'Ниже представлены тематические группы подготовленных нами материалов (в скобках написаны задания ОГЭ, для которых они пригодятся). Каждая ссылка направит тебя в нужную папку на Яндекс.Диск, где ты найдёшь 2 раздела -"Теория" и "Практические задания".\nМы надеемся, что здесь ты найдёшь всю информацию, необходимую для сдачи экзамена. При возникновении любых вопросов отправь команду /question. В качестве дополнительного материала тебе может понадобиться помощь словарей и форумов по русскому языку. Для обращения к ним, отправь команду /help. Удачи в обучении и на сдаче экзамена!✨'
        bot.send_photo(call.message.chat.id, file, mess)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("показат..", callback_data="OGE_Sh")
        markup.add(button1)
        bot.send_message(call.message.chat.id, "⬇", reply_markup=markup)
    if data == "EGE":
        file = open('ege.jpg', 'rb')
        mess = 'Ниже представлены тематические группы подготовленных нами материалов (в скобках написаны задания ЕГЭ, для которых они пригодятся). Каждая ссылка направит тебя в нужную папку на Яндекс.Диск, где ты найдёшь 2 раздела -"Теория" и "Практические задания".\nМы надеемся, что здесь ты найдёшь всю информацию, необходимую для сдачи экзамена. При возникновении любых вопросов отправь команду /question. В качестве дополнительного материала тебе может понадобиться помощь словарей и форумов по русскому языку. Для обращения к ним, отправь команду /help. Удачи в обучении и на сдаче экзамена!✨'
        bot.send_photo(call.message.chat.id, file, mess)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("показат..", callback_data="EGE_Sh")
        markup.add(button1)
        bot.send_message(call.message.chat.id, "⬇", reply_markup=markup)
    if data == "it_sob":
        file = open('it_sob.jpg', 'rb')
        mess = 'Для успешной сдачи итогового собеседования мы приготовили тебе материалы, представленные ниже. Каждая ссылка направит тебя в нужную папку на Яндекс.Диск.\n🔹Теоретические материалы - https://clck.ru/33pQxi\n🔹Список вариантов прошлых лет - https://clck.ru/SGukh\nМы надеемся, что здесь ты найдёшь всю информацию, необходимую для сдачи экзамена. При возникновении любых вопросов отправь команду /question. В качестве дополнительного материала тебе может понадобиться помощь словарей и форумов по русскому языку. Для обращения к ним, отправь команду /help. Удачи в обучении и на сдаче экзамена!'
        bot.send_photo(call.message.chat.id, file, mess)
    if data == "it_soch":
        file = open('it_soch.jpg', 'rb')
        mess = 'Для успешного написания итогового сочинения мы приготовили тебе материалы, представленные ниже. Каждая ссылка направит тебя в нужную папку на Яндекс.Диск.\n🔹Теоретические материалы - https://clck.ru/33pR49\n🔹Список тем прошлых лет - https://clck.ru/33pR49\nМы надеемся, что здесь ты найдёшь всю информацию, необходимую для сдачи экзамена. При возникновении любых вопросов отправь команду /question. В качестве дополнительного материала тебе может понадобиться помощь словарей и форумов по русскому языку. Для обращения к ним, отправь команду /help. Удачи в обучении и на сдаче экзамена!'
        bot.send_photo(call.message.chat.id, file, mess)
    if data == "OGE_Sh":
        mess = '🔹Изложение (задание 1) - https://clck.ru/33pR5P\n🔹Синтаксис (задание 2,4) - https://clck.ru/33pR8b\n🔹Пунктуация (задание 3) - https://clck.ru/33pR9g\n🔹Орфография (задание 5) - https://clck.ru/33pRBT\n🔹Анализ содержания текста (задание 6) - https://clck.ru/33pRDL\n🔹Средства выразительности (задание 7) - https://clck.ru/33pREe\n🔹Лексический анализ (задание 8) - https://clck.ru/33pRFh\n🔹Сочинение (задание 9) - https://clck.ru/33pRGf'
        bot.send_message(call.message.chat.id, mess, disable_web_page_preview=True)
    if data == "EGE_Sh":
        mess = '🔹Стилистика (задания 1-3) - https://clck.ru/33pbRi\n🔹Орфоэпия (задание 4) -  https://clck.ru/33pZGi\n🔹Лексические нормы (задания 5-6) -  https://clck.ru/33pbML\n🔹Грамматика (задания 7-8) -  https://clck.ru/33pbHU\n🔹Орфография (задания 9-15) -  https://clck.ru/33pbP5 \n🔹Пунктуация (задания 16-21) -  https://clck.ru/33pbPm \n🔹Работа с текстом (задания 22-26) - https://clck.ru/33pbQX\n🔹Сочинение (задание 27) - https://clck.ru/33pZbD'
        bot.send_message(call.message.chat.id, mess, disable_web_page_preview=True)

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)