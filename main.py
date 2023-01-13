import requests
def json(url:str)->dict:
    response=requests.get(url)
    return response.json()

data=json("https://jsonplaceholder.typicode.com/")
print(data)