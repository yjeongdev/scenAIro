import json
import os

from formatter import assign_ids_to_scenarios, print_scenarios
from json_to_excel import json_to_excel
from requirement_parser import parse_requirements
from scenario_generator import generate_scenarios


def main(input_file_path: str, output_file_path: str) -> None:
    # 1. 요구사항 파일 읽기
    if not os.path.exists(input_file_path):
        print(f"[ERROR] 입력 파일이 존재하지 않습니다: {input_file_path}")
        return

    with open(input_file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # 2. 요구사항 파싱
    requirements = parse_requirements(raw_text)
    if not requirements:
        print("[WARN] 요구사항이 없습니다.")
        return

    print(f"[INFO] 총 {len(requirements)}개의 요구사항을 파싱했습니다.")

    # 3. GPT를 통한 시나리오 생성
    scenarios = generate_scenarios(requirements)

    # 4. ID 부여 및 포맷 정리
    formatted_scenarios = assign_ids_to_scenarios(scenarios)

    # 5. 콘솔 출력
    print_scenarios(formatted_scenarios)

    # 6. JSON 파일 저장
    with open(output_file_path, "w", encoding="utf-8") as f_out:
        json.dump(formatted_scenarios, f_out, ensure_ascii=False, indent=2)
    print(f"[INFO] 테스트 시나리오 JSON이 저장되었습니다: {output_file_path}")

    # 7. JSON 파일을 Excel 파일로 저장
    excel_output = os.path.splitext(output_file_path)[0] + ".xlsx"
    json_to_excel(formatted_scenarios, excel_output)
    print(f"[INFO] 테스트 시나리오 엑셀 파일이 저장되었습니다: {excel_output}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="seanAIro 테스트 시나리오 생성기")
    parser.add_argument(
        "--input", "-i", type=str, default="requirements.txt", help="요구사항 텍스트 파일 경로"
    )
    parser.add_argument(
        "--output", "-o", type=str, default="test_scenarios.json", help="출력 JSON 파일 경로"
    )

    args = parser.parse_args()
    main(args.input, args.output)