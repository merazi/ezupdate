import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Insert Data')

# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=0, column=0, padx=10, pady=5)

# title
title_label = ttk.Label(master=input_frame, text="Data Entry", font="Calibri 24 bold").grid(row=0, column=0, padx=10, pady=5)

names_label = ttk.Label(master=input_frame, text="Nombres").grid(row=1, column=0, padx=10, pady=5)
names = ttk.Entry(master=input_frame).grid(row=1, column=1, padx=10, pady=5)

lnames_label = ttk.Label(master=input_frame, text="Apellidos").grid(row=2, column=0, padx=10, pady=5)
lnames = ttk.Entry(master=input_frame).grid(row=2, column=1, padx=10, pady=5)

gender_label = ttk.Label(master=input_frame, text="Sexo").grid(row=3, column=0, padx=10, pady=5)
gender = ttk.Combobox(master=input_frame)
# dropdown menu selections
gender_options = ("M","F")
gender['values'] = gender_options
gender.grid(row=3, column=1, padx=10, pady=5)

birthday_label = ttk.Label(master=input_frame, text="Fecha Nacimiento").grid(row=4, column=0, padx=10, pady=5)
birthday = ttk.Entry(master=input_frame).grid(row=4, column=1, padx=10, pady=5)

email_label = ttk.Label(master=input_frame, text="Email").grid(row=5, column=0, padx=10, pady=5)
email = ttk.Entry(master=input_frame).grid(row=5, column=1, padx=10, pady=5)

phone_label = ttk.Label(master=input_frame, text="Telefono").grid(row=6, column=0, padx=10, pady=5)
phone = ttk.Entry(master=input_frame).grid(row=6, column=1, padx=10, pady=5)

address_label = ttk.Label(master=input_frame, text="Direccion").grid(row=7, column=0, padx=10, pady=5)
address = ttk.Entry(master=input_frame).grid(row=7, column=1, padx=10, pady=5)

civil_status_label = ttk.Label(master=input_frame, text="Estado Civil").grid(row=8, column=0, padx=10, pady=5)
civil_status = ttk.Combobox(master=input_frame)
civil_status_options = ("Casado","Soltero","Divorciado")
civil_status['values'] = civil_status_options
civil_status.grid(row=8, column=1, padx=10, pady=5)

submit = ttk.Button(master=input_frame, text="Submit").grid(row=9, column=0, padx=10, pady=5)

# log fields

userr = ttk.Entry(master=input_frame)
useru = ttk.Entry(master=input_frame)
dater = ttk.Entry(master=input_frame)
dateu = ttk.Entry(master=input_frame)
status = ttk.Entry(master=input_frame)
timer = ttk.Entry(master=input_frame)
timeu = ttk.Entry(master=input_frame)

userr_label = ttk.Label(master=input_frame, text="userr")
useru_label = ttk.Label(master=input_frame, text="useru")
dateu_label = ttk.Label(master=input_frame, text="dateu")
dater_label = ttk.Label(master=input_frame, text="dater")
status_label = ttk.Label(master=input_frame, text="estado")
timer_label = ttk.Label(master=input_frame, text="timer")
timeu_label = ttk.Label(master=input_frame, text="timeu")

# run window
window.mainloop()
