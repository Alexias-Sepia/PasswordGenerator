from tkinter import *
import random

up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@%&!'

all_chars = up + low + numbers + symbols

def generate_password():
    try:
        length = int(loginput.get())
        if length <= 0:
            loginfo.delete(0, END)
            loginfo.insert(0, "Введите положительное число")
            return
        if length > len(all_chars):
            loginfo.delete(0, END)
            loginfo.insert(0, f"Максимум: {len(all_chars)}")
            return
        password = "".join(random.sample(all_chars, length))
        loginfo.delete(0, END)
        loginfo.insert(0, password)
    except ValueError:
        loginfo.delete(0, END)
        loginfo.insert(0, "Введите число")

root = Tk()
root.title("PassGen")
root.geometry("300x200")

frame = Frame(root, bg="lightgray")
frame.place( relheight=1, relwidth=1)

title = Label(frame, text="Генератор паролей", bg="lightgray", font=("Arial", 14))
title.pack(pady=10)

title = Label(frame, text="Введите длину пароля: ", bg="lightgray", font=("Arial", 11))
title.pack()

loginput = Entry(frame, bg="white", font=("Arial", 12))
loginput.pack(pady=5)

btn_generate = Button(frame, text="Сгенерировать", command=generate_password)
btn_generate.pack(pady=5)

loginfo = Entry(frame, bg="white", font=("Arial", 12))
loginfo.pack(pady=5)

root.mainloop()