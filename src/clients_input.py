import tkinter as tk
import build_json as mj
import send_request as sr
from tkinter import ttk
from datetime import datetime

endpoint = "https://eot5nxsbpnt20i2.m.pipedream.net"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # if you need to send a token
}

# window
window = tk.Tk()

# field variables
names = tk.StringVar()
lnames = tk.StringVar()
gender = tk.StringVar()
birthday = tk.StringVar()
email = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
civil_status = tk.StringVar()

def create_client():
    # collect data from data entries

    val_names=names.get()
    val_lnames=lnames.get()
    val_gender=gender.get()
    val_dob=birthday.get()
    val_email=email.get()
    val_phone=phone.get()
    val_address=address.get()
    val_civil_status=civil_status.get()

    # user information, placeholders for now
    now = datetime.now()
    val_userr = "meraz"
    val_useru = "meraz"
    val_dateu = str(now.strftime("%Y-%m-%d"))
    val_dater = str(now.strftime("%Y-%m-%d"))
    val_status = 1
    val_timer = str(now.strftime("%H:%M:%S"))
    val_timeu = str(now.strftime("%H:%M:%S"))

    # create dictionary with all items
    client = mj.build_client(val_names,
                           val_lnames,
                           val_gender,
                           val_dob,
                           val_email,
                           val_phone,
                           val_address,
                           val_civil_status,
                           val_userr,
                           val_useru,
                           val_dateu,
                           val_dater,
                           val_status,
                           val_timer,
                           val_timeu)

    # send a request to the database
    sr.send_request(endpoint, client, headers)

window.title('Modulo Cliente')
# theme
window.tk.call('source', './azure-theme/azure.tcl')
window.tk.call('set_theme', 'light')
# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=10, pady=5)
# title
title_label = ttk.Label(master=window, text="Ingrese Cliente",
                        font="Calibri 24 bold").grid(row=0, column=0, padx=10, pady=5)
# fields
names_label = ttk.Label(master=input_frame, text="Nombres").grid(row=1, column=0, padx=10, pady=5)
names_entry = ttk.Entry(master=input_frame, textvariable=names).grid(row=1, column=1, padx=10, pady=5)
lnames_label = ttk.Label(master=input_frame, text="Apellidos").grid(row=2, column=0, padx=10, pady=5)
lnames_entry = ttk.Entry(master=input_frame, textvariable=lnames).grid(row=2, column=1, padx=10, pady=5)
gender_label = ttk.Label(master=input_frame, text="Sexo").grid(row=3, column=0, padx=10, pady=5)
gender_entry = ttk.Combobox(master=input_frame, textvariable=gender)
gender_options = ("M","F")
gender_entry['values'] = gender_options
gender_entry.grid(row=3, column=1, padx=10, pady=5)
birthday_label = ttk.Label(master=input_frame, text="Fecha Nacimiento").grid(row=4, column=0, padx=10, pady=5)
birthday_entry = ttk.Entry(master=input_frame, textvariable=birthday).grid(row=4, column=1, padx=10, pady=5)
email_label = ttk.Label(master=input_frame, text="Email").grid(row=5, column=0, padx=10, pady=5)
email_entry = ttk.Entry(master=input_frame, textvariable=email).grid(row=5, column=1, padx=10, pady=5)
phone_label = ttk.Label(master=input_frame, text="Telefono").grid(row=6, column=0, padx=10, pady=5)
phone_entry = ttk.Entry(master=input_frame, textvariable=phone).grid(row=6, column=1, padx=10, pady=5)
address_label = ttk.Label(master=input_frame, text="Direccion").grid(row=7, column=0, padx=10, pady=5)
address_entry = ttk.Entry(master=input_frame, textvariable=address).grid(row=7, column=1, padx=10, pady=5)
civil_status_label = ttk.Label(master=input_frame, text="Estado Civil").grid(row=8, column=0, padx=10, pady=5)
civil_status_entry = ttk.Combobox(master=input_frame, textvariable=civil_status)
civil_status_options = ("Casado","Soltero","Divorciado")
civil_status_entry['values'] = civil_status_options
civil_status_entry.grid(row=8, column=1, padx=10, pady=5)
# submit button
submit_button = ttk.Button(master=window, text="Submit", command=create_client).grid(row=2, column=0, padx=10, pady=5)
window.mainloop()