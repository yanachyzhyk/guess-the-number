import random

print("Добро пожаловать в числовую угадайку")


def is_valid(s):
    return s in range(1, 101)


def choose_number(num):
    number = random.randint(1, 100)
    i = 1
    if num == number:
        print("Ты угадал, поздравляю!")
    while num != number:
        if num > number:
            print("Слишком много")
        elif num < number:
            print("Слишком мало")
        num = int(input("Вводи еще: "))
        i += 1
        if i > 5:
            print("Попытки закончились")
            return


num = int(input("Угадай моё число: "))
if is_valid(num) is False:
    print("А может быть все-таки введем целое число от 1 до 100?")
    num = int(input("Угадай моё число: "))
else:
    choose_number(num)


again = "да"


def again_game():
    while again == "да":
        number = random.randint(1, 100)
        choose_number(number)
        again = input("Хочешь еще раз? (да/нет): ")
    print("Пока!")
