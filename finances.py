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
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        operations()

# статистика
def statistics():
    print('Напишите день, статистику о котором вы хотите узнать.')
    answer = input()
    cur.execute("SELECT * FROM finances WHERE day={0}".format(answer))
    print(' День' + '  Сумма')
    print('  \/' + '    \/')
    print(cur.fetchone())
    con.commit()
# вступление
def intro():
    print('1 - Операции со средствами.')
    print('2 - Когда и сколько потратил.')
    answer = input()
    if answer == str(1):
        operations()
    elif answer == str(2):
        statistics()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
        intro()

intro()
