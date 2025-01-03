import random
import tkinter as tk
from tkinter import *
m = tk.Tk()
m.title('Crack Password')
m.geometry('200x300')
w = Label(m, text='Enter password to crack:')
w.pack()
e = Entry(m)
e.pack()
label = Label(m, text='',cursor='arrow')
label.pack()
def crack_passowrd(password):
    counter_tries = 0
    set_of_chars = {
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9',
        '$','@','!','#','%','^','&','*','(',')'
    }
    password_guess = ""
    while(password != password_guess):
        for i in range(len(password)):
            password_guess += random.choice(list(set_of_chars))
        print(password_guess)
        label.config(text=counter_tries)
        counter_tries += 1

        if (password_guess != password):
            label.config(text=password_guess)
            password_guess = ""
button = tk.Button(m, text='Crack', width=10, height=0, command=lambda:crack_passowrd(str(e.get())), cursor='dot')
button.pack()
m.mainloop()