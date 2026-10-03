while True:
    try:
        number = int(input("введите трёхзначное число:"))
        if 100<= number <= 999:
            break
        else:
            print("ошибка: нужно трёхзначное число.")
            except ValueError:
            print("ошибка: введите целое число, а не слова.")

            units = number % 10
            tens = (number // 10) % 10

            print(units)
            print(tens)
