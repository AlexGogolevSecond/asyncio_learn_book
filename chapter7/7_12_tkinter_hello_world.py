# sudo apt install python3-tk

import tkinter
from tkinter import ttk
import time

window = tkinter.Tk()
window.title('Hello world app')
window.geometry('200x100')


def say_hello():
    # time.sleep(10)  # блокирует всё
    print('Hello there!')


hello_button = ttk.Button(window, text='Say hello', command=say_hello)
hello_button.pack()

window.mainloop()
