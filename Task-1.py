# Task No:1 To Do List
#CodSoft

from tkinter import *
from tkinter import font

win = Tk()
win.maxsize(width=500, height=570)
win.minsize(width=500, height=570)
win.title("To Do List")

label = Label(text="To Do List", bg="black", fg="white", width=37)
label.config(font=('Cursive 16 bold'))
label.place(x=10, y=25)

scrol = Scrollbar(win)
scrol.pack(side=RIGHT, fill=Y)
task_list = Listbox(win, yscrollcommand=scrol.set, font=('Cursive 12'))
scrol.config(command=task_list.yview)
task_list.place(width=200, height=350, x=270, y=110)

label = Label(text="List Items", bg="red", fg="white", width=19)
label.config(font=('Cursive 12 bold'))
label.place(x=273, y=82)

label = Label(text="Operations On List Items", bg="red", fg="white", width=20)
label.config(font=('Cursive 12 bold'))
label.place(x=17, y=80)



def add():
    a = t.get()
    task_list.insert(END, a)
    t.set("")

bt1 = Button(text="Add Task", bg="green", fg="white", font=('Cursive 12 bold'), bd=2, command=add)
bt1.place(x=75, y=170)

def change():
    selected_index = task_list.curselection()
    if selected_index:
        index = selected_index[0]
        new_value = t.get()  # Get the new text from the Entry widget
        task_list.delete(index)  # Remove the selected item
        task_list.insert(index, new_value)  # I
        t.set("")
        
t = StringVar()
entry = Entry(width=25, font=('Cursive 12'), textvariable=t)
entry.place(x=36, y=135, width=180, height=25)

bt2 = Button(text="Update Task", bg="yellow", fg="black", font=('Cursive 12 bold'), bd=2, command=change)
bt2.place(x=63, y=230)

def delt():
    task_list.delete(ANCHOR)

bt3 = Button(text="Delete Task", bg="red", fg="white", font=('Cursive 12 bold'), bd=2, command=delt)
bt3.place(x=71, y=290)

label = Label(text="To Do List", bg="black", fg="white", width=37)
label.config(font=('Cursive 16 bold'))
label.place(x=10, y=500)

win.mainloop()
