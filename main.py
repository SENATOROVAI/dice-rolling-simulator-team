import dice 

while True:
    num_sides = input('Введите число: ')
    if not num_sides.isdigit():
        print("Ошибка вы ввели не число!!!")
        продолжи
    roll_result = названиефайла.roll_dice(int(num_sides))
    print("You rolled a " + str(roll_result) + "!")
    play_again = input("Roll again? (y/n): ")
    if play_again.lower() != "y":
        print("Давай отдохнем!")
#         сделай рефакторинг согласно линтеру flake8
#         во втором файле используй randint(1, num_sides)
