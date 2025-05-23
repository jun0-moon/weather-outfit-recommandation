async function getRecommendation() {
  const city = document.getElementById("cityInput").value;
  const resultDiv = document.getElementById("result");

  resultDiv.innerText = "AI가 추천 중입니다...🧠";

  try {
    const res = await fetch(
      `http://localhost:5000/recommend_gemini?city=${city}`
    );
    console.log("통신 결과", res);
    const data = await res.json();
    resultDiv.innerHTML = "👕 " + marked.parse(data.recommendation);
  } catch (err) {
    resultDiv.innerText = "❌ 추천 실패: " + err.message;
  }
}

// Enter 키로 추천받기 가능하게 하기
document.getElementById("cityInput").addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    event.preventDefault(); // 폼 제출 방지
    document.querySelector("button").click(); // 버튼 클릭 실행
  }
});