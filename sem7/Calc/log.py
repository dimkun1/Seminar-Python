from datetime import datetime as dt


def universal_logger(data, data_description = "действие"):
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('log_calc.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data))
                    
def print_log():
    with open('log_calc.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')