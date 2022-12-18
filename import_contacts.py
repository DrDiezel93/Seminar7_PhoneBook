from os.path import exists


def Import_file(file):
    with open(file, 'r', encoding = 'utf-8') as file:
        for line in file:
            with open('phone.csv', 'a+', encoding = 'utf-8') as file:
                file.write(line)
        with open('phone.csv', 'a+', encoding = 'utf-8') as file:
            file.write(f"\n")


def Import_contacts():
    temp = False
    while not temp:
        path = input('Введите название файла(приемр: list_contacts): ')
        path = path + '.csv'
        valid = exists(path)
        if not valid:
            print('Вы ввели неврное имя файла. Повторите попытку!')
        else:
            Import_file(path)
            print('Контакты инпортированы!')
            return True