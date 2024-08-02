import clients_input
import account_input

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # if you need to send a token
}

# I have to work on being able to use this
clients_input.create_gui("https://eot5nxsbpnt20i2.m.pipedream.net", headers)
account_input.create_gui("https://eojcf9ylwovln2u.m.pipedream.net",headers)