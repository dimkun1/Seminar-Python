import log
import model_math as model
import input_new
import excep



type_menu_1 = 0       # Выберите действие с цифрами
type_menu = 0       # какими числами будем работать?

def menu3():
    global type_menu
    print("\nС какими числами будем работать?\n 1 - Целые\n 2 - Вещественные\n 3 - Комплексные\n 4 - выход")
    type_menu = excep.excep_menu(5)
    if type_menu == 1:
        log.universal_logger(type_menu, data_description = "пользователь выбрал Целые")  
        menu_two_numbers_int()
    elif type_menu == 2:
        log.universal_logger(type_menu, data_description = "пользователь выбрал Вещественные")  
        menu_two_numbers_float()
    elif type_menu == 3:
        log.universal_logger(type_menu, data_description = "пользователь выбрал Комплексные")  
        menu_two_numbers_complex()
    elif type_menu == 4:
        log.universal_logger(type_menu, data_description = "пользователь выбрал выход")  
        end_calc()
        
        
def menu_two_numbers_int():
    print("Вам нужно ввести два числа.")
    input_new.int_num()
    menu1()
    
def menu_two_numbers_float():
    print("Вам нужно ввести два числа.")
    input_new.float_num()
    menu1()

def menu_two_numbers_complex():
    print("Вам нужно ввести два числа.")
    input_new.complex_num()
    menu1()



def menu1():
    global type_menu_1
    if type_menu == 1:
        print(f"Выберите действие с числами {input_new.x} и {input_new.y}\n 1 - сумма\n 2 - вычитание\n 3 - умножение\n 4 - деление\n 5 - деление на цело\n 6 - остаток от деления\n 7 - возведение в степень\n 8 - назад\n 9 - выход")
        type_menu_1 = excep.excep_menu(10)
        if type_menu_1 == 1:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал сумма")  
            action(type_menu_1)
        elif type_menu_1 == 2:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал вычитание")  
            action(type_menu_1)
        elif type_menu_1 == 3:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал умножение")  
            action(type_menu_1)        
        elif type_menu_1 == 4:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал деление")  
            if input_new.y == 0:
                print("На ноль делить нельзя")
                continue_menu()
            elif input_new.y != 0:
                action(type_menu_1)
        elif type_menu_1 == 5:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал деление на цело")  
            if input_new.y == 0:
                print("На ноль делить нельзя")
                continue_menu()
            elif input_new.y != 0:
                action(type_menu_1)
        elif type_menu_1 == 6:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал остаток от деления")  
            if input_new.y == 0:
                print("На ноль делить нельзя")
                continue_menu()
            elif input_new.y != 0:
                action(type_menu_1)
        elif type_menu_1 == 7:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал возведение в степень")  
            action(type_menu_1)
        elif type_menu_1 == 8:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал назад")  
            menu3()
        elif type_menu_1 == 9:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал выход из калькулятора")  
            end_calc()

    elif type_menu == 2 or type_menu == 3:
        print(f"Выберите действие с числами {input_new.x} и {input_new.y}\n 1 - сумма\n 2 - вычитание\n 3 - умножение\n 4 - деление\n 5 - назад\n 6 - выход")
        type_menu_1 = excep.excep_menu(7)
        if type_menu_1 == 1:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал сумма")  
            action(type_menu_1)
        elif type_menu_1 == 2:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал вычитание")  
            action(type_menu_1)
        elif type_menu_1 == 3:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал умножение")  
            action(type_menu_1)       
        elif type_menu_1 == 4:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал деление")  
            if input_new.y == 0:
                print("На ноль делить нельзя")
                continue_menu()
            elif input_new.y != 0:
                action(type_menu_1)
        elif type_menu_1 == 5:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал назад")  
            menu3()
        elif type_menu_1 == 6:
            log.universal_logger(type_menu_1, data_description = "пользователь выбрал выход из калькулятора")  
            end_calc()





def action(type_menu_1):
    if type_menu_1 == 1:
        return model.sumab(), continue_menu()
    elif type_menu_1 == 2:
        return model.subab(), continue_menu()
    elif type_menu_1 == 3:
        return model.multab(), continue_menu()
    elif type_menu_1 == 4:
        return model.divab(), continue_menu()
    elif type_menu_1 == 5:
        return model.int_divab(), continue_menu()
    elif type_menu_1 == 6:
        return model.div_w_rem_ab(), continue_menu()
    elif type_menu_1 == 7:
        return model.expab(), continue_menu()

        
def continue_menu():
    print(f' 1 - продолжить работу с новыми числами?\n 2 - продолжить работу с числами {input_new.x} и {input_new.y}?\n 3 - показать логи\n 4 - выход')
    continue_menu = excep.excep_menu(5)
    if continue_menu == 1:
        log.universal_logger(continue_menu, data_description = "пользователь выбрал продолжить работу с новыми числами") 
        menu3()
    elif continue_menu == 2:
        log.universal_logger(continue_menu, data_description = "пользователь выбрал продолжить работу с текущими числами") 
        menu1()
    elif continue_menu == 3:
        log.universal_logger(continue_menu, data_description = "пользователь выбрал показать логи") 
        log.print_log()
        print('продолжить работу с калькулятором? \n 1 - продолжить\n 2 - выход')
        continue_menu1 = excep.excep_menu(3)
        if continue_menu1 == 1:
            menu3()
        else:
            end_calc()
    elif continue_menu == 4:
        log.universal_logger(continue_menu, data_description = "пользователь выбрал выход") 
        end_calc()







def end_calc():
    print('Выход из калькулятора')
    log.universal_logger("Выход из программы", data_description = "Выход")
    exit()

print(10*'\n')

print("Вас приветсвует калькулятор!")
log.universal_logger("Вход в программу", data_description = "Запуск")

menu3()
