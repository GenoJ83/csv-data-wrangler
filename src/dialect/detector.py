import csv
from typing import Optional

class DialectDetector:
    @staticmethod
    def detect_delimiter(sample_text: str) -> str:
        common_delims = [",", "\t", ";", "|"]
        lines = [line.strip() for line in sample_text.strip().split("\n")[:5] if line.strip()]
        if not lines:
            return ","
        best_delim = ","
        max_consistency = -1
        for d in common_delims:
            counts = [l.count(d) for l in lines]
            if len(set(counts)) == 1 and counts[0] > 0:
                return d
            if sum(counts) > max_consistency:
                max_consistency = sum(counts)
                best_delim = d
        return best_delim
