import requests
import telebot
from beautifulsoup4 import BeautifulSoup

URL = 'https://rostics.ru/promo/crazydays'
API_KEY = '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps'
r = requests.get(URL)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
  bot.send_message(message.chat.id, 'Привет')

bot.polling()
