import requests

def send_request(url, data, headers):
    # Send post request
    response = requests.post(url, json=data, headers=headers)

    # Server response
    print('Status Code:', response.status_code)
    #print('Response Text:', response.text)
