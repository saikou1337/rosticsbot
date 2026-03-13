import requests
import telebot
from bs4 import BeautifulSoup

URL = 'https://rostics.ru/promo'
API_KEY = '8602811245:AAEYXcNpGMH9WUmT57qC_YAKUAJewdDJ3Ps'
bot = telebot.TeleBot(API_KEY)
def parser():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    element = soup.find('h1', class_='_1-7Ufy1g4eD h1')
    return [c.text for c in element]
  
@bot.message_handler(commands=['5050'])
def action(message):
    akciya = parser()
    bot.send_message(message.chat.id, akciya[0])
    
bot.polling()
