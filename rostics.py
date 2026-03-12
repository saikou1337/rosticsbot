import requests
import telebot
from bs4 import BeautifulSoup

API_KEY = '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps'
bot = telebot.TeleBot(API_KEY)
def parser():
  URL = 'https://rostics.ru/promo/crazydays'
  
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, 'html.parser')
  
  akciya = soup.find('h1', class_='Nq_zsMVbqV3').text.strip()


@bot.message_handler(commands=['начать'])
def hello(message):
  bot.send_message(message.chat.id, akciya)

bot.polling()




import requests
import telebot
from bs4 import BeautifulSoup
import os

API_KEY = os.environ.get('TELEGRAM_BOT_TOKEN', '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps')
bot = telebot.TeleBot(API_KEY)
def parser():
    URL = 'https://rostics.ru/promo/crazydays'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    element = soup.find('h1', class_='Nq_zsMVbqV3')
  
@bot.message_handler(commands=['начать'])
def hello(message):
    akciya = parser()
    bot.send_message(message.chat.id, akciya)
bot.polling()
