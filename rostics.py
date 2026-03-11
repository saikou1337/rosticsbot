import requests
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://rostics.ru/promo/crazydays'
API_KEY = '8630240850:AAE3FTuNZOnariyGKFHYwG9BksFLZmnOc14'
r = requests.get(URL)

bot = telebot.TeleBot(API_KEY)
@bot.message.handler(commands=['начать'])

def hello(message):
  bot.send_message(message.chat.id, 'Привет')

bot.polling()
