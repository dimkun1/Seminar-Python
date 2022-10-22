import input_new
import log


def sumab():
    summa = input_new.x + input_new.y
    log.universal_logger(summa, data_description = "Сумма")  
    print(f"Сумма чисел {input_new.x} и {input_new.y} равно {summa}")
    print()
    


def subab():
    sub = input_new.x - input_new.y
    log.universal_logger(sub, data_description = "Вычитание")  
    print(f"Разность чисел {input_new.x} и {input_new.y} равно {sub}")
    print()
    

def multab():
    mult = input_new.x * input_new.y
    log.universal_logger(mult, data_description = "Умножение")  
    print(f"Умножение чисел {input_new.x} и {input_new.y} равно {mult}")
    print()
   
    
def divab():
    div = input_new.x / input_new.y
    log.universal_logger(div, data_description = "Деление")  
    print(f"Деление чисел {input_new.x} и {input_new.y} равно {div}")
    print()
    

def int_divab():
    int_div = input_new.x // input_new.y
    log.universal_logger(int_div, data_description = "Целочисленное деление")  
    print(f"Целочисленное деление чисел {input_new.x} и {input_new.y} равно {int_div}")
    print()
    

def div_w_rem_ab():
    div_w_rem = input_new.x % input_new.y
    log.universal_logger(div_w_rem, data_description = "Получение остатка от деления")  
    print(f"Остаток от деления чисел {input_new.x} и {input_new.y} равно {div_w_rem}")
    print()
   

def expab():
    exp = input_new.x ** input_new.y
    log.universal_logger(exp, data_description = "Возведение в степень")  
    print(f"Возведение числа {input_new.x} в степень {input_new.y} равно {exp}")
    print()
    