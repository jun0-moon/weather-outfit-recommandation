// ✅ 1. 도시명 매핑 테이블 추가
const cityTranslation = {
  서울: "Seoul",
  부산: "Busan",
  대구: "Daegu",
  인천: "Incheon",
  광주: "Gwangju",
  대전: "Daejeon",
  울산: "Ulsan",
  제주: "Jeju",
  춘천: "Chuncheon",
  포항: "Pohang",
  청주: "Cheongju",
  창원: "Changwon",
  전주: "Jeonju",
  여수: "Yeosu",
  김해: "Gimhae",
};

// ✅  입력값 처리 함수
function getCityInputValue() {
  const rawInput = document.getElementById("cityInput").value.trim();
  return cityTranslation[rawInput] || rawInput; // 매핑 실패 시 원본 반환
}

async function getRecommendation() {
  const city = getCityInputValue();
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
    console.log("통신 실패", err.message);
    resultDiv.innerText = "❌ 추천 실패: 추천 결과를 받아올 수 없습니다.";
  }
}

// Enter 키로 추천받기 가능하게 하기
document
  .getElementById("cityInput")
  .addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault(); // 폼 제출 방지
      document.querySelector("button").click(); // 버튼 클릭 실행
    }
  });
