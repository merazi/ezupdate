import json

def build_client(names,lnames,
               gender,dob,email,
               phone,address,
               civil_status,userr,
               useru,dateu,dater,
               status,timer,timeu):
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
  
    print(json.dumps(client))

    # return dictionary
    return client

def build_account(account_number,userr,
               useru,dateu,dater,
               status,timer,timeu):
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
  
    print(json.dumps(account))

    return account