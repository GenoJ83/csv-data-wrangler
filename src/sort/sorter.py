from typing import List, Tuple

class TableSorter:
    @staticmethod
    def sort_by_column(rows: List[List[str]], col_index: int, reverse: bool = False) -> List[List[str]]:
        return sorted(rows, key=lambda r: r[col_index] if col_index < len(r) else "", reverse=reverse)
