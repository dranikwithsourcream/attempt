import os
import time
import sqlite3
from colorama import Fore, Back, Style
from colorama import init
init()

con = sqlite3.connect('finances.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS finances (
                day text,
                amount text
                )""")

# функция добавления денег.
def add_money():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.YELLOW + Fore.BLACK + 'Впишите ' + Back.RED + Fore.BLACK + 'день и потом сумму' + Back.YELLOW + Fore.BLACK + ', которую хотите добавить в таблицу.\n' + Back.RED + Fore.BLACK + 'Пример: 2<enter>, 6.90<enter>\n' + Back.YELLOW + Fore.BLACK + 'Обязательно в таком порядке.')
    day = input()
    if day == 'back':
        operations()
    amount = input()
    if amount == 'back':
        operations()
    cur.execute("INSERT INTO finances VALUES ({0} , {1})".format(day, amount))
    con.commit()
    operations()

# функция уменьшения денег
def reduce_money():
    print(Back.RED + Fore.BLACK + 'Функция временно недоступна.')
    time.sleep(2)
    operations()
# операции с деньгами в целом
def operations():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.YELLOW + Fore.BLACK + 'Выберите операцию:')
    print(Back.CYAN + Fore.BLACK + '1 - Добавить кол-во потраченных средств.')
    print(Back.CYAN + Fore.BLACK + '2 - Удалить кол-во потраченных средств.')
    answer = input()
    if answer == str(1):
        add_money()
    elif answer == str(2):
        reduce_money()
    elif answer == 'back':
        intro()
    else:
        print(Back.RED + Fore.BLACK + 'Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        operations()

# статистика
def statistics():
    print(Back.YELLOW + Fore.BLACK + 'Напишите день, статистику о котором вы хотите узнать.')
    answer = input()
    cur.execute("SELECT * FROM finances WHERE day={0}".format(answer))
    print(' День' + '  Сумма ')
    print('  \/' + '    \/   ')
    print(cur.fetchone())
    con.commit()
    time.sleep(2)
    intro()

#правила
def rules():
    print(Back.RED + Fore.BLACK + 'Функция временно недоступна.')
    time.sleep(2)
    intro()

# вступление
def intro():
    print(Back.YELLOW + Fore.BLACK + 'Выберите функцию.')
    print(Back.CYAN + Fore.BLACK + '1 - Операции со средствами.')
    print(Back.CYAN + Fore.BLACK + '2 - Когда и сколько потратил.')
    print(Back.GREEN + Fore.BLACK + '3 - Правила использования программы.')
    answer = input()
    if answer == str(1):
        operations()
    elif answer == str(2):
        statistics()
    elif answer == str(3):
        rules()
    else:
        print(Back.RED + Fore.BLACK + 'Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        intro()

intro()
