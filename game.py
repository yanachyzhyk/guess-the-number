import random

print("Добро пожаловать в числовую угадайку")


def is_valid(s):
    return s in range(1, 101)

def choose_number(num):
    number = random.randint(1, 100)
    i = 1
    while True:
        
        if num > number:
            print("Слишком много")
        elif num < number:
            print("Слишком мало")
        elif num == number:
            print("Ты угадал, поздравляю!")
            break
            
        num = int(input("Вводи еще: "))
        i += 1
        if i >= 5:
            print("Попытки закончились")
            break
    
            


num = int(input("Угадай моё число: "))
if is_valid(num) is False:
    print("А может быть все-таки введем целое число от 1 до 100?")
    num = int(input("Угадай моё число: "))
else:
    choose_number(num)


again = input("Хочешь еще раз? (да/нет): ")
while again == "да":
    num = int(input("Угадай моё число: "))
    if is_valid(num) is False:
        print("А может быть все-таки введем целое число от 1 до 100?")
        num = int(input("Угадай моё число: "))
    else:
        choose_number(num)
    again = input("Хочешь еще раз? (да/нет): ")
if again != 'да':
    print('Пока!')



