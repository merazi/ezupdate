import endpoint
import tkinter as tk
import build_json as mj
import send_request as sr
from tkinter import ttk
from datetime import datetime
import mysql.connector
import db_credentials
import os

# Create a connection
h = db_credentials.host
d = db_credentials.database
u = db_credentials.user
p = db_credentials.password
con = mysql.connector.connect(host=h, database=d, user=u, password=p)


def select_all_from_table(table, connection):
    query = f"SELECT * FROM {table}"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


endpoint = endpoint.get_url()
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # if you need to send a token
}

# window
window = tk.Tk()

# field variables
cliente = tk.StringVar()
tipo_cuenta = tk.StringVar()
cuenta = tk.StringVar()


def get_id_from_combobox(combo_StringVar):
    """This function helps me extract the id number from the Comboboxes"""
    id = [int(word) for word in combo_StringVar.get().split() if word.isdigit()][0]
    return id


def assign_acct_to_client():

    # collect data from data entries
    val_cliente = get_id_from_combobox(cliente)
    val_tipo_cuenta = get_id_from_combobox(tipo_cuenta)
    val_cuenta = get_id_from_combobox(cuenta)

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
    client = mj.build_assign_client(
        val_cliente,
        val_tipo_cuenta,
        val_cuenta,
        val_userr,
        val_useru,
        val_dateu,
        val_dater,
        val_status,
        val_timer,
        val_timeu,
    )

    # send a request to the database
    sr.send_request(endpoint, client, headers)


window.title("Modulo Cliente")

# theme
theme_path = os.path.join(os.path.dirname(__file__), "azure_theme", "azure.tcl")
window.tk.call("source", theme_path)
window.tk.call("set_theme", "light")

# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=10, pady=5)

# title
title_label = ttk.Label(
    master=window,
    text="Relacionar Cuenta con Cliente (Y Tipo cuenta)",
    font="Calibri 24 bold",
).grid(row=0, column=0, padx=10, pady=5)

# fields

## for clients
client_list = select_all_from_table("clientes", con)
client_entry_label = ttk.Label(master=input_frame, text="Seleccione un cliente:")
client_entry_label.grid(row=1, column=0, padx=10, pady=5)
client_entry = ttk.Combobox(master=input_frame, textvariable=cliente)
client_entry["values"] = client_list
client_entry.grid(row=2, column=0, padx=10, pady=5)

## for account types
account_type_list = select_all_from_table("tipo_cuenta", con)
account_type_entry_label = ttk.Label(master=input_frame, text="Tipo de Cuenta:")
account_type_entry_label.grid(row=1, column=1, padx=10, pady=5)
account_type_entry = ttk.Combobox(master=input_frame, textvariable=tipo_cuenta)
account_type_entry["values"] = account_type_list
account_type_entry.grid(row=2, column=1, padx=10, pady=5)

## for accounts
account_list = select_all_from_table("cuentas", con)
account_entry_label = ttk.Label(master=input_frame, text="Tipo de Cuenta:")
account_entry_label.grid(row=1, column=2, padx=10, pady=5)
account_entry = ttk.Combobox(master=input_frame, textvariable=cuenta)
account_entry["values"] = account_list
account_entry.grid(row=2, column=2, padx=10, pady=5)

# submit button
submit_button = ttk.Button(
    master=window, text="Submit", command=assign_acct_to_client
).grid(row=2, column=0, padx=10, pady=5)
window.mainloop()
