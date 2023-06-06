import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN");

name = '';
name_author = '';
name_book = '';
rating = '';
feedback = '';
markup = '';


@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.from_user.id, "Как вас зовут?");
    bot.register_next_step_handler(message, get_name);

@bot.message_handler(content_types=['text'])
def get_name(message):
    global name;
    name = message.text; 
    markup = types.ReplyKeyboardMarkup(row_width=2);
    itembtn1 = types.KeyboardButton('Добавить книгу');
    markup.add(itembtn1);
    bot.send_message(message.from_user.id, "Здравствуйте, " + name + "!", reply_markup=markup);
    bot.register_next_step_handler(message, get_book);

def get_book(message):   
    markup = types.ReplyKeyboardMarkup(row_width=2);
    btn1 = types.KeyboardButton('Название');
    btn2 = types.KeyboardButton('Автор');
    btn3 = types.KeyboardButton('Оценка');
    btn4 = types.KeyboardButton('Краткий сюжет/Впечатление');
    btn5 = types.KeyboardButton('Завершить');
    markup.add(btn1, btn2, btn3, btn4, btn5);
    bot.send_message(message.from_user.id, text="Выбирите пункт:", reply_markup=markup);
    bot.register_next_step_handler(message, book);


def book(message):
    if message.text == "Название":
        bot.register_next_step_handler(message, get_name_book);
    if message.text == "Автор":
        bot.register_next_step_handler(message, get_name_author);
    if message.text == "Оценка":
        bot.register_next_step_handler(message, get_rating);
    if message.text == "Краткий сюжет/Впечатление":
        bot.register_next_step_handler(message, get_feedback);
    if message.text == "Завершить":
        bot.send_message(message.from_user.id, "Название: " + name_book + '\n' + 
                                               "Автор: " + name_author + '\n' + 
                                               "Оценка: " + rating + '\n' + 
                                               "Впечатление: " + feedback + '\n', reply_markup=markup);
        bot.register_next_step_handler(message, get_name);

def get_name_book(message):
    global name_book;
    name_book = message.text;
    bot.register_next_step_handler(message, book);

def get_name_author(message):
    global name_author;
    name_author = message.text;
    bot.register_next_step_handler(message, book);

def get_rating(message):
    global rating;
    rating = message.text;
    bot.register_next_step_handler(message, book);

def get_feedback(message):
    global feedback;
    feedback = message.text;
    bot.register_next_step_handler(message, book);




bot.polling(none_stop=True)

