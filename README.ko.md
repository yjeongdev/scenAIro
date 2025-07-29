# 🤖 scenAIro 🤖

자연어로 작성된 요구사항을 기반으로 기능별 **테스트 시나리오**를 자동 생성하는 Python 기반 도구입니다.  
GPT-4o-mini 모델을 활용하여 요구사항을 분석하고, 각 기능에 대해 사전조건과 예상결과를 포함한 시나리오를 JSON 및 Excel 파일로 출력합니다.

---

## 📌 주요 기능
- 자연어 요구사항 파싱 (`-` 기호 기준)
- OpenAI GPT-4o-mini로 테스트 시나리오 생성
- 시나리오 ID 자동 생성 (`SC-001` 등)
- 결과를 Excel(.xlsx)로 저장

---

## 📁 주요 디렉토리 구조
```bash
scenAIro/
├── deploy.bat                # 배포 스크립트 (Windows)
├── src/
│ ├── frontend/
│ │ └── assets/               # Vite 기반 프론트엔드 자산
│ ├── api.py                  # API 정의
│ ├── formatter.py            # 출력 포매터
│ ├── json_to_excel.py        # JSON to Excel 변환기
│ ├── main.py                 # 애플리케이션 실행 진입점
│ ├── requirement_parser.py   # 요구사항 파서
│ └── scenario_generator.py   # 테스트 시나리오 생성기
├── .env.example              # 환경 변수 예시
├── .gitignore                # gitignore 설정
└── requirement.txt           # Python 의존성 목록
```

## 🧑‍💻 사용 방법

### 1. 환경 준비

```bash
git clone https://github.com/yjeongdev/scenAIro.git
cd scenAIro
python -m venv venv
venv\Scripts\activate  # (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
```

### 2. .env 파일 생성
```ini
OPENAI_API_KEY=sk-xxxxxxx
```

### 3. 실행
```bash
uvicorn src.api:app --reload --port 8000
```

### 4. 요구사항 입력
`http://localhost:8000/`에 접속하여 자연어 요구사항을 입력합니다.<br>
요구사항이 여러 개인 경우 하이픈(`-`)으로 구분하여 작성합니다.
```txt
- 메인화면에서 사용자로 로그인한다.
- 게시물을 생성한다. 
```

### 5. 시나리오 생성
`시나리오 생성` 버튼을 클릭하면 자연어로 입력한 요구사항의 테스트 시나리오가 화면 하단에 표시됩니다.<br>
생성된 시나리오에서 수정할 내용이 있는 경우 직접 입력할 수 있습니다.<br>
단, ID는 수정할 수 없습니다. (시퀀스 자동생성)

### 6. 엑셀 다운로드
`엑셀 다운로드` 버튼을 클릭하면 `test_scenarios.xlsx` 파일이 로컬 경로에 다운로드 됩니다.

## 🧠 사용 모델

- OpenAI GPT-4o-mini
- openai 공식 Python SDK (openai>=1.0.0)

## 📝 라이선스
MIT License. 자세한 내용은 [LICENSE](https://mit-license.org/) 파일을 참조하세요.

## 🙋‍♂️ 제작자
- 개발자 : [@yjeongdev](https://github.com/yjeongdev)
- AI 개발 도우미 : OpenAI의 ChatGPT (GPT-4o)와 함께 개발하였습니다.