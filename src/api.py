from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from src import (formatter, json_to_excel, requirement_parser,
                 scenario_generator)

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    text: str


@app.get("/")
def read_index():
    return FileResponse("src/frontend/index.html")


@app.post("/api/generate")
async def generate(body: RequestBody):
    try:
        requirements = requirement_parser.parse_requirements(body.text)
        scenarios = scenario_generator.generate_scenarios(requirements)
        formatted_scenarios = formatter.assign_ids_to_scenarios(scenarios)
        formatted = formatter.format_scenarios(formatted_scenarios)
        return formatted
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/generate_excel")
async def generate_excel(request: Request):
    data = await request.json()
    scenarios = data.get("scenarios", [])
    if not scenarios:
        return JSONResponse(content={"error": "No scenarios provided"}, status_code=400)

    # 엑셀 생성
    output_path = "test_scenarios.xlsx"
    json_to_excel.json_to_excel(scenarios, output_path)

    # 파일 반환
    return FileResponse(path=output_path, filename="test_scenarios.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


app.mount("/", StaticFiles(directory="src/frontend", html=True), name="frontend")