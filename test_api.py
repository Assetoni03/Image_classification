import requests

# Замените URL на адрес вашего FastAPI приложения
url = "http://localhost:8000/upload/"

# Замените путь к файлу на путь к вашему файлу "dog.png"
files = {'item': ('dog.png', open('dog.png', 'rb'))}  # Обратите внимание на 'item' вместо 'image'

response = requests.post(url, files=files)

if response.status_code == 200:
    data = response.json()
    print("Label:", data["label"])
    print("Confidence:", data["confidence"])
else:
    print("Error:", response.status_code, response.text)
