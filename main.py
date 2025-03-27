
# Завдання 1: Перевірка критичних умов
try:
    temperature = float(input("Введіть температуру (°C): "))
    humidity = float(input("Введіть відносну вологість (%): "))

    if temperature > 30 and humidity > 70:
        print("Активація системи охолодження")
    else:
        print("Умови нормальні")
except ValueError:
    print("Некоректне введення. Будь ласка, введіть числові значення.")


# Завдання 2: Валідація введення користувача
try:
    number = int(input("Введіть число від 1 до 100: "))

    if 1 <= number <= 100:
        print("Число у межах від 1 до 100.")
    else:
        print("Число поза межами діапазону.")
except ValueError:
    print("Некоректне введення. Введіть ціле число.")


# Завдання 3: Складний логічний вираз для відбору кандидатів
try:
    age = int(input("Введіть вік кандидата: "))
    experience = int(input("Введіть кількість років досвіду роботи: "))
    qualification = input("Чи має кандидат спеціальну кваліфікацію (True/False)? ").strip().lower() == 'true'

    if 25 <= age <= 50 and (experience >= 3 or qualification):
        print("Кандидат відповідає вимогам")
    else:
        print("Кандидат не відповідає вимогам")
except ValueError:
    print("Некоректне введення. Перевірте правильність даних.")
