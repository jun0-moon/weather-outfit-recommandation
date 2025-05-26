import os

GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")
OPEN_WEATHER_MAP_API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")

missing = []
if GEMINI_API_KEY is None:
    missing.append("GOOGLE_API_KEY")
if OPEN_WEATHER_MAP_API_KEY is None:
    missing.append("OPEN_WEATHER_MAP_API_KEY")

if missing:
    raise RuntimeError(f"환경 변수 {', '.join(missing)} 가(이) 없습니다.")
