import json
from flask import Flask, request, Response, jsonify
import requests
from transformers import pipeline

app = Flask(__name__)

# OpenWeatherMap API Key
API_KEY = "0284e70071622bcb22e623b8584d52f1"

# AI 모델 로드
generator = pipeline("text-generation", model="skt/kogpt2-base-v2")

@app.route('/recommend')
def recommend():
    city = request.args.get('city')

    # 날씨 데이터 가져오기
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=kr"
    weather_res = requests.get(weather_url)
    
    if weather_res.status_code != 200:
        return jsonify({"error": "날씨 정보를 불러올 수 없습니다."}), 400

    data = weather_res.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    humidity = data['main']['humidity']

    # 프롬프트 생성
    prompt = f"""
    현재 기온은 {temp}도이고, 날씨는 {desc}, 습도는 {humidity}%입니다.
    이런 날씨에 어울리는 남녀 모두 입을 수 있는 **캐주얼 데일리룩**을 하나만 추천해줘.
    예: 얇은 셔츠 + 청바지, 가벼운 후드티 + 반바지 처럼 간단하게 말해줘.
    """

    # AI 텍스트 생성
    result = generator(prompt, max_length=100, num_return_sequences=1)
    generated = result[0]['generated_text'].replace(prompt.strip(), '').strip()

    result_json = json.dumps({"recommendation": generated}, ensure_ascii=False)
    return Response(result_json, content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True)
