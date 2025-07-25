# 🤖 scenAIro 🤖

A Python-based tool that automatically generates test scenarios by function from natural language requirements.
It leverages the GPT-4o-mini model to analyze requirements and outputs scenarios including preconditions and expected results in JSON and Excel formats.

---

## 📌 Key Features
- Parses natural language requirements based on the - delimiter
- Generates test scenarios using OpenAI GPT-4o-mini
- Automatically generates scenario IDs (e.g., SC-001)
- Saves results in JSON and Excel (.xlsx) formats

---

## 🧑‍💻 How to Use

### 1. Set up the environment

```bash
git clone https://github.com/yjeongdev/scenAIro.git
cd scenAIro
python -m venv venv
venv\Scripts\activate  # (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
```

### 2. Create the .env file
```ini
OPENAI_API_KEY=sk-xxxxxxx
```

### 3. Prepare the requirements file
Create a `test_scenarios.txt` file with content like:
```txt
- Log in as a user on the main screen.
- Create a post.
```

### 4. Run the program
```bash
cd src
python main.py -i ../test_scenarios.txt -o ../test_scenarios.json
```

### 5. Output
The files `test_scenarios.json` and `test_scenarios.xlsx` will be generated in the root directory.

## 📁 Project Structure
```bash
seanAIro/
├── .env                 # OpenAI API key
├── requirements.txt     # Required libraries
├── .gitignore           # Git ignore settings
├── test_scenarios.txt   # Input file for requirements (example)
├── test_scenarios.json  # Output JSON file for test scenarios (example)
├── test_scenarios.xlsx  # Output Excel file for test scenarios (example)
└── src/
    ├── main.py
    ├── requirement_parser.py
    ├── scenario_generator.py
    ├── formatter.py
    └── json_to_excel.py
```

## 🧠 AI Models Used

- OpenAI GPT-4o-mini
- openai 공식 Python SDK (openai>=1.0.0)

## 📝 License
MIT License. For details, please refer to the [LICENSE](https://mit-license.org/) file.

## 🙋‍♂️ Authors
- Developer : [@yjeongdev](https://github.com/yjeongdev)
- AI Development Assistant : Developed with OpenAI's ChatGPT (GPT-4o-mini).