import os
import time
import sys
import sqlite3

# подключение к дата базе
con = sqlite3.connect('finances.db')
cur = con.cursor()


# creating table
def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS finances (
                    day integer,
                    amount real
                    )""")


def sum_money():
    print('(напишите "back" чтобы возвратиться.)')
    print('  Сумма, потраченная за всё время.   ')
    cur.execute("SELECT sum(amount) FROM finances")
    con.commit()
    if cur.fetchone() == (None,):
        print('Ничего не потрачено.')
    else:
        cur.execute("SELECT sum(amount) FROM finances")
        con.commit()
        print(cur.fetchone())
    time.sleep(2)
    statistics()


# функция добавления денег.
def add_money():
    print('(напишите "back" чтобы возвратиться.)')
    print(
        'Впишите день и потом сумму, которую хотите добавить в таблицу.\nПример: 2<enter>, 6.90<enter>\nОбязательно в таком порядке.')
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
    print('(напишите "back" чтобы возвратиться.)')
    print('Впишите день, информацию о котором вы хотите стереть.')
    day = input()
    if day == 'back':
        operations()
    cur.execute("DELETE from finances WHERE day = {0}".format(day))
    con.commit()
    print('Информация успешно удалена.')
    time.sleep(2)
    operations()


# операции с деньгами в целом
def operations():
    print('(напишите "back" чтобы возвратиться.)')
    print('Выберите операцию:')
    print('1 - Добавить кол-во потраченных средств.')
    print('2 - Удалить кол-во потраченных средств.')
    print('3 - Очистить ВСЮ информацию о средствах.')
    answer = input()
    if answer == str(1):
        add_money()
    elif answer == str(2):
        reduce_money()
    elif answer == str(3):
        clear_db()
    elif answer == 'back':
        intro()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        operations()


# fetchall
# def fetchall():
#    cur.execute("SELECT * FROM finances")
#    print(cur.fetchall())

def statistics():
    print('(напишите "back" чтобы возвратиться.)')
    print('               Статистика.            ')
    print('1 - Сколько потрачено за определённый день')
    print('2 - Сколько потрачено за всё время')
    answer = input()
    if answer == str(1):
        one_day_money()
    elif answer == str(2):
        sum_money()
    elif answer == 'back':
        intro()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        statistics()


# статистика
def one_day_money():
    print('                   Статистика.                       ')
    print('Напишите день, статистику о котором вы хотите узнать.')
    answer = input()
    if answer == 'back':
        statistics()
    cur.execute("SELECT * FROM finances WHERE day={0}".format(answer))
    print(' День' + '  Сумма ')
    print('  \/' + '    \/   ')
    print(cur.fetchone())
    con.commit()
    time.sleep(2)
    intro()


# очистка всех данных
def clear_db():
    print('(напишите "back" чтобы возвратиться.)')
    print('Вы действительно хотите удалить все записи?')
    print('Если вы уверены напишите "DELETE"')
    answer = input()
    if answer == 'DELETE':
        cur.execute('DROP TABLE finances')
        create_table()
        time.sleep(1)
        print('Данные успешно удалены.')
        operations()
    else:
        operations()


# правила
def rules():
    print('(напишите "back" чтобы возвратиться.)')
    print('   Правила использования программы.  ')
    time.sleep(1)
    print('   правила...  ')
    answer = input()
    if answer == 'back':
        intro()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        time.sleep(2)
        rules()


# вступление
def intro():
    print('Выберите функцию.')
    print('1 - Операции со средствами.')
    print('2 - Статистика.')
    print('3 - Правила использования программы.')
    answer = input()
    if answer == str(1):
        operations()
    elif answer == str(2):
        statistics()
    elif answer == str(3):
        rules()
    elif answer == 'quit':
        os.abort()
    elif answer == 'back':
        print('Вы и так на начальной ступени.')
        time.sleep(1)
        intro()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        time.sleep(1)
        intro()


create_table()
intro()
