import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import tkinter.messagebox as mb
import random

def no_action(event):
    btn2.place(x=random.randint(0,300),y=random.randint(0,300))
    
def yes_action(event):
    msg = 'Поздравляю вы пидорас!!!'
    mb.showinfo('Вы пидор',msg)
root = tk.Tk()
root.title('sosal')
root.geometry("500x500+200+200")

root.resizable(False,False)
myfont = tkfont.Font(size=50)
lbl = ttk.Label(master=root,text="Сосал?",font=myfont)
btn1 = ttk.Button(master=root,text="Да",padding=10,command='Click')
btn2 = ttk.Button(master=root,text="Нет",padding=10)
btn1.bind('<Button-1>',yes_action)
btn2.bind('<Enter>',no_action)

lbl.place(x = 150, y = 100)

btn1.place(x = 100, y = 300)
btn2.place(x = 320, y = 300)

root.mainloop()