from import_contacts import Import_contacts
from read_file import Read_file
from print_data import print_data
from verif_doc import Verif_doc
from new_contact import new_contact
from export_contacts import writing_txt, writing_csv
from search_data import search_data

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель ({,}; {;}, {:}): ")
    if sep == "":
        sep = None
    return sep
def choice_todo_2():
   temp_2 = False
   while not temp_2: 
    print("Доступные операции с телефонной книгой:\n\
    1 - Импортировать контакты;\n\
    2 - Добавить новый контакт;\n\
    3 - Выход из программы;\n\
        ")
    ch = input("Введите цифру: ")
    if ch == '1':
        Import_contacts()
        temp_2 = True
        return temp_2
    elif ch == '2':
        sep = choice_sep()
        new_contact(input_data(), sep)
        temp_2 = True
        return temp_2
    elif ch == '3':
        print('До свидания')
        break
    else:
        print('Вы ввели некорретное значение! Повторите попытку')


def choice_todo():
    temp = False
    while not temp:
        print("Доступные операции с телефонной книгой:\n\
        1 - Добавить новый контакт;\n\
        2 - Печать всех контактов;\n\
        3 - Экспорт контактов;\n\
        4 - Поиск контактов;\n\
        5 - Выход из программы")
        ch = input("Введите цифру: ")
        if ch == '1':
            sep = choice_sep()
            new_contact(input_data(), sep)
            tempos = False
            while not tempos:
                print('Добавить еще контакт (1 - да; 2 - нет): ')
                choice = input('Введите цифру: ')
                if choice == '1':
                    sep = choice_sep()
                    new_contact(input_data(), sep)
                elif choice == '2':
                    tempos = True
                else:
                    print('Вы ввели некорретное значение! Повторите попытку')
        elif ch == '2':
            data = Read_file()
            print_data(data)
        elif ch == '3':
            tempos = False
            while not tempos:
                print('Выберите формат файла (1 - .txt; 2 - .scv): ')
                choice = input('Введите цифру: ')
                if choice == '1':
                    data = Read_file()
                    writing_txt(data)
                    print('Контакты успешно экспортированы (см. файл "Export_contacts.txt")')
                    tempos = True
                elif choice == '2':
                    file = 'phone.csv'
                    writing_csv(file)
                    print('Контакты успешно экспортированы (см. файл "Export_contacts.csv")')
                    tempos = True
                else:
                    print('Вы ввели некорретное значение! Повторите попытку')
        elif ch == '4':
            word = input('Введите данные для поиска (фамилию или имя): ')
            data = Read_file()
            search_data(word, data)
        elif ch == '5':
            print('До свидания')
            break
        else:
            print('Вы ввели некорретное значение! Повторите попытку')
    


greeting()

tem = Verif_doc()

if tem:
    temm = choice_todo_2()
    if temm:
        choice_todo()
else:
    temmm = choice_todo()
    if temmm:
        choice_todo()