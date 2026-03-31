from typing import List, Dict, Any

class ColumnSummarizer:
    @staticmethod
    def summarize_numeric(values: List[float]) -> Dict[str, float]:
        if not values:
            return {"count": 0}
        s_vals = sorted(values)
        n = len(s_vals)
        return {
            "count": float(n),
            "min": s_vals[0],
            "max": s_vals[-1],
            "mean": round(sum(s_vals) / n, 2),
            "median": s_vals[n // 2]
        }
