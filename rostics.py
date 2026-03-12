import requests
import telebot
from bs4 import BeautifulSoup

URL = 'https://rostics.ru/promo/crazydays'
API_KEY = '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps'

def parser(URL):
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, 'html.parser')
  akciya = soup.find_all('h1', class_='Nq_zsMVbqV3')
  return [c.text for c in akciya]

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
  bot.send_message(message.chat.id, akciya)

bot.infinity_polling()
