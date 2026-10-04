while True:
    try:
        number = int(input("Введите трёхзначное число: "))
        if 100 <= number <= 999:
            break
        else:
            print("Ошибка: нужно трёхзначное число.")
    except ValueError:
        print("Ошибка: введите целое число, а не слова.")

units = number % 10
tens = (number // 10) % 10

print("Единицы:", units)
print("Десятки:", tens)
