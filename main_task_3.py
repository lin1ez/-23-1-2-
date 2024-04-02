exchange_rates = {
    "Рубль": 1,
    "Доллар": 1/75.0,
    "Евро": 1/90.0,
    "Юань": 1/11.5,
    "Тенге": 1/0.18,
    "Сум": 1/0.0071,
    "Драм": 1/0.15,
    "Сом": 1/0.86,
    "Белорусский рубль": 1/28.51,
    "Манаты": 1/44.2
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    else:
        amount_in_rubles = amount / exchange_rates[from_currency]
        converted_amount = amount_in_rubles * exchange_rates[to_currency]
        return converted_amount

def print_currency_menu():
    print("Выберите валюту для конвертации:")
    for index, currency in enumerate(exchange_rates.keys(), start=1):
        print(f"{index}. {currency}")

def get_currency_choice():
    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(exchange_rates):
                return choice
            else:
                print("Неверный выбор. Пожалуйста, выберите номер из списка.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

print_currency_menu()
from_currency_index = get_currency_choice()

from_currency = list(exchange_rates.keys())[from_currency_index - 1]

print(f"Введите количество {from_currency} для конвертации:")
amount = float(input("> "))

print_currency_menu()
to_currency_index = get_currency_choice()

to_currency = list(exchange_rates.keys())[to_currency_index - 1]

print(f"Вы выбрали: {from_currency}->{to_currency}")
result = convert_currency(amount, from_currency, to_currency)
print(f"Результат конвертации: {result:.2f}")