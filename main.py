# Функція task0
def task0(number1, number2):
    result = number1 + number2
    return result

# Функція task1
def task1(number1, znak, number2):
    if znak == '>':
        return number1 > number2
    elif znak == '<':
        return number1 < number2
    elif znak == '>=':
        return number1 >= number2
    elif znak == '<=':
        return number1 <= number2
    elif znak == '==':
        return number1 == number2
    elif znak == '!=':
        return number1 != number2
    else:
        return False  # Якщо введено неправильний знак порівняння

# Функція task2
def task2(text, number):
    return len(text) > number

# Функція task3
def task3(number1, number2, number3):
    return number1 == number2 == number3

# Приклади використання функцій:
print(task0(5, 3))  # Виведе: 8
print(task1(5, '>', 3))  # Виведе: True
print(task2('hello', 3))  # Виведе: True
print(task3(2, 2, 2))  # Виведе: True
