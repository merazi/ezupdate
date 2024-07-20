import requests

# The URL to which the POST request will be sent
url = 'https://testmeraz07192024.requestcatcher.com/'

# The data to be sent in the POST request
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'message': 'Hello, this is a test message.'
}

# Headers for the request, if needed
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # if you need to send a token
}

# Sending the POST request
response = requests.post(url, json=data, headers=headers)

# Printing the response from the server
print('Status Code:', response.status_code)
print('Response Text:', response.text)
