import excep
import input_new



def menu1():
    print('Телефонный справочник \n 1 - импорт данных\n 2 - экспорт данных\n 3 - выход')
    menu = excep.excep_menu(4)
    if menu == 1:
        input_new.input_tel()
        print(2*"\n")
        menu1()
    elif menu == 2:
        print(2*"\n")
        print("Данные в телефонном справочнике")
        input_new.print_tel()
        print(2*"\n")
        menu1()
    elif menu == 3:
        print("Выход из телефонного справочника")
        exit()


        
print(10*"\n")
menu1()

        


