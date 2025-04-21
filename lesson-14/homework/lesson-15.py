import json

with open('students.json', 'r') as file:
    data = json.load(file)


for student in data:
    print("Student details:")
    print(f"Name: {student['name']}")
    print(f"Age {student['age']}")
    print(f"Grade {student['grade']}")
    print("_"*20)

################################################################################################################################################################################################################


import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid=be67b5a1782335d4388e8a9309bd389f&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description']

    print(f"Today in Tashkent weather is {temp} humidity is {humidity} and {desc}")
else:
    print('Invalid url!')

################################################################################################################################################################################################################









