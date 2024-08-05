import requests
import json
import socket

# Get the local IP address of the server
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# URL construction using local IP address
local_ip = get_local_ip()
base_url = f"http://{local_ip}:8001"  # Change port if needed

def show_data():
    URL = f"{base_url}/api/itemdetail/"
    r = requests.get(url=URL)
    data = r.json()
    print(data)

def insert_data(name='pizza360', description='french dish', price=1000.0):
    URL = f"{base_url}/api/itemcreate/"
    data = {
        'name': name,
        'description': description,
        'price': price
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    print(r.json())

def get_data(id=None):
    URL = f"{base_url}/itemapi"
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print(data)

def post_data():
    URL = f"{base_url}/itemapi"
    data = {
        'name': 'asdwa',
        'description': 'khakejana',
        'price': 200.0
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print(data)

def update_data():
    URL = f"{base_url}/itemapi"
    data = {
        'id': 69,
        'name': 'aaaaaaaaa',
        'description': 'kahkejana',
        'price': 70.5
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print(data)

def delete_data():
    URL = f"{base_url}/itemapi"
    data = {
        'id': 69,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print(data)

# Example usage
show_data()
insert_data()
get_data()
post_data()
update_data()
delete_data()