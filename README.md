# 날씨 기반 의상 추천 시스템

## 개요

사용자의 지역 날씨 데이터를 기반으로 적절한 옷차림을 추천해주는 인공지능 웹 애플리케이션입니다.

## 기능

- 위치 기반 날씨 API 연동
- 머신러닝 기반 의상 추천
- 웹 인터페이스 제공

## 🚀 서버(Backend) 실행 방법

1. **backend 폴더로 이동**

   ```
   cd backend
   ```

2. **필요한 패키지 설치**

   ```
   pip install -r requirements.txt
   ```

   - `requirements.txt`에 명시된 모든 파이썬 패키지가 설치됩니다.

3. **서버 실행**
   ```
   python app.py
   ```
   - 서버가 실행되면 기본적으로 `http://localhost:5000`에서 접속할 수 있습니다.

---

### ⚡️ 참고/문제 해결

- **Python이 설치되어 있어야 합니다.**
  ```
  python --version
  pip --version
  ```
- **포트 충돌 시**
  - 기본 포트(5000)가 이미 사용 중이면 `app.py` 내에서 포트를 변경하거나 아래처럼 실행:
    ```
    python app.py --port 5001
    ```
- **에러 발생 시**
  - 터미널의 에러 메시지를 확인하세요.
  - 패키지 설치 오류가 있으면 `pip`를 최신 버전으로 업그레이드 해보세요:
    ```
    pip install --upgrade pip
    ```

---

**Tip:**

- 환경변수(API Key 등)가 필요한 경우 `.env` 파일이나 환경변수 설정을 확인하세요.
- 서버 실행 후 정상적으로 동작하는지 [http://localhost:5000](http://localhost:5000)에서 확인할 수 있습니다.

## 🖥️ 프론트엔드(Frontend) 실행 방법

1. **frontend 폴더로 이동**

   ```
   cd frontend
   ```

2. **필요한 패키지 설치**

   ```
   npm install
   ```

   - 의존성 패키지들을 자동으로 설치합니다.

3. **개발 서버 실행**
   ```
   npm start
   ```
   - 브라우저에서 자동으로 `http://localhost:3000`이 열립니다.

---

### ⚡️ 참고/문제 해결

- **Node.js가 설치되어 있어야 합니다.**
  ```
  node -v
  npm -v
  ```
- **포트 충돌 시**
  ```
  PORT=4000 npm start
  ```
- **에러가 발생하면 터미널의 에러 메시지를 확인하세요.**

---

**Tip:**

- frontend 폴더에 `package.json`이 반드시 있어야 합니다.
