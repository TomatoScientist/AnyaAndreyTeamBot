import telebot
from telebot import types

token = "8298950837:AAHremcLil5IbzqOEtp9migwNdhrkOKq05I"
bot = telebot.TeleBot(token)

buttons = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4", "кнопка 5"]

buttons_per_page = 4
page = 0
def generate_markup():
    global page
    m = types.InlineKeyboardMarkup()
    start = page * buttons_per_page
    end = start * buttons_per_page
    for b in buttons[start:end]:
        button = types.InlineKeyboardButton(b, callback_data=b)

    if page > 0:
        page -= 1
        b1 = types.InlineKeyboardButton("<", callback_data=f"page_{page}")
        m.add(b1)
        return m
    if end < len(buttons):
        page += 1
        b2 = types.InlineKeyboardButton(">", callback_data=f"page_{page}")
        m.add(b2)
        return m



@bot.message_handler(commands=["start"])
def start(message):
    markup = generate_markup()
    bot.send_message(message.chat.id, "Выберите кнопки", reply_markup=markup)



# @bot.message_handler(commands=["start"])
# def start_message(message):
#
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     button_1 = types.KeyboardButton("Поспать")
#     button_2 = types.KeyboardButton("Покушать")
#     keyboard.add(button_1, button_2)
#
#     bot.send_message(message.chat.id, "Выберите кнопки", reply_markup=keyboard)


# @bot.message_handler(func=lambda message: True)
# def handle(message):
#     if message.text == "Поспать":
#         bot.send_message(message.chat.id, "Поспи")

#InlineQueryResultArticle — это один из типов результата
@bot.inline_handler(lambda query: True)
def inline_query(query):
    try:
        results = [
            types.InlineQueryResultArticle(
                id="1",
                title="Привет",
                description="Отправить приветствие",
                input_message_content=types.InputTextMessageContent("Привет от бота!")
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="Цитата",
                description="Мудрая мысль",
                input_message_content=types.InputTextMessageContent("Самое лучшее время посадить дерево было 20 лет назад...")
            )
        ]
        bot.answer_inline_query(query.id, results, cache_time=1)
    except Exception as e:
        print(e)

bot.polling(non_stop=True)