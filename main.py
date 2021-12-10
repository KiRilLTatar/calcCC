import tkinter as tk

import eel

win = tk.Tk()  # создание окна и разбиение на части
win.title("Калькулятор СС")  # создание окна и разбиение на части
win.iconphoto(True, tk.PhotoImage(file='icons8-калькулятор-48.png'))
w_win = win.winfo_screenwidth()
h_win = win.winfo_screenheight()
w_win = w_win // 2  # середина экрана
h_win = h_win // 2
w = w_win - 400  # смещение от середины
h = h_win - 300
win.geometry('800x500+{}+{}'.format(w, h))
win.wm_geometry("800x500")  # создание окна и разбиение на части
win.resizable(False, False)  # создание окна и разбиение на части

tetr = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000',
        '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

tetr_2 = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def Error(change_1, change_2):
    global text1
    text1.delete(0, 'end')
    popup = tk.Toplevel()
    popup.grab_set()
    w_pop = win.winfo_screenwidth()
    h_pop = win.winfo_screenheight()
    w_pop = w_pop // 2  # середина экрана
    h_pop = h_pop // 2
    w_pop = w_pop - 150  # смещение от середины
    h_pop = h_pop - 300
    popup.geometry('400x100+{}+{}'.format(w_pop, h_pop))
    popup.resizable(False, False)
    text_error = tk.Label(popup, text=f'{change_1} число может содержать только цифры \n {change_2}!!!',
                          font='Arial 13')
    text_error.pack(side='top')
    button_OK = tk.Button(popup, text='ОК', font='Arial 10', command=lambda: popup.destroy())
    button_OK.pack(side='bottom')


lab4 = tk.Label(win, text='Результат', font='Arial 18')
lab4.place(x=100, y=400)


def count_0_9(param_1, param_2, param_3):
    global lab4
    n = []
    x = text1.get()
    b = len(x)
    c = 0
    h = 0
    m = 1
    for i in range(0, b):
        c += int(x[h]) * (param_1 ** (b - m))  # возводим в степень каждую цифру и поочередно прибавляем их
        h += 1  # берем вторую цифру и так поочередно
        m += 1  # уменьшаем число на которое будем возводить
    while True:
        r = c % param_2
        for key, value in tetr_2.items():
            value = str(value)
            r = str(r)
            r = r.replace(key, value)
        n.append(r)
        c //= param_2
        if c / param_2 == 0:
            break
    rev = (n[::-1])
    lab4 = tk.Label(win, text=f'Число в {param_3} системе:' + str(''.join(rev)), font='Arial 18')
    lab4.place(x=30, y=400)


def count_10(param_1):
    global lab4
    x = text1.get()
    b = len(x)
    c = 0
    h = 0
    m = 1
    for i in range(0, b):
        c += int(x[h]) * (param_1 ** (b - m))  # возводим в степень каждую цифру и поочередно приваляем их
        h += 1  # берем вторую цифру и так поочередно
        m += 1  # уменьшаем число на которое будем возводить
    lab4 = tk.Label(win, text=f'Число в десятичной системе:' + str(c), font='Arial 18')
    lab4.place(x=30, y=400)


def count_10_1(param_2, param_3):
    global lab4
    n = []
    x = text1.get()
    while True:
        r = x % param_2
        for key, value in tetr_2.items():
            value = str(value)
            r = str(r)
            r = r.replace(key, value)
        n.append(str(r))
        x //= param_2
        if x / param_2 == 0:
            break
    rev = (n[::-1])
    lab4 = tk.Label(win, text=f'Число в {param_3} системе:' + str(''.join(rev)), font='Arial 18')
    lab4.place(x=30, y=400)


def count_in_2():
    global lab4
    x = text1.get()
    for key, value in tetr.items():
        value = str(value)
        x = x.replace(key, value)
    x = int(x)
    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10
    result.reverse()
    num = 0
    for i, v in enumerate(reversed(result)):
        num += v * 10 ** i
    lab4 = tk.Label(win, text=f'Число в двоичной системе:' + str(num),
                    font='Arial 18')
    lab4.place(x=30, y=400)


def count_11_16(parametr_2, parametr_3):
    global lab4
    n = []
    x = text1.get()
    b = len(x)
    c = 0
    h = 0
    m = 1
    for key, value in tetr.items():
        value = str(value)
        x = x.replace(key, value)
    x = int(x)
    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10
    result.reverse()
    num = 0
    for i, v in enumerate(reversed(result)):
        num += v * 10 ** i
    num = str(num)
    for i in range(0, b):
        c += int(num[h]) * (2 ** (b - m))  # возводим в степень каждую цифру и поочередно приваляем их
        h += 1  # берем вторую цифру и так поочередно
        m += 1  # уменьшаем число на которое будем возводить
    while True:
        r = c % parametr_2
        for key, value in tetr_2.items():
            value = str(value)
            r = str(r)
            r = r.replace(key, value)
        n.append(str(r))
        c //= parametr_2
        if c / parametr_2 == 0:
            break
    rev = (n[::-1])
    lab4 = tk.Label(win, text=f'Число в {parametr_3} системе:' + str(''.join(rev)),
                    font='Arial 18')
    lab4.place(x=30, y=400)


def count_10_2():
    global lab4
    n = []
    x = text1.get()
    b = len(x)
    c = 0
    h = 0
    m = 1
    for key, value in tetr.items():
        value = str(value)
        x = x.replace(key, value)
    x = int(x)
    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10
    result.reverse()
    num = 0
    for i, v in enumerate(reversed(result)):
        num += v * 10 ** i
    num = str(num)
    for i in range(0, b):
        c += int(num[h]) * (2 ** (b - m))  # возводим в степень каждую цифру и поочередно приваляем их
        h += 1  # берем вторую цифру и так поочередно
        m += 1  # уменьшаем число на которое будем возводить
    lab4 = tk.Label(win, text=f'Число в десятеричной системе:' + str(c),
                    font='Arial 18')
    lab4.place(x=30, y=400)


def count():
    global lab4
    input_name = text1.get()

    allowed = set('01')
    allowed_2 = set('012')
    allowed_3 = set('01234567')
    allowed_4 = set('0123456789')
    allowed_5 = set('0123456789ABCDEF')
    allowed_6 = set('0123')
    allowed_7 = set('01234')
    allowed_8 = set('012345')
    allowed_9 = set('0123456')
    allowed_A = set('012345678')
    allowed_B = set('0123456789A')
    allowed_C = set('0123456789AB')
    allowed_D = set('0123456789ABC')
    allowed_E = set('0123456789ABCD')
    allowed_F = set('0123456789ABCDE')
    if var.get() == 0:
        def chek_1(input_name):
            return set(input_name) <= allowed

        if chek_1(input_name):
            if var.get() == 0 and text3.get() == '2' or var1.get() == 0:  # из двоичной в двоичную
                lab4 = tk.Label(win, text=f'Число в двоичной системе:' + str(text1.get()), font='Arial 18')
                lab4.place(x=30, y=400)
            elif var.get() == 0 and text3.get() == '3' or var1.get() == 1:  # из двоичной в троичную
                count_0_9(2, 3, 'троичной')
            elif var.get() == 0 and text3.get() == '4':
                count_0_9(2, 4, 'четверичной')
            elif var.get() == 0 and text3.get() == '5':
                count_0_9(2, 5, 'пятеричной')
            elif var.get() == 0 and text3.get() == '6':
                count_0_9(2, 6, 'шестеричной')
            elif var.get() == 0 and text3.get() == '7':
                count_0_9(2, 7, 'семеричной')
            elif var.get() == 0 and text3.get() == '8' or var1.get() == 2:  # из двоичной в восьмеричную
                count_0_9(2, 8, 'восьмеричной')
            elif var.get() == 0 and text3.get() == '9':
                count_0_9(2, 9, 'девятеричной')
            elif var.get() == 0 and text3.get() == '10' or var1.get() == 3:  # из двоичной в десятичную
                count_10(2)
            elif var.get() == 0 and text3.get() == '11':
                count_0_9(2, 11, 'одинадцатеричной')
            elif var.get() == 0 and text3.get() == '12':
                count_0_9(2, 12, 'двенадцатеричной')
            elif var.get() == 0 and text3.get() == '13':
                count_0_9(2, 13, 'тринадцатеричной')
            elif var.get() == 0 and text3.get() == '14':
                count_0_9(2, 14, 'четырнадцатеричной')
            elif var.get() == 0 and text3.get() == '15':
                count_0_9(2, 15, 'пятнадцатеричной')
            elif var.get() == 0 and text3.get() == '16' or var1.get() == 4:  # из двоичной в шестнадцатеричную
                x = hex(int(text1.get(), 2))[2:].upper()
                lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                font='Arial 18')
                lab4.place(x=30, y=400)
        else:
            Error(change_1="Двоичное", change_2="0 и 1")

    if var.get() == 1:
        def chek_2(input_name):
            return set(input_name) <= allowed_2

        if chek_2(input_name):
            if var.get() == 1 and text3.get() == '2' or var1.get() == 0:  # из троичной в двоичную
                count_0_9(3, 2, 'двоичной')
            elif var.get() == 1 and text3.get() == '3' or var1.get() == 1:  # из троичной в троичную
                lab4 = tk.Label(win, text=f'Число в троичной системе:' + str(text1.get()),
                                font='Arial 18')
                lab4.place(x=30, y=400)
            elif var.get() == 1 and text3.get() == '4':
                count_0_9(3, 4, 'четверичной')
            elif var.get() == 1 and text3.get() == '5':
                count_0_9(3, 5, 'пятеричной')
            elif var.get() == 1 and text3.get() == '6':
                count_0_9(3, 6, 'шестеричной')
            elif var.get() == 1 and text3.get() == '7':
                count_0_9(3, 7, 'семеричной')
            elif var.get() == 1 and text3.get() == '8' or var1.get() == 2:  # из троичной в восьмеричную
                count_0_9(3, 8, 'восьмеричной')
            elif var.get() == 1 and text3.get() == '9':
                count_0_9(3, 9, 'девятерчной')
            elif var.get() == 1 and text3.get() == '10' or var1.get() == 3:  # из троичной в десятичную
                count_10(3)
            elif var.get() == 1 and text3.get() == '11':
                count_0_9(3, 11, 'одинадцатеричной')
            elif var.get() == 1 and text3.get() == '12':
                count_0_9(3, 12, 'двенадцатеричной')
            elif var.get() == 1 and text3.get() == '13':
                count_0_9(3, 13, 'тринадцатеричной')
            elif var.get() == 1 and text3.get() == '14':
                count_0_9(3, 14, 'четырнадцатеричной')
            elif var.get() == 1 and text3.get() == '15':
                count_0_9(3, 15, 'пятнадцатеричной')
            elif var.get() == 1 and text3.get() == '16' or var1.get() == 4:  # из троичной в шестнадцатеричную
                x = hex(int(text1.get(), 3))[2:].upper()
                lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                font='Arial 18')
                lab4.place(x=30, y=400)
        else:
            Error(change_1="Троичное", change_2="0, 1 и 2")

    if var.get() == 2:
        def chek_3(input_name):
            return set(input_name) <= allowed_3

        if chek_3(input_name):
            if var.get() == 2 and text3.get() == '2' or var1.get() == 0:
                count_0_9(8, 2, 'двоичной')
            elif var.get() == 2 and text3.get() == '3' or var1.get() == 1:
                count_0_9(8, 3, 'троичной')
            elif var.get() == 2 and text3.get() == '4':
                count_0_9(8, 4, 'четверичной')
            elif var.get() == 2 and text3.get() == '5':
                count_0_9(8, 5, 'пятеричной')
            elif var.get() == 2 and text3.get() == '6':
                count_0_9(8, 6, 'шестеричной')
            elif var.get() == 2 and text3.get() == '7':
                count_0_9(8, 7, 'семеричной')
            elif var.get() == 2 and text3.get() == '8' or var1.get() == 2:
                lab4 = tk.Label(win, text=f'Число в восьмеричной системе:' + str(''.join(text1.get())),
                                font='Arial 18')
                lab4.place(x=30, y=400)
            elif var.get() == 2 and text3.get() == '9':
                count_0_9(8, 9, 'девятеричной')
            elif var.get() == 2 and text3.get() == '10' or var1.get() == 3:
                count_10(8)
            elif var.get() == 2 and text3.get() == '11':
                count_0_9(8, 11, 'одинадцатеричной')
            elif var.get() == 2 and text3.get() == '12':
                count_0_9(8, 12, 'двенадцатеричной')
            elif var.get() == 2 and text3.get() == '13':
                count_0_9(8, 13, 'тринадцатеричной')
            elif var.get() == 2 and text3.get() == '14':
                count_0_9(8, 14, 'четырнадцатеричной')
            elif var.get() == 2 and text3.get() == '15':
                count_0_9(8, 15, 'пятнадцатеричной')
            elif var.get() == 2 and text3.get() == '16' or var1.get() == 4:
                x = hex(int(text1.get(), 8))[2:].upper()
                lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                font='Arial 18')
                lab4.place(x=30, y=400)
        else:
            Error(change_1="Восьмеричное", change_2="от 0 до 7(вкл)")

    if var.get() == 3:
        def chek_4(input_name):
            return set(input_name) <= allowed_4

        if chek_4(input_name):
            if var.get() == 3 and text3.get() == '2' or var1.get() == 0:
                count_10_1(2, 'двоичной')
            elif var.get() == 3 and text3.get() == '3' or var1.get() == 1:
                count_10_1(3, 'троичной')
            elif var.get() == 3 and text3.get() == '4':
                count_10_1(4, 'четверичной')
            elif var.get() == 3 and text3.get() == '5':
                count_10_1(5, 'пятеричной')
            elif var.get() == 3 and text3.get() == '6':
                count_10_1(6, 'шестеричной')
            elif var.get() == 3 and text3.get() == '7':
                count_10_1(7, 'семеричной')
            elif var.get() == 3 and text3.get() == '8' or var1.get() == 2:
                count_10_1(8, 'восьмеричной')
            elif var.get() == 3 and text3.get() == '9':
                count_10_1(9, 'девятеричной')
            elif var.get() == 3 and text3.get() == '10' or var1.get() == 3:
                lab4 = tk.Label(win, text=f'Число в десятеричной системе:' + str(''.join(text1.get())),
                                font='Arial 18')
                lab4.place(x=30, y=400)
            elif var.get() == 3 and text3.get() == '11':
                count_10_1(11, 'одинадцатеричной')
            elif var.get() == 3 and text3.get() == '12':
                count_10_1(12, 'двенадцатеричной')
            elif var.get() == 3 and text3.get() == '13':
                count_10_1(13, 'тринадцатеричной')
            elif var.get() == 3 and text3.get() == '14':
                count_10_1(14, 'четырнадцатеричной')
            elif var.get() == 3 and text3.get() == '15':
                count_10_1(15, 'пятнадцатеричной')
            elif var.get() == 3 and text3.get() == '16' or var1.get() == 4:
                x = hex(int(text1.get(), 10))[2:].upper()
                lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                font='Arial 18')
                lab4.place(x=30, y=400)
        else:
            Error(change_1="Десятичное", change_2="от 0 до 9(вкл)")

    if var.get() == 4:
        def chek_5(input_name):
            return set(input_name) <= allowed_5

        if chek_5(input_name):
            if var.get() == 4 and text3.get() == '2' or var1.get() == 0:
                count_in_2()
            elif var.get() == 4 and text3.get() == '3' or var1.get() == 1:
                count_11_16(3, 'троичной')
            elif var.get() == 4 and text3.get() == '4':
                count_11_16(4, 'четверичной')
            elif var.get() == 4 and text3.get() == '5':
                count_11_16(5, 'пятеричной')
            elif var.get() == 4 and text3.get() == '6':
                count_11_16(6, 'шестеричной')
            elif var.get() == 4 and text3.get() == '7':
                count_11_16(7, 'семеричной')
            elif var.get() == 4 and text3.get() == '8' or var1.get() == 2:
                count_11_16(8, 'восьмеричной')
            elif var.get() == 4 and text3.get() == '9':
                count_11_16(9, 'девятеричной')
            elif var.get() == 4 and text3.get() == '10' or var1.get() == 3:
                count_10_2()
            elif var.get() == 4 and text3.get() == '11':
                count_11_16(11, 'одинадцатеричной')
            elif var.get() == 4 and text3.get() == '12':
                count_11_16(12, 'двенадцатеричной')
            elif var.get() == 4 and text3.get() == '13':
                count_11_16(13, 'тринадцатеричной')
            elif var.get() == 4 and text3.get() == '14':
                count_11_16(14, 'четырнадцатеричной')
            elif var.get() == 4 and text3.get() == '15':
                count_11_16(15, 'пятнадцатеричной')
            elif var.get() == 4 and text3.get() == '16' or var1.get() == 4:
                lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(text1.get()),
                                font='Arial 18')
                lab4.place(x=30, y=400)
        else:
            Error(change_1="Шестнадцатеричное", change_2="от 0 до 16(вкл) и буквы A, B, C, D, E, F")

    if var.get() == 5:
        if text2.get() == '2':

            def chek_1(input_name):
                return set(input_name) <= allowed

            if chek_1(input_name):
                if text2.get() == '2' and text3.get() == '2' or var1.get() == 0:  # из двоичной в двоичную
                    lab4 = tk.Label(win, text=f'Число в двоичной системе:' + str(text1.get()), font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '2' and text3.get() == '3' or var1.get() == 1:  # из двоичной в троичную
                    count_0_9(2, 3, 'троичной')
                elif text2.get() == '2' and text3.get() == '4':
                    count_0_9(2, 4, 'четверичной')
                elif text2.get() == '2' and text3.get() == '5':
                    count_0_9(2, 5, 'пятеричной')
                elif text2.get() == '2' and text3.get() == '6':
                    count_0_9(2, 6, 'шестеричной')
                elif text2.get() == '2' and text3.get() == '7':
                    count_0_9(2, 7, 'семеричной')
                elif text2.get() == '2' and text3.get() == '8' or var1.get() == 2:  # из двоичной в восьмеричную
                    count_0_9(2, 8, 'восьмеричной')
                elif text2.get() == '2' and text3.get() == '9':
                    count_0_9(2, 9, 'девятеричной')
                elif text2.get() == '2' and text3.get() == '10' or var1.get() == 3:  # из двоичной в десятичную
                    count_10(2)
                elif text2.get() == '2' and text3.get() == '11':
                    count_0_9(2, 11, 'одинадцатеричной')
                elif text2.get() == '2' and text3.get() == '12':
                    count_0_9(2, 12, 'двенадцатеричной')
                elif text2.get() == '2' and text3.get() == '13':
                    count_0_9(2, 13, 'тринадцатеричной')
                elif text2.get() == '2' and text3.get() == '14':
                    count_0_9(2, 14, 'четырнадцатеричной')
                elif text2.get() == '2' and text3.get() == '15':
                    count_0_9(2, 15, 'пятнадцатеричной')
                elif text2.get() == '2' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 2))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1="Двоичное", change_2="0 и 1")
        if text2.get() == '3':

            def chek_2(input_name):
                return set(input_name) <= allowed_2

            if chek_2(input_name):
                if text2.get() == '3' and text3.get() == '2' or var1.get() == 0:  # из троичной в двоичную
                    count_0_9(3, 2, 'двоичной')
                elif text2.get() == '3' and text3.get() == '3' or var1.get() == 1:  # из троичной в троичную
                    lab4 = tk.Label(win, text=f'Число в троичной системе:' + str(text1.get()),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '3' and text3.get() == '4':
                    count_0_9(3, 4, 'четверичной')
                elif text2.get() == '3' and text3.get() == '5':
                    count_0_9(3, 5, 'пятеричной')
                elif text2.get() == '3' and text3.get() == '6':
                    count_0_9(3, 6, 'шестеричной')
                elif text2.get() == '3' and text3.get() == '7':
                    count_0_9(3, 7, 'семеричной')
                elif text2.get() == '3' and text3.get() == '8' or var1.get() == 2:  # из троичной в восьмеричную
                    count_0_9(3, 8, 'восьмеричной')
                elif text2.get() == '3' and text3.get() == '9':
                    count_0_9(3, 9, 'девятерчной')
                elif text2.get() == '3' and text3.get() == '10' or var1.get() == 3:  # из троичной в десятичную
                    count_10(3)
                elif text2.get() == '3' and text3.get() == '11':
                    count_0_9(3, 11, 'одинадцатеричной')
                elif text2.get() == '3' and text3.get() == '12':
                    count_0_9(3, 12, 'двенадцатеричной')
                elif text2.get() == '3' and text3.get() == '13':
                    count_0_9(3, 13, 'тринадцатеричной')
                elif text2.get() == '3' and text3.get() == '14':
                    count_0_9(3, 14, 'четырнадцатеричной')
                elif text2.get() == '3' and text3.get() == '15':
                    count_0_9(3, 15, 'пятнадцатеричной')
                elif text2.get() == '3' and text3.get() == '16' or var1.get() == 4:  # из троичной в шестнадцатеричную
                    x = hex(int(text1.get(), 3))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                else:
                    Error(change_1="Троичное", change_2="0, 1 и 2")
        if text2.get() == '4':
            def chek_6(input_name):
                return set(input_name) <= allowed_6

            if chek_6(input_name):
                if text2.get() == '4' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(4, 2, 'двоичной')
                elif text2.get() == '4' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(4, 3, 'троичной')
                elif text2.get() == '4' and text3.get() == '4':
                    lab4 = tk.Label(win, text=f'Число в четверичной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '4' and text3.get() == '5':
                    count_0_9(4, 5, 'пятеричной')
                elif text2.get() == '4' and text3.get() == '6':
                    count_0_9(4, 6, 'шестеричной')
                elif text2.get() == '4' and text3.get() == '7':
                    count_0_9(4, 7, 'семеричной')
                elif text2.get() == '4' and text3.get() == '8' or var1.get() == 2:
                    count_0_9(4, 8, 'восьмеричной')
                elif text2.get() == '4' and text3.get() == '9':
                    count_0_9(4, 9, 'девятеричной')
                elif text2.get() == '4' and text3.get() == '10' or var1.get() == 3:
                    count_10(4)
                elif text2.get() == '4' and text3.get() == '11':
                    count_0_9(4, 11, 'одинадцатеричной')
                elif text2.get() == '4' and text3.get() == '12':
                    count_0_9(4, 12, 'двенадцатеричной')
                elif text2.get() == '4' and text3.get() == '13':
                    count_0_9(4, 13, 'тринадцатеричной')
                elif text2.get() == '4' and text3.get() == '14':
                    count_0_9(4, 14, 'четырнадцатеричной')
                elif text2.get() == '4' and text3.get() == '15':
                    count_0_9(4, 15, 'пятнадцатеричной')
                elif text2.get() == '4' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 4))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='четверичное', change_2='от 0 до 3(вкл)')
        if text2.get() == '5':
            def chek_7(input_name):
                return set(input_name) <= allowed_7

            if chek_7(input_name):
                if text2.get() == '5' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(5, 2, 'двоичной')
                elif text2.get() == '5' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(5, 3, 'троичной')
                elif text2.get() == '5' and text3.get() == '4':
                    count_0_9(5, 4, 'четверичной')
                elif text2.get() == '5' and text3.get() == '5':
                    lab4 = tk.Label(win, text=f'Число в пятеричной системе:' + str(''.join(text2.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '5' and text3.get() == '6':
                    count_0_9(5, 6, 'шестеричной')
                elif text2.get() == '5' and text3.get() == '7':
                    count_0_9(5, 7, 'семеричной')
                elif text2.get() == '5' and text3.get() == '8' or var1.get() == 2:
                    count_0_9(5, 8, 'восьмеричной')
                elif text2.get() == '5' and text3.get() == '9':
                    count_0_9(5, 9, 'девятеричной')
                elif text2.get() == '5' and text3.get() == '10' or var1.get() == 3:
                    count_10(5)
                elif text2.get() == '5' and text3.get() == '11':
                    count_0_9(5, 11, 'одинадцатеричной')
                elif text2.get() == '5' and text3.get() == '12':
                    count_0_9(5, 12, 'двенадцатеричной')
                elif text2.get() == '5' and text3.get() == '13':
                    count_0_9(5, 13, 'тринадцатеричной')
                elif text2.get() == '5' and text3.get() == '14':
                    count_0_9(5, 14, 'четырнадцатеричной')
                elif text2.get() == '5' and text3.get() == '15':
                    count_0_9(5, 15, 'пятнадцатеричной')
                elif text2.get() == '5' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 5))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='пятеричное', change_2='от 0 до 4(вкл)')
        if text2.get() == '6':
            def chek_8(input_name):
                return set(input_name) <= allowed_8

            if chek_8(input_name):
                if text2.get() == '6' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(6, 2, 'двоичной')
                elif text2.get() == '6' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(6, 3, 'троичной')
                elif text2.get() == '6' and text3.get() == '4':
                    count_0_9(6, 4, 'четверичной')
                elif text2.get() == '6' and text3.get() == '5':
                    count_0_9(6, 5, 'пятеричной')
                elif text2.get() == '6' and text3.get() == '6':
                    lab4 = tk.Label(win, text=f'Число в шестеричной системе:' + str(''.join(text2.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '6' and text3.get() == '7':
                    count_0_9(6, 7, 'семеричной')
                elif text2.get() == '6' and text3.get() == '8' or var1.get() == 2:
                    count_0_9(6, 8, 'восьмеричной')
                elif text2.get() == '6' and text3.get() == '9':
                    count_0_9(6, 9, 'девятеричной')
                elif text2.get() == '6' and text3.get() == '10' or var1.get() == 3:
                    count_10(6)
                elif text2.get() == '6' and text3.get() == '11':
                    count_0_9(6, 11, 'одинадцатеричной')
                elif text2.get() == '6' and text3.get() == '12':
                    count_0_9(6, 12, 'двенадцатеричной')
                elif text2.get() == '6' and text3.get() == '13':
                    count_0_9(6, 13, 'тринадцатеричной')
                elif text2.get() == '6' and text3.get() == '14':
                    count_0_9(6, 14, 'четырнадцатеричной')
                elif text2.get() == '6' and text3.get() == '15':
                    count_0_9(6, 15, 'пятнадцатеричной')
                elif text2.get() == '6' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 6))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='шестеричное', change_2='от 0 до 5(вкл)')
        if text2.get() == '7':
            def chek_9(input_name):
                return set(input_name) <= allowed_9

            if chek_9(input_name):
                if text2.get() == '7' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(7, 2, 'двоичной')
                elif text2.get() == '7' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(7, 3, 'троичной')
                elif text2.get() == '7' and text3.get() == '4':
                    count_0_9(7, 3, 'четверичной')
                elif text2.get() == '7' and text3.get() == '5':
                    count_0_9(7, 5, 'пятеричной')
                elif text2.get() == '7' and text3.get() == '6':
                    count_0_9(7, 6, 'шестеричной')
                elif text2.get() == '7' and text3.get() == '7':
                    lab4 = tk.Label(win, text=f'Число в семеричной системе:' + str(''.join(text2.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '7' and text3.get() == '8' or var1.get() == 2:
                    count_0_9(7, 8, 'восьмеричной')
                elif text2.get() == '7' and text3.get() == '9':
                    count_0_9(7, 9, 'девятеричной')
                elif text2.get() == '7' and text3.get() == '10' or var1.get() == 3:
                    count_10(7)
                elif text2.get() == '7' and text3.get() == '11':
                    count_0_9(7, 11, 'одинадцатеричной')
                elif text2.get() == '7' and text3.get() == '12':
                    count_0_9(7, 12, 'двенадцатеричной')
                elif text2.get() == '7' and text3.get() == '13':
                    count_0_9(7, 13, 'тринадцатеричной')
                elif text2.get() == '7' and text3.get() == '14':
                    count_0_9(7, 14, 'четырнадцатеричной')
                elif text2.get() == '7' and text3.get() == '15':
                    count_0_9(7, 15, 'пятнадцатеричной')
                elif text2.get() == '7' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 7))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='семеричной', change_2='от 0 до 6(вкл)')
        if text2.get() == '8':
            def chek_3(input_name):
                return set(input_name) <= allowed_3

            if chek_3(input_name):
                if text2.get() == '8' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(8, 2, 'двоичной')
                elif text2.get() == '8' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(8, 3, 'троичной')
                elif text2.get() == '8' and text3.get() == '4':
                    count_0_9(8, 3, 'четверичной')
                elif text2.get() == '8' and text3.get() == '5':
                    count_0_9(8, 5, 'пятеричной')
                elif text2.get() == '8' and text3.get() == '6':
                    count_0_9(8, 6, 'шестеричной')
                elif text2.get() == '8' and text3.get() == '7':
                    count_0_9(8, 7, 'семеричной')
                elif text2.get() == '8' and text3.get() == '8' or var1.get() == 2:
                    lab4 = tk.Label(win, text=f'Число в восьмеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '8' and text3.get() == '9':
                    count_0_9(8, 9, 'девятеричной')
                elif text2.get() == '8' and text3.get() == '10' or var1.get() == 3:
                    count_10(8)
                elif text2.get() == '8' and text3.get() == '11':
                    count_0_9(8, 11, 'одинадцатеричной')
                elif text2.get() == '8' and text3.get() == '12':
                    count_0_9(8, 12, 'двенадцатеричной')
                elif text2.get() == '8' and text3.get() == '13':
                    count_0_9(8, 13, 'тринадцатеричной')
                elif text2.get() == '8' and text3.get() == '14':
                    count_0_9(8, 14, 'четырнадцатеричной')
                elif text2.get() == '8' and text3.get() == '15':
                    count_0_9(8, 15, 'пятнадцатеричной')
                elif text2.get() == '8' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 8))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='восьмеричное', change_2='от 0 до 7(вкл)')
        if text2.get() == '9':
            def chek_A(input_name):
                return set(input_name) <= allowed_A

            if chek_A(input_name):
                if text2.get() == '9' and text3.get() == '2' or var1.get() == 0:
                    count_0_9(9, 2, 'двоичной')
                elif text2.get() == '9' and text3.get() == '3' or var1.get() == 1:
                    count_0_9(9, 3, 'троичной')
                elif text2.get() == '9' and text3.get() == '4':
                    count_0_9(9, 3, 'четверичной')
                elif text2.get() == '9' and text3.get() == '5':
                    count_0_9(9, 5, 'пятеричной')
                elif text2.get() == '9' and text3.get() == '6':
                    count_0_9(9, 6, 'шестеричной')
                elif text2.get() == '9' and text3.get() == '7':
                    count_0_9(9, 7, 'семеричной')
                elif text2.get() == '9' and text3.get() == '8' or var1.get() == 2:
                    count_0_9(9, 8, 'восьмеричной')
                elif text2.get() == '9' and text3.get() == '9':
                    lab4 = tk.Label(win, text=f'Число в девятеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '9' and text3.get() == '10' or var1.get() == 3:
                    count_10(9)
                elif text2.get() == '9' and text3.get() == '11':
                    count_0_9(9, 11, 'одинадцатеричной')
                elif text2.get() == '9' and text3.get() == '12':
                    count_0_9(9, 12, 'двенадцатеричной')
                elif text2.get() == '9' and text3.get() == '13':
                    count_0_9(9, 13, 'тринадцатеричной')
                elif text2.get() == '9' and text3.get() == '14':
                    count_0_9(9, 14, 'четырнадцатеричной')
                elif text2.get() == '9' and text3.get() == '15':
                    count_0_9(9, 15, 'пятнадцатеричной')
                elif text2.get() == '9' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 9))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='девятеричное', change_2='от 0 до 8(вкл)')
        if text2.get() == '10':
            def chek_4(input_name):
                return set(input_name) <= allowed_4

            if chek_4(input_name):
                if text2.get() == '10' and text3.get() == '2' or var1.get() == 0:
                    count_10_1(2, 'двоичной')
                elif text2.get() == '10' and text3.get() == '3' or var1.get() == 1:
                    count_10_1(3, 'троичной')
                elif text2.get() == '10' and text3.get() == '4':
                    count_10_1(4, 'четверичной')
                elif text2.get() == '10' and text3.get() == '5':
                    count_10_1(5, 'пятеричной')
                elif text2.get() == '10' and text3.get() == '6':
                    count_10_1(6, 'шестеричной')
                elif text2.get() == '10' and text3.get() == '7':
                    count_10_1(7, 'семеричной')
                elif text2.get() == '10' and text3.get() == '8' or var1.get() == 2:
                    count_10_1(8, 'восьмеричной')
                elif text2.get() == '10' and text3.get() == '9':
                    count_10_1(9, 'девятеричной')
                elif text2.get() == '10' and text3.get() == '10' or var1.get() == 3:
                    lab4 = tk.Label(win, text=f'Число в десятеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '10' and text3.get() == '11':
                    count_10_1(11, 'одинадцатеричной')
                elif text2.get() == '10' and text3.get() == '12':
                    count_10_1(12, 'двенадцатеричной')
                elif text2.get() == '10' and text3.get() == '13':
                    count_10_1(13, 'тринадцатеричной')
                elif text2.get() == '10' and text3.get() == '14':
                    count_10_1(14, 'четырнадцатеричной')
                elif text2.get() == '10' and text3.get() == '15':
                    count_10_1(15, 'пятнадцатеричной')
                elif text2.get() == '10' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 10))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='десятеричное', change_2='от 0 до 9(вкл)')
        if text2.get() == '11':
            def chek_B(input_name):
                return set(input_name) <= allowed_B

            if chek_B(input_name):
                if text2.get() == '11' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '11' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '11' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '11' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '11' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '11' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '11' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '11' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '11' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '11' and text3.get() == '11':
                    lab4 = tk.Label(win, text=f'Число в одинадцатеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '11' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '11' and text3.get() == '13':
                    count_11_16(13, 'тринадцатеричной')
                elif text2.get() == '11' and text3.get() == '14':
                    count_11_16(14, 'четырнадцатеричной')
                elif text2.get() == '11' and text3.get() == '15':
                    count_11_16(15, 'пятнадцатеричной')
                elif text2.get() == '11' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 11))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='одинадцатеричное', change_2='от 0 до 9(вкл) и букву A')
        if text2.get() == '12':
            def chek_C(input_name):
                return set(input_name) <= allowed_C

            if chek_C(input_name):
                if text2.get() == '12' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '12' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '12' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '12' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '12' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '12' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '12' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '12' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '12' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '12' and text3.get() == '11':
                    count_11_16(11, 'одинадцатеричной')
                elif text2.get() == '12' and text3.get() == '12':
                    lab4 = tk.Label(win, text=f'Число в двенадцатеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '12' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '12' and text3.get() == '13':
                    count_11_16(13, 'тринадцатеричной')
                elif text2.get() == '12' and text3.get() == '14':
                    count_11_16(14, 'четырнадцатеричной')
                elif text2.get() == '12' and text3.get() == '15':
                    count_11_16(15, 'пятнадцатеричной')
                elif text2.get() == '12' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 12))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='двенадцатеричное', change_2='от 0 до 9(вкл) и буквы A и B')
        if text2.get() == '13':
            def chek_D(input_name):
                return set(input_name) <= allowed_D

            if chek_D(input_name):
                if text2.get() == '13' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '13' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '13' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '13' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '13' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '13' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '13' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '13' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '13' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '13' and text3.get() == '11':
                    count_11_16(11, 'одинадцатеричной')
                elif text2.get() == '13' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '13' and text3.get() == '13':
                    lab4 = tk.Label(win, text=f'Число в тринадцатеричной системе:' + str(text1.get()),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '13' and text3.get() == '14':
                    count_11_16(14, 'четырнадцатеричной')
                elif text2.get() == '13' and text3.get() == '15':
                    count_11_16(15, 'пятнадцатеричной')
                elif text2.get() == '13' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 13))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='тринадцатеричное', change_2='от 0 до 9(вкл) и буквы A,B и C')
        if text2.get() == '14':
            def chek_E(input_name):
                return set(input_name) <= allowed_E

            if chek_E(input_name):
                if text2.get() == '14' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '14' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '14' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '14' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '14' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '14' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '14' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '14' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '14' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '14' and text3.get() == '11':
                    count_11_16(11, 'одинадцатеричной')
                elif text2.get() == '14' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '14' and text3.get() == '13':
                    count_11_16(13, 'тринадцатеричной')
                elif text2.get() == '14' and text3.get() == '14':
                    lab4 = tk.Label(win, text=f'Число в четырнадцатеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '14' and text3.get() == '15':
                    count_11_16(15, 'пятнадцатеричной')
                elif text2.get() == '14' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 14))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='четырнадцатеричное', change_2='от 0 до 9(вкл) и буквы A,B,C и D')
        if text2.get() == '15':
            def chek_F(input_name):
                return set(input_name) <= allowed_F

            if chek_F(input_name):
                if text2.get() == '15' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '15' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '15' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '15' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '15' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '15' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '15' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '15' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '15' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '15' and text3.get() == '11':
                    count_11_16(11, 'одинадцатеричной')
                elif text2.get() == '15' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '15' and text3.get() == '13':
                    count_11_16(13, 'тринадцатеричной')
                elif text2.get() == '15' and text3.get() == '14':
                    count_11_16(14, 'четырнадцатеричной')
                elif text2.get() == '15' and text3.get() == '15':
                    lab4 = tk.Label(win, text=f'Число в пятнадцатеричной системе:' + str(''.join(text1.get())),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
                elif text2.get() == '15' and text3.get() == '16' or var1.get() == 4:
                    x = hex(int(text1.get(), 15))[2:].upper()
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(x),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='пятнадцатеричное', change_2='от 0 до 9(вкл) и буквы A,B,C,D и E')
        if text2.get() == '16':
            def chek_5(input_name):
                return set(input_name) <= allowed_5

            if chek_5(input_name):
                if text2.get() == '16' and text3.get() == '2' or var1.get() == 0:
                    count_in_2()
                elif text2.get() == '16' and text3.get() == '3' or var1.get() == 1:
                    count_11_16(3, 'троичной')
                elif text2.get() == '16' and text3.get() == '4':
                    count_11_16(4, 'четверичной')
                elif text2.get() == '16' and text3.get() == '5':
                    count_11_16(5, 'пятеричной')
                elif text2.get() == '16' and text3.get() == '6':
                    count_11_16(6, 'шестеричной')
                elif text2.get() == '16' and text3.get() == '7':
                    count_11_16(7, 'семеричной')
                elif text2.get() == '16' and text3.get() == '8' or var1.get() == 2:
                    count_11_16(8, 'восьмеричной')
                elif text2.get() == '16' and text3.get() == '9':
                    count_11_16(9, 'девятеричной')
                elif text2.get() == '16' and text3.get() == '10' or var1.get() == 3:
                    count_10_2()
                elif text2.get() == '16' and text3.get() == '11':
                    count_11_16(11, 'одинадцатеричной')
                elif text2.get() == '16' and text3.get() == '12':
                    count_11_16(12, 'двенадцатеричной')
                elif text2.get() == '16' and text3.get() == '13':
                    count_11_16(13, 'тринадцатеричной')
                elif text2.get() == '16' and text3.get() == '14':
                    count_11_16(14, 'четырнадцатеричной')
                elif text2.get() == '16' and text3.get() == '15':
                    count_11_16(14, 'пятнадцатеричной')
                elif text2.get() == '16' and text3.get() == '16' or var1.get() == 4:
                    lab4 = tk.Label(win, text=f'Число в шестнадцатеричной системе:' + str(text1.get()),
                                    font='Arial 18')
                    lab4.place(x=30, y=400)
            else:
                Error(change_1='шестнадцатеричное', change_2='от 0 до 9(вкл) и буквы A,B,C,D,E,F')


def deleted():
    global lab4
    lab4.destroy()


def sum_funks():
    deleted()
    count()


@eel.expose
def inf():
    eel.init('web')
    eel.start("inf.html", size=(800, 900))


def ent_1():
    text2.place(x=150, y=340)


def ent_2():
    text3.place(x=500, y=340)


trans = tk.Button(win,
                  text='перевод',
                  command=sum_funks,
                  width='13')

help_setting = tk.Button(win,
                         text='Информация',
                         font='Arial 8',
                         width='15',
                         command=inf)

lab1 = tk.Label(win,  # создание текста"введите число"
                text="Введите число:",
                font='Arial 19', )

text1 = tk.Entry(win,  # создание поля ввода
                 font='Arial 17',  # создание поля ввода
                 width='37')

text2 = tk.Entry(win,
                 font='Arial 13',
                 width='5')

text3 = tk.Entry(win,
                 font='Arial 13',
                 width='5')
trans.place(x=690, y=10)
help_setting.place(x=690, y=40)
lab1.place(x=10, y=10)
text1.place(x=200, y=10)

lab2 = tk.Label(win, text='Исходная система счисления:', font='Arial 15',
                padx='25').place(x=50, y=130)

var = tk.IntVar()
var.set(0)
inp1 = tk.Radiobutton(win, text="двоичная система", command=lambda: text2.place_forget(),
                      variable=var, value=0, padx=70, font='Arial 14')
inp2 = tk.Radiobutton(win, text="троичная система", command=lambda: text2.place_forget(),
                      variable=var, value=1, padx=70, font='Arial 14')
inp3 = tk.Radiobutton(win, text="восьмеричная система", command=lambda: text2.place_forget(),
                      variable=var, value=2, padx=70, font='Arial 14')
inp4 = tk.Radiobutton(win, text='десятичная система', command=lambda: text2.place_forget(),
                      variable=var, value=3, padx=70, font='Arial 14')
inp5 = tk.Radiobutton(win, text='шестнадцатеричная система', command=lambda: text2.place_forget(),
                      variable=var, value=4, padx=70, font='Arial 14')
inp11 = tk.Radiobutton(win, text='Другая', command=ent_1,
                       variable=var, value=5, padx=70, font='Arial 14')

inp1.place(x=50, y=160)
inp2.place(x=50, y=190)
inp3.place(x=50, y=220)
inp4.place(x=50, y=250)
inp5.place(x=50, y=280)
inp11.place(x=50, y=310)

lab3 = tk.Label(win, text='Конечная система счисления:', font='Arial 15').place(x=400, y=130)

var1 = tk.IntVar()
var1.set(0)
inp6 = tk.Radiobutton(win, text="двоичная система", command=lambda: text3.place_forget(),
                      variable=var1, value=0, padx=70, font='Arial 14')
inp7 = tk.Radiobutton(win, text="троичная система", command=lambda: text3.place_forget(),
                      variable=var1, value=1, padx=70, font='Arial 14')
inp8 = tk.Radiobutton(win, text="восьмеричная система", command=lambda: text3.place_forget(),
                      variable=var1, value=2, padx=70, font='Arial 14')
inp9 = tk.Radiobutton(win, text='десятичная система', command=lambda: text3.place_forget(),
                      variable=var1, value=3, padx=70, font='Arial 14')
inp10 = tk.Radiobutton(win, text='шестнадцатеричная система', command=lambda: text3.place_forget(),
                       variable=var1, value=4, padx=70, font='Arial 14')
inp12 = tk.Radiobutton(win, text='Другая', command=ent_2,
                       variable=var1, value=5, padx=70, font='Arial 14')

inp6.place(x=400, y=160)
inp7.place(x=400, y=190)
inp8.place(x=400, y=220)
inp9.place(x=400, y=250)
inp10.place(x=400, y=280)
inp12.place(x=400, y=310)
win.mainloop()
