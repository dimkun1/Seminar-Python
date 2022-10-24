import excep
import log


def input_men():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    telefon = input("Введите телефон: ")
    data_of_birth = input("Введите дату рождения: ")
    job_title = input("Введите должность: ")
    shift = input("Введите смену сотрудника: ")
    id_com = excep.id_company()
    with open('Company_dic.csv', 'a', encoding='utf-8') as file:
        file.write(f'{id_com}, {surname}, {name}, {data_of_birth}, {telefon}, {job_title}, {shift}\n')
    file.close()
    print()
    print('Сотрудник сохранен в информационной системе !')
    log.universal_logger(f"{surname} {name},", data_description = "новый сотрудник сохранен в информационной системе")  


def print_company():
    log.universal_logger("", data_description = "распечатка всей информационной системы")  
    with open('Company_dic.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

def find_input():
    print()
    worlds = input("Введите данные для поиска = ")
    worlds = worlds.lower()
    log.universal_logger(worlds, data_description = "поиск в информационной системе") 
    flag = 1
    with open('Company_dic.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if worlds in line:
                flag = 0
                print(line) 
        if flag:   
            print("Нет таких данных")

def replace_input():
    worlds = input("\nВведите данные какие нужно изменить = ")
    worlds = worlds.lower()
    worlds_new = input("Введите новые данные = ")
    log.universal_logger(f'{worlds} на {worlds_new}', data_description = "изменение в информационной системе") 
    file = open('Company_dic.csv', 'r', encoding='utf-8').read().replace(worlds, worlds_new)
    with open('Company_dic.csv', 'w', encoding='utf-8') as file2:
        file2.write(file)

        
def del_input():
    worlds = input("\nВведите данные из строки которую нужно удалить = ")
    worlds = worlds.lower()
    log.universal_logger(f'{worlds}', data_description = "удаление из информационной системы") 
    with open('Company_dic.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    with open('Company_dic.csv', 'w', encoding='utf-8') as file:
                for line in data:
                    if worlds not in line:
                        file.write(line)





