import telebot #, os
import random
bot = telebot.TeleBot('8588446042:AAHETasAIx-KNJUvhU5Qc-jjoA09NCugAeM')
oip = ['Экономьте энергию', 'Берегите воду', 'Не разбрасывайте мусор', 'Избегайте пластика', 'Посадите растения и деревья']

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, 'Привет! Я твой помощник по экологии')
    bot.reply_to(message, 'Набери info и выбери информацию, которая тебе нужна')

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, 'Узнай, сколько разлагается мусор разного типа- rft, советы- oik')


@bot.message_handler(commands=['rft'])
def send_rft(message):
    with open('ec1.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, 'Окурок	1–10 лет')
    bot.reply_to(message, 'Пластиковая чашка	50 лет')
    bot.reply_to(message, 'Обувь из натуральной кожи	25–40 лет')
    bot.reply_to(message,'Жестяная банка	до 90 лет')
    bot.reply_to(message, 'Синтетическая одежда	30–40 лет')
    bot.reply_to(message,'Одноразовый подгузник	около 500 лет')
    bot.reply_to(message, 'Пластиковая бутылка	до 1000 лет')
    bot.reply_to(message,'Алюминиевая банка	до 500 лет')
    bot.reply_to(message,'Пластиковый пакет	200–1000 лет')
    bot.reply_to(message,'Резина (покрышки)	до 100 лет')
    bot.reply_to(message,'Стекло	Более 1000 лет')

@bot.message_handler(commands=['oik'])
def send_oik(message):
    with open('ec2.jpg', 'rb') as f1:
        random_oip = random.choice(oip)
        bot.send_photo(message.chat.id, f1)
        bot.reply_to(message,random_oip)
bot.polling()