# Напишите программу, в которой пользователь вводит число от 0 до 9 включительно,
# а программа выводит название введённого числа, а если второй входной аргумент type имеет значение bin, oct,hex,
# то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму.
# Предусмотреть проверку корректности введённого пользователем значения. При реализации должны использоваться декораторы.
# При реализации должны использоваться декораторы (но можно обойтись и без них). Предусмотрите обработку исключительных ситуаций.
# Напишите тесты с использованием assert.

# Напишите класс для обработки исключений RangeException, для обработки исключения,
# которое возникает в ситуации, когда вводится число не из описанного в условии диапазона;

# Для программы, сделанной в рамках лабораторной работы 1 и 2, реализуйте с использованием механизма декораторов (предпочтительно)
# или без него (в этом случае будет необходимо использовать еще один аргумент) функционал для сохранения истории вычислений функции в файл.

# Выполнены: Лабораторная работа 1, Лабораторная работа 2, Самостоятельная работа 1.

'''
RangeException
'''

class RangeException(Exception):
    def __init__(self, text):
        RangeException.txt = text

numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
types = ['bin', 'oct', 'hex']

a = input("Введите один из типов hex, oct, bin:")
b = input("Введите число от 0 до 9:")

'''
Создаю функцию getStringNumber
'''

def getStringNumber(x, num_type):
    if num_type in types and num_type != "" and x in range(10):
        if (num_type == 'bin'):
            return bin(x)
        elif (num_type == 'oct'):
            return oct(x)
        elif (num_type == 'hex'):
            return hex(x)
        else:
            return 'Ok'
    if x in range(10):
        return numbers[x]
    else:
        return "Неверное значение"

print(getStringNumber(b, a))


try:
    num = int(input("Введите число от 0 до 9:"))
    if ((num < 0) | (num > 9)):
        raise RangeException(
            'Введено неверное значение числа, не соответсвует интервалу/типу RangeException')  # если не те цифры
    else:
        print(getStringNumber(num, a))
        with open('FileP.txt', 'a') as f:
            f.write('Numbers:'"\n" + str(num) + 'Type:' + str(a) + "\n")
except RangeException:
    print(RangeException.txt)
except ValueError:
    print("Введено неверное значение числа, не соответсвует интервалу/типу ValueError")

def test():
    assert getStringNumber(9, 'oct') == '0o11'
    assert getStringNumber('qw', 'oct') == 'Неверное значение'
    assert getStringNumber(5, 'qwer') == 'пять'


test()