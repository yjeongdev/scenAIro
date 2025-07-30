# scenAIro

A Python-based tool that automatically generates **test scenarios** by function from natural language requirements.
It leverages the GPT-4o-mini model to analyze requirements and outputs scenarios including preconditions and expected results in JSON and Excel formats.

- Parses natural language requirements based on the - delimiter
- Generates test scenarios using OpenAI GPT-4o-mini
- Automatically generates scenario IDs (e.g., SC-001)
- Saves results in Excel (.xlsx) formats
---

## Project Structure

```bash
scenAIro/
├── deploy.bat
├── src/
│   ├── frontend/
│   │   └── assets
│   ├── api.py
│   ├── formatter.py
│   ├── json_to_excel.py
│   ├── main.py
│   ├── requirement_parser.py
│   └── scenario_generator.py
├── .env.example
├── .gitignore
└── requirement.txt
```

## Requirements

* Python 3 (3.11+)
* Node.js 18
* OpenAI API Key

## Installation

### Clone Git

```bash
git clone https://github.com/yjeongdev/scenAIro.git
cd scenAIro
```

### Backend

```bash
python -m venv venv
venv\Scripts\activate  # (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
```

Create the `.env` file
```ini
OPENAI_API_KEY=sk-xxxxxxx
```

### Frontend

```bash
cd scenAIro-ui
npm install
npm run dev
npm run build
xcopy /E /I /Y dist ..\src\frontend\
```

### Execution

```bash
uvicorn src.api:app --reload --port 8000
```

## Testing

### Input Requirements

Go to `http://localhost:8000/` and enter your natural language requirements.<br>
If you have multiple requirements, separate them with a hyphen (`-`).
```txt
- Log in as a user on the main screen.
- Create a post.
```

### Generate Scenarios

When you click the `Generate Scenario` button, the test scenario for the requirements entered in natural language will be displayed at the bottom of the screen.<br>
If there is anything you want to edit in the generated scenario, you can enter it directly.<br>
However, the ID cannot be edited. (Sequence auto-generation)

### Download Excel File

When you click the `Excel Download` button, the “test_scenarios.xlsx” file will be downloaded to your local path.

## AI Models Used

- OpenAI GPT-4o-mini
- openai Official Python SDK (openai>=1.0.0)

## License

MIT License. For details, please refer to the [LICENSE](https://mit-license.org/) file.

## Authors

- Developer : [@yjeongdev](https://github.com/yjeongdev)
- AI Development Assistant : Developed with OpenAI's ChatGPT (GPT-4o).