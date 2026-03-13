import requests
import telebot
from bs4 import BeautifulSoup
import os

API_KEY = os.environ.get('TELEGRAM_BOT_TOKEN', '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps')
bot = telebot.TeleBot(API_KEY)
def parser():
    URL = 'https://rostics.ru'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    element = soup.find('div', class_='_14ZQf5wtqxX')
  
@bot.message_handler(commands=['начать'])
def hello(message):
    akciya = parser()
    bot.send_message(message.chat.id, akciya)
bot.polling()
