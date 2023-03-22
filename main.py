import random
from typing import List
from random import randrange
import telebot
from telebot import types
import os

image_folder = '/Users/a1/PycharmProjects/vinishko_bot/ wine'
images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]

WHITE_SWEETY = [
    "Майбах Рислинг Зюсс, Германия.Вино обладает элегантным, гармоничным и сбалансированным вкусом с приятной фруктовой сладостью. Вино с приятным фруктовым ароматом.",
    "Шато Жани Сотерн, Франция. Во вкусе богатство и плотность прекрасно гармонируют со свежестью.",
    "Москато д`Асти, Италия.Во вкусе вина ощущаются ноты сладкого миндаля и специй, персика и белых фруктов. Легкое цветочно-фруктовое послевкусие завершает композицию.В свежем, чистом аромате вина преобладают оттенки белых цветов, цитрусовых, меда акации, миндаля, специй и персика."

    ]

WHITE_SEMI_SWEET = [
    "Лос Сантос Айрен, Испания.Идеальный баланс легких сладких ноток с низким содержанием алкоголя придает этому вину превосходную гармонию вкуса, подчеркиваемую изящным сахарным послевкусием.",
    "Еспириту де Чили Совиньон Блан, Чили. Легкий и освежающий вкус вина с отлично сбалансированной кислотностью развивается в послевкусии оттенками айвы.",
    "Борго Аль Соле, Италия.Легкое и освежающее вино с цветочным вкусом. Бледно-соломенный цвет с золотистыми бликами.Ярко выраженный аромат зеленых яблок."]

token = "6149175223:AAH0kFaZDCKKFJJNJ-Q7Izvi1JemtCGQjZc"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message, messsage=None):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🥂Белое")
    btn2 = types.KeyboardButton("🍷Красное")
    btn100 = types.KeyboardButton("Обратная связь")
    btn101 = types.KeyboardButton("🍾Рандомная бутылочка")
    markup.add(btn1, btn2, btn100, btn101)
    bot.send_message(message.chat.id,
                     "Привет и добро пожаловать! Это бот vinishko_bot. Если ты не знаешь какое вино пить сегодня вечерком, то этот бот поможет тебе! Ответь на пару вопросов и бот подберет тебе интересную бутылочку винца!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Обратная связь")
def handle_button100(message):
    bot.send_message(message.chat.id,
                     text="По вопросам сотрудничества или если у вас есть пожелания - пишите разработчику @mayinyard")


@bot.message_handler(func=lambda message: message.text == "🥂Белое")
def handle_button1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton("Белое сладкое")
    btn4 = types.KeyboardButton("Белое полусладкое")
    btn5 = types.KeyboardButton("Белое сухое")
    btn6 = types.KeyboardButton("Белое полусухое")
    btn777 = types.KeyboardButton("Назад")
    markup.add(btn3, btn4, btn5, btn6, btn777)
    bot.send_message(message.chat.id, text="Выбери вино по сладости:".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "🍷Красное")
def handle_button2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn7 = types.KeyboardButton("Красное сладкое")
    btn8 = types.KeyboardButton("Красное полусладкое")
    btn9 = types.KeyboardButton("Красное сухое")
    btn10 = types.KeyboardButton("Красное полусухое")
    btn777 = types.KeyboardButton("Назад")
    markup.add(btn7, btn8, btn9, btn10, btn777)
    bot.send_message(message.chat.id, text="Выбери вино по сладости:".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Белое сладкое")
def handle_button3(message):
    if message.text == "Белое сладкое":
        bot.send_message(message.chat.id, text="Ты выбрал(а) белое сладкое. Держи рандомную бутылочку")
        bot.send_message(message.chat.id, random.choice(WHITE_SWEETY))


@bot.message_handler(func=lambda message: message.text == "Белое полусладкое")
def handle_button4(message):
    if message.text == "Белое полусладкое":
        photo = open(random.choice(images), 'rb')
        bot.send_photo(message.from_user.id, photo, caption='Ты выбрал(а) белое полусладкое. Держи рандомную бутылочку')


@bot.message_handler(func=lambda message: message.text == "🍾Рандомная бутылочка")
def handle_button101(message):
    if message.text == "🍾Рандомная бутылочка":
        bot.send_message(message.chat.id, text="Держи рандомную бутылочку")
        bot.send_message(message.chat.id, random.choice(WHITE_SEMI_SWEET + WHITE_SWEETY))


bot.polling(True)
