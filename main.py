import random
import time
from pyexpat.errors import messages

import requests
import telebot

token = ""
bot = telebot.TeleBot(token)

url = "https://api.telegram.org/bot"

# stickers = []
# @bot.message_handler(content_types=["sticker"])
# def handler(message):
#     sticker_id = message.sticker.file_id
#     stickers.append(sticker_id)
#     bot.send_sticker(message.chat.id, random.choice(stickers))


def get_updates(offset=0):
    result = requests.get(f"{url}{token}/getUpdates?offset={offset}").json()
    return result["result"]

def run():
    updates = get_updates()
    if updates:
        update_id = updates[-1]["update_id"]
    else:
        update_id = 0

    while True:
        time.sleep(2)
        messages = get_updates(update_id + 1)
        for m in messages:
            update_id += m["update_id"]
            if "text" in m["message"]:
                print(f"ID: {m['message']['chat']['id']}")
                print(f"Сообщение: {m['message']['text']}")

#тестовое подключение

if __name__ == '__main__':
    run()
