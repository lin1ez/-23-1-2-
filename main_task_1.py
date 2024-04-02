def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    else:
        return x / y

print("Введите два числа:")
num1 = float(input("> "))
num2 = float(input("> "))

print("Вы ввели числа:", num1, "и", num2)
print("Какое действие выполнить?")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("> ")

if choice == '1':
    print("Результат:", num1, "+", num2, "=", addition(num1, num2))
elif choice == '2':
    print("Результат:", num1, "-", num2, "=", subtraction(num1, num2))
elif choice == '3':
    print("Результат:", num1, "*", num2, "=", multiplication(num1, num2))
elif choice == '4':
    print("Результат:", num1, "/", num2, "=", division(num1, num2))
else:
    print("Неверный выбор")