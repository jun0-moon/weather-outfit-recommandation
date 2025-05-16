import requests

API_KEY = "0284e70071622bcb22e623b8584d52f1"
CITY = "Daegu" # TODO 나중에 입력 받을 수 있게 변경해야 함.

# API 요청 URL 구성
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=kr"

response = requests.get(url)
data = response.json()

# 결과 출력
print("도시:", data['name'])
print("날씨 상태:", data['weather'][0]['description'])
print("현재 온도:", data['main']['temp'], "°C")
print("체감 온도:", data['main']['feels_like'], "°C")
print("습도:", data['main']['humidity'], "%")