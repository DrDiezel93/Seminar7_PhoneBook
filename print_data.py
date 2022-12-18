def print_data(data):
    print()
    print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Категория".center(20))
    print("-"*80)
    for item in data:
        print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20))
    
    print()

def search_print_1():
    print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Категория".center(20))
    print("-"*80)


def search_print_2(data_2):
    print(data_2[0].center(20), data_2[1].center(20), data_2[2].center(20), data_2[3].center(20))