import requests

#-- Novi Sad koordinate
#-- longitude = 19.833549
#-- latitude = 45.267136
#-- API Key = 2c82f49daae6f246b961900f75ef7cb4

URL = "https://api.openweathermap.org/data/2.5/weather?lat=45.267136&lon=19.833549&appid=2c82f49daae6f246b961900f75ef7cb4"
conn = requests.get(URL)

data = conn.json()

#print(data)

#-- funkcija koja pretvara temperaturu iz kelvina u celziuse
def k_to_c(k_value):
    c_value = k_value - 273.15
    return c_value

temp = data["main"]["temp"]
fl = data["main"]["feels_like"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]

temp_c = k_to_c(temp)
fl_c = k_to_c(fl)
min_c = k_to_c(temp_min)
max_c = k_to_c(temp_max)

print("Trenutna temperatura: %.2f°C, Feels like: %.2f°C, Minimalno: %.2f°C, Maksimalno: %.2f°C" % (temp_c, fl_c, min_c, max_c))