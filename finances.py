import os
import time
import sqlite3
from colorama import Fore, Back, Style
from colorama import init
init()

#подключение к дата базе
con = sqlite3.connect('finances.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS finances (
                day text,
                amount REAL
                )""")

#удаление в консоле
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# функция добавления денег.
def add_money():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.YELLOW + Fore.BLACK + 'Впишите ' + Back.RED + Fore.BLACK + 'день и потом сумму' + Back.YELLOW + Fore.BLACK + ', которую хотите добавить в таблицу.\n' + Back.RED + Fore.BLACK + 'Пример: 2<enter>, 6.90<enter>\n' + Back.YELLOW + Fore.BLACK + 'Обязательно в таком порядке.')
    print(Back.BLACK + Fore.WHITE)
    day = input()
    print(Back.BLACK + Fore.WHITE)
    if day == 'back':
        operations()
    print(Back.BLACK + Fore.WHITE)
    amount = input()
    print(Back.BLACK + Fore.WHITE)
    if amount == 'back':
        operations()
    cur.execute("INSERT INTO finances VALUES ({0} , {1})".format(day, amount))
    con.commit()
    operations()

# функция уменьшения денег
def reduce_money():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.YELLOW + Fore.BLACK + 'Впишите день, информацию о котором вы хотите стереть.')
    print(Back.BLACK + Fore.WHITE)
    day = input()
    print(Back.BLACK + Fore.WHITE)
    if day == 'back':
        operations()
    cur.execute("DELETE from finances WHERE day = {0}".format(day))
    con.commit()
    print(Back.CYAN + Fore.BLACK + 'Информация успешно удалена.')
    time.sleep(2)
    operations()

# операции с деньгами в целом
def operations():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.YELLOW + Fore.BLACK + 'Выберите операцию:')
    print(Back.CYAN + Fore.BLACK + '1 - Добавить кол-во потраченных средств.')
    print(Back.CYAN + Fore.BLACK + '2 - Удалить кол-во потраченных средств.')
    print(Back.BLACK + Fore.WHITE)
    answer = input()
    print(Back.BLACK + Fore.WHITE)
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

#fetchall
def fetchall():
    cur.execute("SELECT * FROM finances")
    print(cur.fetchall())

# статистика
def statistics():
    print(Back.GREEN + Fore.BLACK + '                   Статистика.                       ')
    print(Back.YELLOW + Fore.BLACK + 'Напишите день, статистику о котором вы хотите узнать.')
    print(Back.BLACK + Fore.WHITE)
    answer = input()
    print(Back.BLACK + Fore.WHITE)
    if answer == 'back':
        intro()
    cur.execute("SELECT * FROM finances WHERE day={0}".format(answer))
    print(Back.CYAN + Fore.BLACK + ' День' + '  Сумма ')
    print(Back.CYAN + Fore.BLACK + '  \/' + '    \/   ')
    print(Back.CYAN + Fore.BLACK + str(cur.fetchone()))
    con.commit()
    print(Back.BLACK + Fore.WHITE)
    time.sleep(2)
    intro()

#правила
def rules():
    print(Back.YELLOW + Fore.BLACK + '(напишите "back" чтобы возвратиться.)')
    print(Back.GREEN + Fore.BLACK + '   Правила использования программы.  ')
    time.sleep(1)
    print(Back.GREEN + Fore.BLACK + '   правила...  ')
    print(Back.BLACK + Fore.WHITE)
    answer = input()
    print(Back.BLACK + Fore.WHITE)
    if answer == 'back':
        intro()
    else:
        print(Back.RED + Fore.BLACK + 'Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        rules()

# вступление
def intro():
    print(Back.YELLOW + Fore.BLACK + 'Выберите функцию.')
    print(Back.CYAN + Fore.BLACK + '1 - Операции со средствами.')
    print(Back.CYAN + Fore.BLACK + '2 - Когда и сколько потратил.')
    print(Back.GREEN + Fore.BLACK + '3 - Правила использования программы.')
    print(Back.BLACK + Fore.WHITE)
    answer = input()
    print(Back.BLACK + Fore.WHITE)
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

fetchall()
