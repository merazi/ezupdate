import json


def build_client(
    names,
    lnames,
    gender,
    dob,
    email,
    phone,
    address,
    civil_status,
    userr,
    useru,
    dateu,
    dater,
    status,
    timer,
    timeu,
):
    # create dictionary with received data
    # also note we are using the actual db's column names
    client = dict()
    client["nombres"] = names
    client["apellidos"] = lnames
    client["sexo"] = gender
    client["fecha_nacimiento"] = dob
    client["correo"] = email
    client["telefono"] = phone
    client["residencia"] = address
    client["es_civil"] = civil_status
    client["userr"] = userr
    client["useru"] = useru
    client["dateu"] = dateu
    client["dater"] = dater
    client["status"] = status
    client["timer"] = timer
    client["timeu"] = timeu
    client["table_name"] = "CustomerAdd"

    print(json.dumps(client))

    # return dictionary
    return client


def build_account(account_number, userr, useru, dateu, dater, status, timer, timeu):
    # create dictionary with received data
    # also note we are using the actual db's column names
    account = dict()
    account["num_cuenta"] = account_number
    account["userr"] = userr
    account["useru"] = useru
    account["dateu"] = dateu
    account["dater"] = dater
    account["status"] = status
    account["timer"] = timer
    account["timeu"] = timeu
    account["table_name"] = "AccountAdd"

    print(json.dumps(account))

    return account


def build_account_type(
    desc, currency, userr, useru, dateu, dater, status, timer, timeu
):
    # create dictionary with received data
    # also note we are using the actual db's column names
    account_type = dict()
    account_type["descripcion"] = desc
    account_type["moneda"] = currency
    account_type["userr"] = userr
    account_type["useru"] = useru
    account_type["dateu"] = dateu
    account_type["dater"] = dater
    account_type["status"] = status
    account_type["timer"] = timer
    account_type["timeu"] = timeu
    account_type["table_name"] = "AccountTypeAdd"

    print(json.dumps(account_type))
    return account_type


def build_assign_client(
    id_client,
    id_account,
    id_account_type,
    userr,
    useru,
    dateu,
    dater,
    status,
    timer,
    timeu,
):
    rel_acct_client = dict()
    rel_acct_client["id_client"] = id_client
    rel_acct_client["id_account_type"] = id_account_type
    rel_acct_client["id_account"] = id_account
    rel_acct_client["userr"] = userr
    rel_acct_client["useru"] = useru
    rel_acct_client["dateu"] = dateu
    rel_acct_client["dater"] = dater
    rel_acct_client["status"] = status
    rel_acct_client["timer"] = timer
    rel_acct_client["timeu"] = timeu
    rel_acct_client["table_name"] = "AssignAccountToCustomer"
    return rel_acct_client
