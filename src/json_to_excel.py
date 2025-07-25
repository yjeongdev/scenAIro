from typing import Dict, List

import pandas as pd


def json_to_excel(data: List[Dict], output_path: str) -> None:
    """
    JSON 리스트 데이터를 엑셀(.xlsx) 파일로 저장

    Args:
        data (List[Dict]): 시나리오 JSON 리스트
        output_path (str): 저장할 엑셀 파일 경로
    """
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
