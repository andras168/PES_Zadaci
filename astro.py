import requests

URL = "http://api.open-notify.org/astros.json"

conn = requests.get(URL)

data = conn.json()
i = 0

while i < len(data["people"]):
    ime = data["people"][i]["name"]
    print("Ime:", ime)
    i += 1
    
#-- len() function in python - return the number of items in a list
#-- mylist = ["apple", "banana", "cherry"]
#-- x = len(mylist)
#-- result: 3
