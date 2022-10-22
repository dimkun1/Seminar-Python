


def input_tel():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    telefon = input("Введите телефон: ")
    data_of_birth = input("Введите дату рождение: ")
    with open('tel_dic.csv', 'a', encoding='utf-8') as file:
        file.write(f'{surname}, {name}, {data_of_birth}, {telefon}\n')
    file.close()
    print ('Контакт сохранен в справочнике!')


def print_tel():
    with open('tel_dic.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

