from typing import List, Dict

def group_by_count(rows: List[List[str]], col_idx: int) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for r in rows:
        if col_idx < len(r):
            k = r[col_idx]
            counts[k] = counts.get(k, 0) + 1
    return counts
