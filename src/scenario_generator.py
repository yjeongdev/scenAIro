import json
import os
from typing import Dict, List

import openai
from dotenv import load_dotenv
from tqdm import tqdm

# 환경 변수 로드 (.env 파일에서 OPENAI_API_KEY 가져오기)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_scenario(requirement: str) -> Dict:
    """
    단일 요구사항에 대해 GPT를 호출하여 테스트 시나리오 JSON 생성
    (보안 강화: json.loads 사용)

    Args:
        requirement (str): 사용자 요구사항

    Returns:
        Dict: 테스트 시나리오 JSON 구조
    """
    system_prompt = (
        "당신은 QA 엔지니어입니다. 사용자의 요구사항을 보고 테스트 시나리오를 JSON으로 작성하세요.\n"
        "출력은 반드시 JSON 문자열로 반환되어야 하며, 코드 블록(```json`) 등은 포함하지 마세요.\n"
        "형식:\n"
        "{\n"
        "  \"content\": \"<요구사항 그대로>\",\n"
        "  \"precondition\": \"<사전조건 내용>\",\n"
        "  \"expected_result\": \"<예상 결과>\",\n"
        "  \"actual_result\": \"\",\n"
        "  \"note\": \"\"\n"
        "}"
    )

    user_prompt = f'요구사항: "{requirement}"'

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        content = response.choices[0].message.content.strip()

        # 안전한 JSON 파싱
        scenario = json.loads(content)

        # 기본 필드 보완 (실수로 누락된 필드 보정)
        scenario.setdefault("actual_result", "")
        scenario.setdefault("note", "")

        return scenario

    except json.JSONDecodeError as je:
        print(f"[PARSE ERROR] JSON 파싱 실패: {je}")
        return {
            "content": requirement,
            "precondition": "GPT 응답 JSON 파싱 실패",
            "expected_result": "응답 오류",
            "actual_result": "",
            "note": f"json error: {je}"
        }

    except Exception as e:
        print(f"[ERROR] GPT 호출 실패: {e}")
        return {
            "content": requirement,
            "precondition": "GPT 호출 실패",
            "expected_result": "오류",
            "actual_result": "",
            "note": str(e)
        }


def generate_scenarios(requirements: List[str]) -> List[Dict]:
    """
    여러 요구사항 리스트에 대해 테스트 시나리오 일괄 생성

    Args:
        requirements (List[str]): 요구사항 리스트

    Returns:
        List[Dict]: 테스트 시나리오 JSON 리스트
    """
    return [generate_scenario(req) for req in tqdm(requirements, desc="Generating scenarios")]
