import endpoint
import tkinter as tk
import build_json as mj
import send_request as sr
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar
import mysql.connector
import db_credentials
import os

endpoint = endpoint.get_url()
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # if you need to send a token
}

# Create a connection
h = db_credentials.host
d = db_credentials.database
u = db_credentials.user
p = db_credentials.password
con = mysql.connector.connect(host=h, database=d, user=u, password=p)

# window
window = tk.Tk()

# field variables
rel = tk.StringVar()
date = tk.StringVar()
description = tk.StringVar()
charge = tk.StringVar()
credit = tk.StringVar()
balance = tk.StringVar()


def select_all_from_table(table, connection):
    query = f"SELECT * FROM {table} INNER JOIN "
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def get_id_from_combobox(combo_StringVar):
    """This function helps me extract the id number from the Comboboxes"""
    id = [int(word) for word in combo_StringVar.get().split() if word.isdigit()][0]
    return id


def create_account_type(endpoint, headers):
    # collect data from data entries
    # TODO: Change this...
    val_rel_id = get_id_from_combobox(rel)
    val_date = movement_date_entry.get_date()
    # val_description =
    # val_charge =
    # val_credit =
    # val_balance =

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
        # val_rel_id,
        # val_date,
        # val_description,
        # val_charge,
        # val_credit,
        # val_balance,
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
theme_path = os.path.join(os.path.dirname(__file__), "azure_theme", "azure.tcl")
window.tk.call("source", theme_path)
window.tk.call("set_theme", "light")


# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=10, pady=5)

# title
title_label = ttk.Label(master=window, text="Crear movimiento", font="Calibri 24 bold")
title_label.grid(row=0, column=0, padx=10, pady=5)

# fields

## Relational ID
rel_list = select_all_from_table(con) # pass with customer names and all
rel_entry_label = ttk.Label(master=input_frame, text="Seleccione origen:")
rel_entry = ttk.Combobox(master=input_frame, textvariable=rel)
rel_entry["values"] = rel_list
rel_entry_label.grid(row=0, column=0, padx=10, pady=5)
rel_entry.grid(row=0, column=1, padx=10, pady=5)

## Date entry
movement_date_label = ttk.Label(master=input_frame, text="Seleccione la fecha del movimiento")
movement_date_label.grid(row=1, column=1, padx=10, pady=5)
movement_date_entry = Calendar(
    master=input_frame,
    selectmode="day",
    year=int(datetime.now().strftime("%Y")),
    month=int(datetime.now().strftime("%m")),
    day=int(datetime.now().strftime("%d")),
)
movement_date_entry.grid(row=2, column=1, padx=10, pady=5)

# submit button
submit_button = ttk.Button(
    master=window, text="Submit", command=lambda: create_account_type(endpoint, headers)
)
submit_button.grid(row=3, column=0, padx=10, pady=5)
window.mainloop()
