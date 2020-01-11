from colorama import Fore, Back, Style

#Back.GREEN + Fore.BLACK +
def operations():
    print('1')

def statistics():
    print('2')

def intro():
    print('1 - Операции со средствами.')
    print('2 - Статистика.')
    answer = input()
    if answer == str(1):
        operations()
    elif answer == str(2):
        statistics()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        intro()
intro()
