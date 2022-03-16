import requests
import json

def show_data():
    URL = "http://127.0.0.1:8000/api/itemdetail/"

    r = requests.get(url=URL)
    data =  r.json()
    print(data)


def insert_data(name= 'pizza360',description= 'french dish',price= 1000.0):

    URL = "http://127.0.0.1:8000/api/itemcreate/"

    data = {
        'name' : name,
        'description' : description,
        'price' : print
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)

#-----------------------------------------------------------------------------------


def get_data(id = None):
    URL = "http://127.0.0.1:8000/itemapi"
    # URL = "http://127.0.0.1:8000/itemapiclass"
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()
# get_data(37)

def post_data():
    URL = "http://127.0.0.1:8000/itemapi"
    # URL = "http://127.0.0.1:8000/itemapiclass"
    data = {
        'name' : 'asdwa',
        'description' : 'khakejana',
        'price' : 200.0
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()


def update_data():
    URL = "http://127.0.0.1:8000/itemapi"
    # URL = "http://127.0.0.1:8000/itemapiclass"
    data = {
        'id' : 69,
        'name' : 'aaaaaaaaa',
        'description' : 'kahkejana',
        'price' : 70.5
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

update_data()


def delete_data():
    URL = "http://127.0.0.1:8000/itemapi"
    # URL = "http://127.0.0.1:8000/itemapiclass"
    data = {
        'id' : 69,
        
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

delete_data()