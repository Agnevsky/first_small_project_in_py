# numbers random
import random
num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!\nВведите число от 1 до 100:\n Welcome to the number guessing game!\nEnter a number from 1 to 100:\n')


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def input_num():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('А может быть все-таки введем целое число от 1 до 100? Or maybe we’ll still enter an integer from 1 to 100?')


def compare_num():
    count = 0
    while True:

        n = input_num()
        if n < num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок, Your number is less than the hidden number, try again')
        elif n > num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок, Your number is greater than the hidden number, try again')
        else:
            count += 1
            print('Вы угадали, поздравляем! You guessed it, congratulations!')
            print(
                f'Вам понадобилось {count} попыток! It took you {count} attempts!')
            break


compare_num()
