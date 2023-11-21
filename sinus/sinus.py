import requests
import math
from time import sleep

# Na ThingSpeak platform prikazati sinusoidu sa intervalom od 256 tačaka i opsegom vrednosti [-10, 10]
num_points = 256

for i in range(num_points):
    print(i)

    angle = 2 * math.pi * i / num_points
    y_value = 10 * math.sin(angle)
    #https://stackoverflow.com/questions/22566692/how-to-plot-graph-sine-wave

    field_data = {'field1': str(y_value)}

    ts_url = f'https://api.thingspeak.com/update?api_key=7M0VU7KG2MDQ9QQ0&field1={y_value}'
    
    try:
        response = requests.get(ts_url)
        print(f"Data sent to ThingSpeak: {y_value}")
    except requests.RequestException as e:
        print(f"Error sending data to ThingSpeak: {e}")

    sleep(15)  # Salji podatak svakih 15 sekundi (ThingSpeak free account ogranicenje), ili postavi na 1 sekundu da bi ubrzao proces generisanja,
               # ali onda salje samo svaki 15. podatak
    
print("Generation of the sine wave is complete.")
