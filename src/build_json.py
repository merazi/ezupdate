def parse_data(names,lnames,gender,dob,email,phone,address,civil_status,userr,useru,dateu,dater,status,timer,timeu):
    # create dictionary with received data
    # also note we have to use the db's column names here
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
  
    # return dictionary
    return client
