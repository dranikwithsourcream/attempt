import os
import sqlite3
con = sqlite3.connect('finances.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS finances (
                day text,
                amount text
                )""")

# функция добавления денег.
def add_money():
    print('(напишите "back" чтобы возвратиться.)')
    print('Впишите *день и потом сумму*, которую хотите добавить в таблицу.\nПример: 2<enter>, 6.90<enter>\nОбязательно в таком порядке.')
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
    print('reduce')

# операции с деньгами в целом
def operations():
    print('(напишите "back" чтобы возвратиться.)')
    print('Выберите операцию:')
    print('1 - Добавить кол-во потраченных средств.')
    print('2 - Удалить кол-во потраченных средств.')
    answer = input()
    if answer == str(1):
        add_money()
    elif answer == str(2):
        reduce_money()
    elif answer == 'back':
        intro()
        con.close()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        con.close()
        operations()

# статистика
def statistics():
    print('Выберите статистику:')
    print('1 - За 1 день.')
    print('2 - За 3 дня.')
    print('3 - За 7 дней.')
    print('4 - За 14 дней.')
    print('5 - За 31 день.')
    answer = input()

# вступление
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
