import tkinter as tk
import tkinter.ttk
import os
import sys
import animelist


def parsivanko():
    animelist.main('ivanko4456', new.get())


def parsAHMED():
    animelist.main('AHMED2007RUS', new.get())


def parsuser():

    name = username.get()
    if name != '':
        animelist.main(name, new.get())


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root['bg'] = '#000000'
root.resizable(width=False, height=False)
root.geometry('500x300')
image_path = resource_path("icon.ico")
root.iconbitmap(image_path)
root.title('Shikimori parser')

style = tkinter.ttk.Style(root)
style.theme_use('clam')

frame = tk.Frame(root)
frame.place(relheight=1, relwidth=1)

title = tk.Label(frame, text='Welcome to Shikimori parser', font=40)
title.place(x=140, y=10)

Ibutton = tk.Button(frame, text='Pars ivanko4456', font=40, command=parsivanko)
Ibutton.place(x=50, y=50)

Ibutton = tk.Button(frame, text='Pars AHMED2007RUS', font=40, command=parsAHMED)
Ibutton.place(x=200, y=50)

username = tk.Entry(frame, font=40)
username.place(x=150, y=150)

userbutton = tk.Button(frame, text='Pars user', font=40, command=parsuser)
userbutton.place(x=200, y=200)


new = tk.BooleanVar()
newtable = tk.Checkbutton(frame, text='Создавать новые таблицы', variable=new, onvalue=True, offvalue=False)
newtable.place(x=150, y=235)

root.mainloop()
