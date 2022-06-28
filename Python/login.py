#!/usr/bin/python3
#coding: utf-8

from tkinter import *
user="usuario"
passw="contra"
def get_login():
    u_user=my_entry.get()
    u_passw=my_entry2.get()
    if u_user == user and u_passw == passw:
        print("Inicio de sesion correcto")
        mess = Tk()
        mess.geometry("100x100")
        mess_f = Frame(mess)
        mess_f.pack()
        label = Label(mess_f, width=20, text="Inicio de sesion correcto")
        label.pack()
    else:
        print("Fallo de inicio de sesion")
        mess = Tk()
        mess.geometry("100x100")
        mess_f = Frame(mess)
        mess_f.pack()
        label = Label(mess_f, width=20, text="Fallo inicio de sesion")
        label.pack()
root = Tk()
root.geometry("200x200")
frame = Frame(root)
frame.pack()
label = Label(frame, width=20, text="Username")
label.pack()
my_entry = Entry(frame, width = 20)
my_entry.pack(padx = 5, pady = 5)
label = Label(frame, width=20, text="Password")
label.pack()

my_entry2 = Entry(frame, width = 15, show="*")
my_entry2.pack(padx = 5, pady = 5)
button = Button(frame, text="Log-In", fg="red", command=get_login)
button.pack()

root.mainloop()