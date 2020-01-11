import os

# функция добавления денег
def add_money():
    print('add')

# функция уменьшения денег
def reduce_money():
    print('reduce')

# операции с деньгами в целом
def operations():
    print('Выберите операцию:')
    print('1 - Добавить кол-во потраченных средств.')
    print('2 - Удалить кол-во потраченных средств.')
    answer = input()
    if answer == str(1):
        add_money()
    elif answer == str(2):
        reduce_money()
    elif answer == 'назад':
        intro()
    else:
        print('Неверный ответ. Попробуйте ещё раз.')
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
