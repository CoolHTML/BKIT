import telebot
from telebot import types

bot = telebot.TeleBot('1950557144:AAGkgcjdtkmmyT3p43izeRNwDtsZgU2Y1P8')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '''Добро пожаловать. ✌
        ''',
        reply_markup=keyboard())


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('/geophone')
    markup.add(btn1)
    btn2 = types.KeyboardButton('/echo')
    markup.add(btn2)
    return markup
@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_echo = types.KeyboardButton(text="/Эхо")
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo,button_echo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)

@bot.message_handler(commands=['echo'])
def t_s_n(message):
    bot.send_message(message.chat.id,send_number())

def send_number():
    return 2+2






if __name__ == "__main__":
    bot.polling(none_stop=True)
    reply_markup = keyboard()