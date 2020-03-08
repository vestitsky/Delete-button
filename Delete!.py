import time
from tkinter import *
from pynput.keyboard import Key, Controller
root = Tk()
root.title = ('Delete!')
root.geometry('200x150')
root.wm_attributes("-topmost", 1)
keyboard = Controller()


def delete():
    time.sleep(2)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)


button = Button(root, text='DELETE', bg='green', fg='red', padx=50, pady=50, command=delete).pack()

root.mainloop()