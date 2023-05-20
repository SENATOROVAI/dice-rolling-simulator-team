from dice import roll_dice

while True:
    num_sides = (input('Введите число: '))
    if not num_sides.isdigit():
        print("Ошибка вы ввели не число!!!")
    else:
        print('Число принято!')
    roll_result = roll_dice(num_sides=6)
    print("You rolled a " + str(roll_result) + "!")
    play_again = input("Roll again? (y/n): ")
    if play_again.lower() != "y":
        print("Давай отдохнем!")
