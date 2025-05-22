async function getRecommendation() {
  const city = document.getElementById("cityInput").value;
  const resultDiv = document.getElementById("result");

  resultDiv.innerText = "AI가 추천 중입니다...🧠";

  try {
    const res = await fetch(
      `http://localhost:5000/recommend_gemini?city=${city}`
    );
    const data = await res.json();
    resultDiv.innerText = "👕 " + res.recommendation;
  } catch (err) {
    resultDiv.innerText = "❌ 추천 실패: " + err.message;
  }
}
