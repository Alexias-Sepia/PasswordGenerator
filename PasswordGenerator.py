import random

up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@%&'

all_chars = up + low + numbers + symbols

try:
    length = int(input("Введите длину пароля: "))
    if length > len(all_chars):
        print(f"Максимальная длина пароля без повторений: {len(all_chars)}")
    else:
        password = "".join(random.sample(all_chars, length))
        print("Ваш пароль:", password)
except ValueError:
    print("Пожалуйста, введите корректное число.")

input("Нажмите Enter для выхода...")