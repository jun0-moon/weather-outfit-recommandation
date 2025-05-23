import { useState } from "react";
import ReactMarkdown from "react-markdown";

function Recommendation({ markdownText }) {
  return <ReactMarkdown>{markdownText}</ReactMarkdown>;
}

// 예시: fetch로 받아온 결과를 Recommendation에 전달
function App() {
  const [recommendation, setRecommendation] = useState("");

  async function getRecommendation() {
    setResult("AI가 추천 중입니다...🧠");
    try {
      const res = await fetch(
        `http://localhost:5000/recommend_gemini?city=${city}`
      );
      const data = await res.json();
      setRecommendation("👕 " + data.recommendation);
    } catch (err) {
      setRecommendation("❌ 추천 실패: " + err.message);
    }
  }

  return (
    <div>
      <input
        type="text"
        id="cityInput"
        placeholder="도시명을 입력하세요 (예: 서울)"
      />
      <button onClick={getRecommendation}>추천받기</button>
      <Recommendation markdownText={recommendation} />
    </div>
  );
}

export default App;
