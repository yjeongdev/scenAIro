import re
from typing import List


def parse_requirements(input_text: str) -> List[str]:
    """
    '-' 기호로 구분된 요구사항을 파싱하여 리스트로 반환합니다.

    Args:
        input_text (str): 사용자로부터 입력받은 텍스트 (여러 줄 포함 가능)

    Returns:
        List[str]: 파싱된 요구사항 리스트
    """
    lines = input_text.strip().splitlines()
    requirements = []

    for line in lines:
        # "- " 또는 " - " 형식 앞의 공백 포함 허용
        match = re.match(r"^\s*-\s+(.*)", line)
        if match:
            req = match.group(1).strip()
            if req:
                requirements.append(req)

    return requirements

if __name__ == "__main__":
    sample_input = """
    - CR 워크아이템을 생성한다.
    - CR 워크아이템에 담당자를 지정한다.
    -   
    - 로그인 페이지를 띄운다.
    """

    parsed = parse_requirements(sample_input)
    for idx, req in enumerate(parsed, start=1):
        print(f"{idx:02d}: {req}")
