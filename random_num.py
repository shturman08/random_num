#Числовая угадайка
import random


print('Добро пожаловать в числовую угадайку')
play = True
while play == True:
    print('Введите правую границу')
    rr = int(input())

    num = random.randint(1, rr)
    count = 0

    def is_valid(text):
        if text.isdigit():
            if 1 <= int(text) <= rr:
                return True
            else:
                return False
        else:
            return False


    while True:
        print('Введите число от 1 до', rr)
        n = input()
        if is_valid(n):
            n = int(n)
            count += 1
            if n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Число попыток', count)
                break
        else:
            print(f"А может быть все-таки введем целое число от 1 до {rr}?")

    print("Хотите сыграть еще раз? (Да, Нет)")
    ans = input().lower()
    if ans == "да": 
        play = True
    else: 
        play = False

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')