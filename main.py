from telebot import TeleBot

bot = TeleBot('7027073514:AAGtdGt7s1dFMCyiwlaxpGCV0TKX_Aj48M0')


@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'сообщение')


@bot.message_handler(commands=['vystrel'])
def minustri(message):
    bot.send_message(message.chat.id, 'выберите, против кого вы играете')


@bot.message_handler(commands=['sopernik'])
def sopernik(message):
    bot.send_message(message.chat.id, 'вы будете играть против компьютера')


bot.infinity_polling()