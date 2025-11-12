import telebot
from telebot import types

token = "8006928090:AAEsGr5Zrnxfgg-qMml6gSTxLZ-BJi9nc8E"
bot = telebot.TeleBot(token)

buttons = ["button_1", "button_2", "button_3", "button_4", "button_5"]

buttons_per_page = 4

def generate_markup(page=0):

    markup = types.InlineKeyboardMarkup()
    start = page * buttons_per_page
    end = start + buttons_per_page
    for b in buttons[start:end]:
        button = types.InlineKeyboardButton(b, callback_data=b)
        markup.add(button)

    if page > 0:
        page -= 1
        b1 = types.InlineKeyboardButton("<", callback_data=f"page_{page}")
        markup.add(b1)
        # return markup
    if end < len(buttons):
        page += 1
        b2 = types.InlineKeyboardButton(">", callback_data=f"page_{page}")
        markup.add(b2)
    return markup



@bot.message_handler(commands=["start"])
def start(message):
    markup = generate_markup()
    bot.send_message(message.chat.id, "Выберите кнопки", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def query_handler(call):
    if call.data.startswith("page_"):
        _, page = call.data.split("_")
        markup = generate_markup(int(page))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "Выберите элемент:",
            reply_markup=markup
        )



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