#https://www.youtube.com/watch?v=U0RfjVe123A - YouTube Guide
import random
from tkinter import *
from tkinter.ttk import *

main_window = Tk()
main_window.title("Password Generator")
main_window.geometry("300x300")
padd=50
main_window['padx']=padd
poor_password = IntVar()
strong_password = IntVar()

def test():
    strong = "0123456789-=!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    poor = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_password = ""
    duration = poor_password.get()
    entry.delete(0, END)

    if strong_password.get() == 1:
        for i in range(0, duration):
            new_password = new_password + random.choice(poor)
        return new_password
    elif strong_password.get() == 2:
        for i in range(0, duration):
            new_password = new_password + random.choice(strong)
        return new_password
    else:
        print("Select one of the choices.")


def generate_password():
    password_gen = test()
    entry.insert(5, password_gen)


duration_box = Label(text="Length")
duration_box.pack(pady=10)

extent = Combobox(textvariable=poor_password)
extent['values'] = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
extent.current(0)
extent.bind('<<ComboboxSelected>>')
extent.pack(pady=1)

radio_low = Radiobutton(text="Poor", variable=strong_password, value=1)
radio_low.pack(pady=10)
radio_strong = Radiobutton(text="Strong", variable=strong_password, value=2)
radio_strong.pack(pady=5)

generater = Button(text="Generate", command=generate_password)
generater.pack(pady=10)

rand_password = Label(text="Password")
rand_password.pack(pady=10)
entry = Entry()
entry.pack(pady=5)


main_window.mainloop()
