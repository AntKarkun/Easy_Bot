# Эта библиотека написана к файлу bot_Python.py Завьяловым Даниилом
import os
import psutil
import sys
import shutil
from random import randrange


# Функция робот информатор
def robot(b = ''):
    while True:
        print('{}, что ты хочешь делать?'.format(b))
        print('[1] - вывести список файлов')
        print('[2] - вывести информацию o системе')
        print('[3] - вывести список прцессов')
        # print('[4] - дублирование файлов')
        print('[5] - дублирование указанного файла')
        print('[6] - удаление дубликатов в дериктории')
        print('[7] - перевод из 10 сист. счислен. в любую')
        go = input('Ну что? :')

        if go == '1':
            print(os.listdir())

        elif go == '2':
            try:
                print('OS:            ' + sys.platform)
                print('Версия Python: ' + sys.version)
                print('Кодировка:     ' + sys.getdefaultencoding())
                print('Тек. директ.:  ' + os.path.abspath(os.curdir))
                print('Кол-во ядер:   ' + shutil.cpu_count())
            except:
                pass
        elif go == '3':
            print(psutil.pids())

        elif go == '0':
            dirsay = input('Укажите директорию: ')
            print('{0:=^50}'.format('дублирование файлов в тек. дериктории'))
            file_list = os.listdir(dirsay)
            i = 0

            while i < len(file_list):
                fullname = os.path.join(dirsay, file_list[i])

                if True:
                    os.path.isfile(file_list[i])
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)
                    i = i + 1

        elif go == '5':
            filename = input('Укажите имя файла: ')
            print('{0:=^50}'.format('дублирование указанного файла'))

            if os.path.isfile(filename):
                newfile = filename + '.dupl'
                shutil.copy(filename, newfile)

        elif go == '6':
            try:
                dirname = input('Укажите имя директории: ')
                print('{0:=^30}'.format('удаление дубликатов'))
                i = 0
                file_list = os.listdir(dirname)

                while i < len(file_list):
                    fullname = os.path.join(dirname, file_list[i])

                    if fullname.endswith('.dupl'):
                        os.remove(fullname)
                    i += 1
            except FileNotFoundError:
                print('error')

        elif go == '7':
            print('{0:=^50}'.format('пока не работает'))
            print('Но вы можете воспользоваться другими функциями калькулятора')
            kalk = input('Хотите? Если да, нажмите \"y\".\nЕсли нет, то нажмите \"n\": ')

            if kalk == 'y':
                viborl = '3'
                return viborl

        else:
            print('{0:=^30}'.format('ошибка'))

        answer = input('''\nЕсли хотите выйти, нажмите \"q\".
Если нет, то любую другую: ''')

        if answer == 'q' or answer == 'Q' or answer == 'й' or answer == 'Й':
            print('Пока, {}!'.format(b))
            return 'z'
        else:
            print('Хорошо!!!')


# Функция "рассказ историй"
def history_f(a = ''):
    while True:
        history_count = randrange(0, 3)
        print('{0:\'^30} \n{1} \n{0:\"^30} '.format('', history[history_count]))
        history_close = input('Если хотите выйти, нажмите \"q\". \nЕсли нет, то любую другую: ')

        if history_close == "q" or history_close == 'Q' or history_close == 'й' or history_close == 'Й':
            print('До свидания {}!!!'.format(a))
            return 'z'
            break


# истории для фукции выше
history = ['''1. Сволочи… В соседнем кабинете апельсин жрут, а у меня на них
аллергия. Сижу, слёзы текут. Ну, начальник спросил, чё реву.
— Да они там апельсин едят!
Сочувственно посмотрел, после обеда принёс мне два кило
апельсинов…''',

'''2. Сидим на работе. Звонит 5-летняя дочка сослуживицы, просит
позвать маму к телефону. Ей отвечают:
— А мамы нет, она в банке.
Продолжительное молчание, после этого следует вопрос:
— А как она туда залезла?''',

'''3. Сын (10 лет) лежал в больнице. Прихожу в очередной раз,
медсестра смеётся, рассказывает:
— Попросила его подписать продукты в холодильнике, он
подписал: «Курица», «Сок»…
Весь персонал веселился.''']
