from typing import List, Tuple

def check_ragged_rows(headers: List[str], rows: List[List[str]]) -> List[Tuple[int, int]]:
    expected = len(headers)
    ragged = []
    for idx, r in enumerate(rows):
        if len(r) != expected:
            ragged.append((idx + 1, len(r)))
    return ragged
