import requests
import telebot
from bs4 import BeautifulSoup
import os

URL = 'https://rostics.ru'
API_KEY = os.environ.get('TELEGRAM_BOT_TOKEN', '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps')
bot = telebot.TeleBot(API_KEY)
def parser():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    element = soup.find('div', class_='_14ZQf5wtqxX')
    return [c.text for c in element]
  
@bot.message_handler(commands=['5050'])
def action(message):
    akciya = parser()
    bot.send_message(message.chat.id, akciya[0])
    
bot.polling()
