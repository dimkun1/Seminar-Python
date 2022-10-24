import log


def excep_menu(size):
    while True:
        try:
            value_menu = input()
            log.universal_logger(value_menu, data_description = "пользователь выбрал") 
            while int(value_menu) not in range(1, size):
                print('\nНедопустимый ответ! Повторите ввод:')
                log.universal_logger(value_menu, data_description = "пользователь выбрал недопустимый ответ")  
                value_menu = input()
                log.universal_logger(value_menu, data_description = "пользователь выбрал") 
            return int(value_menu)
        except:
            print('\nНеверный формат! Повторите ввод:')
            log.universal_logger(value_menu, data_description = "пользователь ввел неверный формат")  


def id_company():
    line_count = sum(1 for line in open('Company_dic.csv'))
    log.universal_logger(line_count, data_description = " к новому сотруднику присвоили новый ид")
    return line_count






            
