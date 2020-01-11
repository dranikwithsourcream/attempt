from colorama import Fore, Back, Style
import os

#Back.GREEN + Fore.BLACK +

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def operations():
    print('Выберите операцию:')

def statistics():
    print('Выберите статистику:')
    print('1 - За 1 день.')
    print('2 - За 3 дня.')
    print('3 - За 7 дней.')
    print('4 - За 14 дней.')
    print('5 - За 31 день.')

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
