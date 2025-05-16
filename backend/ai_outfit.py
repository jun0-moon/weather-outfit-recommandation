from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import requests

app = Flask(__name__)

def recommend():
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
    gender = "남자"

    if temp < 10:
        tmp="두꺼운 코트, 패딩 추천해줘"
    elif temp < 20:
        tmp="맨투맨, 후드 추천해줘"
    else:
        tmp="반팔, 얇은 셔츠 추천해줘"

    instruction = f"현재 기온은 {temp}도이고, 날씨는 {desc}, 습도는 {humidity}%입니다. 이런 날씨에 어울리는 {gender} {tmp}"
    prompt = f"### 사용자: {instruction}\n### {gender} 의상 추천:"

    # 3. AI에게 프롬프트 전달

    model_name = "hyunjae/skt-kogpt2-kullm-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, do_sample=True, top_k=20)

    result = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"recommendation": result})

if __name__ == '__main__':
    app.run(debug=True)
