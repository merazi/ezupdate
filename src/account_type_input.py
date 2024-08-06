import endpoint
import tkinter as tk
import build_json as mj
import send_request as sr
from tkinter import ttk
from datetime import datetime

endpoint = endpoint.get_url()
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # if you need to send a token
}

# window
window = tk.Tk()

# field variables
account_type_desc = tk.StringVar()
account_type_curr = tk.StringVar()


def create_account_type(endpoint, headers):
    # collect data from data entries
    val_account_type_desc = account_type_desc_entry.get()
    val_account_type_curr = account_type_curr_entry.get()

    # user information, placeholders for now
    now = datetime.now()
    val_userr = "meraz"
    val_useru = "meraz"
    val_dateu = now.strftime("%Y-%m-%d")
    val_dater = now.strftime("%Y-%m-%d")
    val_status = 1
    val_timer = now.strftime("%H:%M:%S")
    val_timeu = now.strftime("%H:%M:%S")

    # create dictionary with all items
    account_type_data = mj.build_account_type(
        val_account_type_desc,
        val_account_type_curr,
        val_userr,
        val_useru,
        val_dateu,
        val_dater,
        val_status,
        val_timer,
        val_timeu,
    )

    # send a request to the database
    sr.send_request(endpoint, account_type_data, headers)


window.title("Crear Tipo de Cuenta Nuevo")

# theme
window.tk.call("source", "./azure-theme/azure.tcl")
window.tk.call("set_theme", "light")

# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=10, pady=5)

# title
title_label = ttk.Label(
    master=window, text="Nuevo Tipo de Cuenta", font="Calibri 24 bold"
)
title_label.grid(row=0, column=0, padx=10, pady=5)

# fields
account_type_desc_label = ttk.Label(master=input_frame, text="Descripcion")
account_type_desc_label.grid(row=1, column=0, padx=10, pady=5)
account_type_desc_entry = ttk.Entry(master=input_frame, textvariable=account_type_desc)
account_type_desc_entry.grid(row=1, column=1, padx=10, pady=5)

account_type_curr_label = ttk.Label(master=input_frame, text="Moneda")
account_type_curr_label.grid(row=2, column=0, padx=10, pady=5)
account_type_curr_entry = ttk.Entry(master=input_frame, textvariable=account_type_curr)
account_type_curr_entry.grid(row=2, column=1, padx=10, pady=5)

# submit button
submit_button = ttk.Button(
    master=window, text="Submit", command=lambda: create_account_type(endpoint, headers)
)
submit_button.grid(row=3, column=0, padx=10, pady=5)
window.mainloop()
