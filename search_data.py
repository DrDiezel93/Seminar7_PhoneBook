from print_data import search_print_1, search_print_2

def search_data(word, data):
    search_print_1()
    for item in data:
        if word in item:
            search_print_2(item)