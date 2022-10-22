


def excep_menu(size):
    while True:
        try:
            value_menu = input()
            while int(value_menu) not in range(1, size):
                print('\nНедопустимый ответ! Повторите ввод:')
                value_menu = input()
            return int(value_menu)
        except:
            print('\nНеверный формат! Повторите ввод:')

            
