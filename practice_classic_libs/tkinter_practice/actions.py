import tkinter as tk
from tkinter import ttk


def f1():
    print(1)


def f2():
    print(2)


def f3():
    print(3)


root = tk.Tk()

button1 = ttk.Button(root, text='1', command=f1)
button2 = ttk.Button(root, text='2', command=f2)
button3 = ttk.Button(root, text='3', command=f3)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()
