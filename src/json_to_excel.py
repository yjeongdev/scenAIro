from io import BytesIO
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


def json_to_excel_buffer(data: List[Dict]) -> BytesIO:
    """
    JSON 데이터를 엑셀로 변환하여 BytesIO 객체로 반환
    """
    output = BytesIO()
    df = pd.DataFrame(data)
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return output
