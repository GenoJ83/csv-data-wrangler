from typing import List, Dict, Any, Tuple

class TableJoiner:
    @staticmethod
    def inner_join(headers_a: List[str], rows_a: List[List[str]],
                   headers_b: List[str], rows_b: List[List[str]],
                   key: str) -> Tuple[List[str], List[List[str]]]:
        idx_a = headers_a.index(key)
        idx_b = headers_b.index(key)
        lut_b = {r[idx_b]: r for r in rows_b}
        joined_headers = headers_a + [h for h in headers_b if h != key]
        joined_rows = []
        for r_a in rows_a:
            k_val = r_a[idx_a]
            if k_val in lut_b:
                r_b = lut_b[k_val]
                joined_rows.append(r_a + [val for j, val in enumerate(r_b) if j != idx_b])
        return joined_headers, joined_rows
