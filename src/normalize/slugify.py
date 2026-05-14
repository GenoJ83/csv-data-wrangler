import re
from typing import List

def normalize_headers(headers: List[str]) -> List[str]:
    norm = []
    for h in headers:
        clean = re.sub(r"[^a-zA-Z0-9]+", "_", h.strip().lower()).strip("_")
        norm.append(clean or "col")
    return norm
