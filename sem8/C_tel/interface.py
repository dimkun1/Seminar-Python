import excep
import input_new
import log


def menu1():
    log.universal_logger('', data_description = "открылось главное меню в информационной системы")
    print('Это информационная система компании, что вы хотите сейчас сделать? \n 1 - добавить \n 2 - посмотреть \n 3 - поиск \n 4 - изменить \n 5 - удалить \n 6 - выход')
    menu = excep.excep_menu(7)
    log.universal_logger(f'{menu}', data_description = "пользователь выбрал в информационной системе") 
    if menu == 1:
        input_new.input_men()
        log.universal_logger('', data_description = "добавление новых данных в информационную систему")
        print(2*"\n")
        menu_small()
    elif menu == 2:
        print(2*"\n")
        print("Данные в информационной системе")
        input_new.print_company()
        log.universal_logger('', data_description = "просмотр данных в информационной системе")
        print(2*"\n")
        menu_small()
    elif menu == 3:
        print("\nПоиск в информационной системе")
        input_new.find_input()
        log.universal_logger('', data_description = "Поиск в информационной системе")
        menu_small()
    elif menu == 4:
        print("\nИзменить запись")
        input_new.replace_input()
        log.universal_logger('', data_description = "Изменить запись из информационной системы")
        menu_small()
    elif menu == 5:
        print("\nУдалить запись")
        input_new.del_input()
        log.universal_logger('', data_description = "Удалить запись из информационной системы")
        menu_small() 
    elif menu == 6:
        print("\nВыход из информационной системы")
        log.universal_logger('', data_description = "Выход из информационной системы")
        exit()


        
def menu_small():
    print()
    print("Вы хотите продолжить работу с информационной системой? \n 1 - Да \n 2 - Нет")
    log.universal_logger('', data_description = "открылось маленькое меню в информационной системы")
    menu_small1 = excep.excep_menu(3)
    if menu_small1 == 1:
        log.universal_logger(f'{menu_small1}', data_description = "пользователь выбрал продолжить работу с информационной системой")
        menu1()
    elif menu_small1 == 2:
        print()
        print("Выход из информационной системы")
        log.universal_logger('', data_description = "Выход из информационной системы")
        exit()



print(10*"\n")
print('Здравствуйте это компания автосервис!')
log.universal_logger('', data_description = "начало работы в информационной системы")
print()
menu1()

        


