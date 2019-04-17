# Напишите программу, в которой пользователь вводит число от 0 до 9 включительно,
# а программа выводит название введённого числа, а если второй входной аргумент type имеет значение bin, oct,hex,
# то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму.
# Предусмотреть проверку корректности введённого пользователем значения. При реализации должны использоваться декораторы.
# При реализации должны использоваться декораторы (но можно обойтись и без них). Предусмотрите обработку исключительных ситуаций.
# Напишите тесты с использованием assert.

numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
types = ['bin', 'oct', 'hex']

a = int(input("Введите число от 0 до 9:"))
b = input("Введите один из типов hex, oct, bin:")

def getStringNumber(x, num_type):
    if num_type in types and num_type != "" and x in range(0, 10):
        if (num_type == 'hex'):
            return hex(x)
        elif (num_type == 'oct'):
            return oct(x)
        elif (num_type == 'bin'):
            return bin(x)
        else:
            return 'Ok'

    if x in range(0, 10):
        return numbers[x]
    else:
        return "Неверное значение"

print(getStringNumber(a, b))

def test():
    assert getStringNumber(9, 'oct') == '0o11'
    assert getStringNumber('qw', 'oct') == 'Неверное значение'
    assert getStringNumber(5, 'qwer') == 'пять'

test()