import log






def excep_menu(size):
    while True:
        try:
            value_menu = input()
            while int(value_menu) not in range(1, size):
                print('\nНедопустимый ответ! Повторите ввод:')
                log.universal_logger(value_menu, data_description = "пользователь выбрал недопустимый ответ")
                value_menu = input()
            return int(value_menu)
        except:
            print('\nНеверный формат! Повторите ввод:')
            log.universal_logger(value_menu, data_description = "пользователь выбрал недопустимый ответ")
            


def check_int():
    while True:
        try:
            enter_num = (input())
            return int(enter_num)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.universal_logger(enter_num, data_description = "Ошибка ввода. Неверный формат")


def check_float():
    while True:
        try:
            enter_num = (input())
            return float(enter_num)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.universal_logger(enter_num, data_description = "Ошибка ввода. Неверный формат")