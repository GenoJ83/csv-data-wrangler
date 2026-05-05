from typing import List

def to_markdown_table(headers: List[str], rows: List[List[str]], limit: int = 5) -> str:
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows[:limit]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)
