from transformers import pipeline
import requests

# 1. 날씨 정보 받아오기
API_KEY = "0284e70071622bcb22e623b8584d52f1"
city = input("도시명을 입력하세요: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=kr"
response = requests.get(url)
data = response.json()

# 2. 프롬프트 만들기
temp = data['main']['temp']
desc = data['weather'][0]['description']
humidity = data['main']['humidity']

prompt = f"""
현재 날씨는 {desc}이고 온도는 {temp}도, 습도는 {humidity}%야.
이 날씨에 어울리는 옷차림을 간단하게 추천해줘.
"""

# 3. AI에게 프롬프트 전달
generator = pipeline('text-generation', model='gpt2')
result = generator(prompt, max_new_tokens=60, num_return_sequences=1)

print("\n🧠 AI 의상 추천:")
print(result[0]['generated_text'])
