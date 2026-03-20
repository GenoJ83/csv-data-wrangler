from typing import List, Dict, Any

class ColumnTransformer:
    @staticmethod
    def trim_whitespace(row: List[str]) -> List[str]:
        return [c.strip() for c in row]
        
    @staticmethod
    def fill_nulls(row: List[str], fallback: str = "N/A") -> List[str]:
        return [c if c.strip() != "" else fallback for c in row]
        
    @staticmethod
    def filter_by_column(rows: List[List[str]], col_index: int, predicate) -> List[List[str]]:
        return [r for r in rows if col_index < len(r) and predicate(r[col_index])]
