﻿# import math
# НАЧАЛО
from one import robot, history_f

vibor = 'z'

print('''Здравствуйте.
Добро пожаловать в программу \"Бот\". ''')
#a = input('Но сначала скажи мне своё имя: ')  # тут имя пользователя зап. в переменую а
print('Хорошо {}, вот её функции: '.format(''))

while True:
    if vibor != '':  # (тут vibor = 'z')
        print('[1] - запустить программу \"Робот информатор\"')
        print('[2] - рассказать историю или анекдот')
        print('[3] - калькулятор')
        vibor = input("Что выберете? (Нажмите \"n\" для выхода): ")

        if vibor == 'n' or vibor == 'N' or vibor == "т" or vibor == "Т": break  # если п.(User) нажал n то цикл завершается и конец
        if vibor == '1':
            viborl = robot()    # запустить функцию robot с аргументамии: а - имя польз.
            vibor = viborl
        elif vibor == '2':
            vibor = history_f()  # если ползователь(далее п.) выбрал 2, то рассказать 1 из историй

        if vibor == '3':
            print('\nПлюс - \"+\", минус - \"-\", умножить - \"*\",')
            print('разделить - \"/\", возвести в степень - \"**\"')
            # print("Если хотите дополнительные функции калькулятора, нажмите \"1\".")

            while True:

##                if math.isfinite(one):
##                if one == '1':
##                    print('Модуль числа - 1, остаток от деления X на Y - 2,')
##                    print('вычисляет гипотенузу треугольника с катетами X и Y - 3')
##                    one1 = input('Введите номер выражения: ')
##                    if one1 == '1':
##                        one_dopl = 1
##                        print('Модуль числа {1} - {2}'.format(one, one1))
##                    elif one1 == '2':
##                        pass
##                    elif one1 == '3':
##                        pass
##                    else:
##                        pass

                one = input('Введите выражение: ')

                try:
                    print('Результат = ' + str(eval(one)))

                except NameError:
                    print('Ошибка. Попробуйте ещё раз.\n')
                except SyntaxError:
                    print('Ошибка. Вы что-то не дописали! \nПопробуйте ещё раз.\n')
                except ZeroDivisionError:
                    print('Ах ты!!! Не дели на ноль! \nПопробуй ещё раз!\n')

                else:
                    print('\nЕсли хотите выйти, нажмите \"q\".\nЕсли нет, то')

                if one == 'q' or one == 'Q' or one == 'й' or one == 'Й':
                    break

    else:
        print('Что-то не так!!!')
print('Пока {}!!!'.format(''))