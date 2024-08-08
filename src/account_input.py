import endpoint
import random, string
import tkinter as tk
import build_json as mj
import send_request as sr
from tkinter import ttk
from datetime import datetime
import os

endpoint = endpoint.get_url()
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # if you need to send a token
}

# window
window = tk.Tk()

# field variables
account = tk.StringVar()


def create_account(endpoint, headers):
    # collect data from data entries
    val_account = account.get()

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
    account_data = mj.build_account(
        val_account,
        val_userr,
        val_useru,
        val_dateu,
        val_dater,
        val_status,
        val_timer,
        val_timeu,
    )

    # send a request to the database
    sr.send_request(endpoint, account_data, headers)


def randomize_account(acct_entry):
    random_text = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    acct_entry.delete(0, tk.END)  # Clear the current content
    acct_entry.insert(0, random_text)  # Insert the new random content


window.title("Modulo Cuenta")

# theme
theme_path = os.path.join(os.path.dirname(__file__), "azure_theme", "azure.tcl")
window.tk.call("source", theme_path)
window.tk.call("set_theme", "light")


# input area fields
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=10, pady=5)

# title
title_label = ttk.Label(master=window, text="Nueva Cuenta", font="Calibri 24 bold")
title_label.grid(row=0, column=0, padx=10, pady=5)

# fields
account_label = ttk.Label(master=input_frame, text="Numero Cuenta")
account_label.grid(row=1, column=0, padx=10, pady=5)
account_entry = ttk.Entry(master=input_frame, textvariable=account)
account_entry.grid(row=1, column=1, padx=10, pady=5)

randomize_button = ttk.Button(
    master=window, text="Random", command=lambda: randomize_account(account_entry)
)
randomize_button.grid(row=2, column=0, padx=10, pady=5)

# submit button
submit_button = ttk.Button(
    master=window, text="Submit", command=lambda: create_account(endpoint, headers)
)
submit_button.grid(row=3, column=0, padx=10, pady=5)
window.mainloop()
