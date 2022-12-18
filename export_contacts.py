def writing_txt(inf):
    file = 'Export_contacts.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        for item in inf:
            data.write(f'Фамилия: {item[0]}\nИмя: {item[1]}\nНомер телефона: {item[2]}\nОписание: {item[3]}\n\n\n')


def writing_csv(fil):
    with open(fil, 'r', encoding = 'utf-8') as file:
        for line in file:
            with open('Export_contacts.csv', 'a+', encoding = 'utf-8') as file:
                file.write(line)