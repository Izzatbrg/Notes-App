"""
this script is just for testing. Insted of that Plz use Postman

"""
import requests

URL = "http://127.0.0.1:5000/"
data ={
    "title": "HelloWorld",
    "text": "Bye Bye World"
    }
responce = requests.post(URL+"notes", data=data)
print(responce.json())