import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN");

name = '';
name_author = '';
name_book = '';
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
    if message.text == "Добавить книгу":        
        keyboard = types.InlineKeyboardMarkup(); 
        key_name_book = types.InlineKeyboardButton(text='Название', callback_data='name_book'); 
        keyboard.add(key_name_book); 
        key_name_author= types.InlineKeyboardButton(text='Автор', callback_data='name_author');
        keyboard.add(key_name_author);
        key_evaluation= types.InlineKeyboardButton(text='Оценка', callback_data='evaluation');
        keyboard.add(key_evaluation);
        key_plot= types.InlineKeyboardButton(text='Краткий сюжет', callback_data='plot');
        keyboard.add(key_plot);
        bot.send_message(message.from_user.id, text="Выбирите пункт:", reply_markup=keyboard);
        bot.register_next_step_handler(message, get_name_book);


def get_name_book(message):
    if message.text == "Название книги":
        global name_book;
        name_book = message.text;


def finish(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "name_book":
        global name_book;
        name_book = message.text;
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        pass


bot.polling(none_stop=True)

