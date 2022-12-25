from telebot import TeleBot, types
from os.path import exists
import os
 
TOKEN = ''
 
bot = TeleBot(TOKEN)
 

@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            with open('phone.csv', 'a+', encoding = 'utf-8') as file:
                file.write(line)
        with open('phone.csv', 'a+', encoding = 'utf-8') as file:
            file.write(f"\n")
    bot.send_message(chat_id=msg.from_user.id, text='Контакты импортированы')
    os.remove(filename)
 

def Verif_doc():
    path = 'phone.csv'
    valid = exists(path)
    if not valid:
        # print('Ваш список контактов пуст')
        return True


def Read_file():
    with open('phone.csv', 'r', encoding = 'utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

def writing_txt(inf):
    file = 'Export_contacts.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        for item in inf:
            data.write(f'Фамилия: {item[0]}\nИмя: {item[1]}\nНомер телефона: {item[2]}\nОписание: {item[3]}\n\n\n')


def new_contact(data):
    with open('phone.csv', 'a+', encoding = 'utf-8') as file:
        file.write(','.join(data))
        file.write(f"\n")


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Добро пожаловать в телефонный справочник!')
    if Verif_doc() == True: 
        bot.send_message(chat_id=msg.from_user.id, text=f'Ваш список контактов пуст')
        bot.send_message(chat_id=msg.from_user.id, text=f'Доступные операции с телефонной книгой:')
        bot.send_message(chat_id=msg.from_user.id, text=f'1 - Импортировать контакты\n2 - Добавить новый контакт\n')
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите число')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Доступные операции с телефонной книгой:')
        bot.send_message(chat_id=msg.from_user.id, text=f'1 - Импортировать контакты\n2 - Добавить новый контакт\n3 - Печать всех контактов\n4 - Экспорт контактов\n')
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите число')

@bot.message_handler()
def answer(msg: types.Message):
    data = []
    text = msg.text
    if text == '1':
        bot.send_message(chat_id=msg.from_user.id, text=f'Добавьте файл в формате .scv')
    elif text == '2':
        data.append(bot.register_next_step_handler(msg, answer1))
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите данные через пробел в формате:\nФамилия/Имя/Номер телефона/Категория контакта')
    elif text == '3':
        with open('phone.csv', 'r', encoding = 'utf-8') as file:
            for line in file:
                bot.send_message(chat_id=msg.from_user.id, text=f'{line}')
    elif text == '4':
        data = Read_file()
        writing_txt(data)       
        bot.send_document(chat_id=msg.from_user.id, document=open('Export_contacts.txt', 'rb'))
        bot.send_message(chat_id=msg.from_user.id, text=f'Контакты экспортированы')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'До свидания')

 
def answer1(msg):
    data = list(msg.text.split())
    new_contact(data)
    bot.send_message(chat_id=msg.from_user.id, text=f'Контакт добавлен')
 
 
bot.polling()