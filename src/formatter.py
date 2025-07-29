from typing import Dict, List


def assign_ids_to_scenarios(scenarios: List[Dict], prefix: str = "SC") -> List[Dict]:
    """
    각 테스트 시나리오에 고유 ID를 부여하여 정리된 JSON 리스트 반환

    Args:
        scenarios (List[Dict]): GPT로 생성된 시나리오 목록
        prefix (str): 시나리오 ID 접두어 (기본값: "SC")

    Returns:
        List[Dict]: ID가 부여된 테스트 시나리오 리스트
    """
    formatted = []

    for idx, scenario in enumerate(scenarios, start=1):
        scenario_id = f"{prefix}-{idx:03d}"

        formatted_scenario = {
            "id": scenario_id,
            "content": scenario.get("content", ""),
            "precondition": scenario.get("precondition", ""),
            "expected_result": scenario.get("expected_result", ""),
            "actual_result": scenario.get("actual_result", ""),
            "note": scenario.get("note", "")
        }

        formatted.append(formatted_scenario)

    return formatted


def print_scenarios(scenarios: List[Dict]) -> None:
    """
    콘솔에 시나리오 출력 (디버깅용)

    Args:
        scenarios (List[Dict]): ID가 포함된 시나리오 리스트
    """
    for scenario in scenarios:
        print(f"[{scenario['id']}] {scenario['content']}")
        print(f"  - 사전조건: {scenario['precondition']}")
        print(f"  - 예상결과: {scenario['expected_result']}")
        print()


def format_scenarios(scenarios: List[Dict]) -> List[Dict]:
    return assign_ids_to_scenarios(scenarios)