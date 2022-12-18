from os.path import exists

def Verif_doc():
    path = 'phone.csv'
    valid = exists(path)
    if not valid:
        print('Ваш список контактов пуст')
        return True