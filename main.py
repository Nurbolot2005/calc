user = int(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
user2 = int(input("Введите второе число: "))

if operator == "+":
    result = user + user2
elif operator == "-":
    result = user - user2
elif operator == "*":
    result = user * user2
elif operator == "/":
    if user2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        result = user / user2
else:
    print("Неверный оператор")

print("Результат:",result )