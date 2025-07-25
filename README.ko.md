# 🤖 scenAIro 🤖

자연어로 작성된 요구사항을 기반으로 기능별 **테스트 시나리오**를 자동 생성하는 Python 기반 도구입니다.  
GPT-4o-mini 모델을 활용하여 요구사항을 분석하고, 각 기능에 대해 사전조건과 예상결과를 포함한 시나리오를 JSON 및 Excel 파일로 출력합니다.

---

## 📌 주요 기능
- 자연어 요구사항 파싱 (`-` 기호 기준)
- OpenAI GPT-4o-mini로 테스트 시나리오 생성
- 시나리오 ID 자동 생성 (`SC-001` 등)
- 결과를 JSON 및 Excel(.xlsx)로 저장

---

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

### 3. 요구사항 파일 작성
`test_scenarios.txt` 파일에 아래와 같이 입력합니다.
```txt
- 메인화면에서 사용자로 로그인한다.
- 게시물을 생성한다. 
```

### 4. 실행
```bash
cd src
python main.py -i ../test_scenarios.txt -o ../test_scenarios.json
```

### 5. 결과
실행 결과 `test_scenarios.json`, `test_scenarios.xlsx` 파일이 루트 경로에 생성됩니다.

## 📁 프로젝트 구조
```bash
seanAIro/
├── .env                 # OpenAI API 키
├── requirements.txt     # 필요한 라이브러리
├── .gitignore           # Git 무시 파일 설정
├── test_scenarios.txt   # 요구사항 입력 파일 (예시)
├── test_scenarios.json  # 요구사항 JSON 출력 파일 (예시)
├── test_scenarios.xlsx  # 요구사항 Excel 출력 파일 (예시)
└── src/
    ├── main.py
    ├── requirement_parser.py
    ├── scenario_generator.py
    ├── formatter.py
    └── json_to_excel.py
```

## 🧠 사용 모델

- OpenAI GPT-4o-mini
- openai 공식 Python SDK (openai>=1.0.0)

## 📝 라이선스
MIT License. 자세한 내용은 [LICENSE](https://mit-license.org/) 파일을 참조하세요.

## 🙋‍♂️ 제작자
- 개발자 : [@yjeongdev](https://github.com/yjeongdev)
- AI 개발 도우미 : OpenAI의 ChatGPT (GPT-4o-mini)와 함께 개발하였습니다.