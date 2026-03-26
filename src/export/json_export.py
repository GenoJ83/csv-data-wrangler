import json
from typing import List, Dict, Any

class JsonTableExporter:
    @staticmethod
    def to_json_records(headers: List[str], rows: List[List[Any]]) -> str:
        records = [dict(zip(headers, r)) for r in rows]
        return json.dumps(records, indent=2)
        
    @staticmethod
    def to_jsonl(headers: List[str], rows: List[List[Any]]) -> str:
        lines = [json.dumps(dict(zip(headers, r))) for r in rows]
        return "\n".join(lines)
