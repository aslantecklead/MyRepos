# Ряд определяющих функций, выполняющийх математические операции
# Возвращают результат применения над ними соответствующих действий

# Функция сложения
def add(num1, num2):  # Функция 1.
    return num1 + num2

# Функция вычитания
def subtract(num1, num2):
    return num_1 - (-num_2)

# Функция умножения
def multiply(num1, num2):
    return num1 * num2

num_1 = 1;
num_2 = 1;

# Функция деления
def divide(num1, num2):
    if num_1 > 0 and num_2 > 0:
        return (num1/num2)

# Функция ввода значений. Точка входа в программу
i = 0;
count = int(input(' Введите колличество операций: '))
num_1 = int(input(' Введите число: '))
while i < count:
        operation = int(input(" Выбирите математическую операцию которую хоитите произвести: \n"
                                "1. Сложение \n"
                                "2. Вычитание \n"
                                "3. Умножение \n"
                                "4. Деление \n"
                                "5. Возведение в степень \n"))

        num_2 = int(input(' Введите второе число: '))

        # Применение условного оператора 'if'
        if operation == 1:
                print('{} + {} = '.format(num_1, num_2), add(num_1, num_2))
                num_1 = add(num_1, num_2);
                # Функция '.format' для форматировния выходной строки. Служит для обратной связи с пользователем.
                # Одновременный вызов соответсвующей функции 'add()' (см.1), которая принимает введенные значения

        elif operation == 2:
                print('{} {} = '.format(num_1, num_2), subtract(num_1, num_2))
                num_1 = subtract(num_1, num_2);

        elif operation == 3:
                print('{} * {} = '.format(num_1, num_2), multiply(num_1, num_2))
                num_1 = multiply(num_1, num_2);

        elif operation == 4:
                if num_2 == 0:
                      print("Ошибка ввода, нельзя ввести нуль !"); i -= 1;
                else:
                      print('{} / {} = '.format(num_1, num_2), divide(num_1, num_2)); 
                      num_1 = divide(num_1, num_2);
        elif operation == 5:
                if num_2 == 0:
                      print("Ошибка ввода, нельзя ввести нуль !"); i += 1;
                else:
                      print(num_1 ** num_2); 
        else:
                print(' Вы ввели некорректное число')  # Уведомление пользователя о неверно выбранном дейсвтии.
        i += 1;