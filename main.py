import telebot
bot = telebot.TeleBot('5737183803:AAElKWfH6Laq5xgBTsng3dKa5-ow5f_W9JM')
import pyodbc 

cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER={localhost,1433};DATABASE=master;UID=sa;PWD=KekLolOrbidol1347")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Получить данные":
        data = get_data()
        bot.send_message(message.from_user.id, data)
    elif message.text == "Добавить пользователя":
        bot.send_message(message.from_user.id, "Введите имя")
        bot.register_next_step_handler(message, add_new_user);
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def add_new_user(message):
    cursor = cnxn.cursor()
    query = 'INSERT INTO users (name) values (%r)' % (message.text)
    print(query)
    cursor.execute(query)
    bot.send_message(message.from_user.id, "Ok")

def get_data():
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM users;')

    answer = 'first line \n'

    for row in cursor:
        answer = answer + 'row = %r \n' % (row,)

    return answer


bot.polling(none_stop=True, interval=0)
