@echo off

echo 🔧 Step 1: React 앱 빌드
cd ..\scenAIro-ui
call npm run build
if errorlevel 1 (
    echo ❌ React 빌드 실패
    exit /b 1
)

echo 📂 Step 2: dist → FastAPI static 폴더 복사
xcopy /E /I /Y dist\* ..\scenAIro\src\frontend\

cd ..\scenAIro

echo 🚀 Step 3: FastAPI 서버 실행
call venv_scenairo\Scripts\activate
uvicorn src.api:app --reload --port 8000
