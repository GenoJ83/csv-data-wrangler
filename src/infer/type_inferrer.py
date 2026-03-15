import datetime
from typing import List, Dict

class TypeInferrer:
    @staticmethod
    def infer_type(values: List[str]) -> str:
        non_empty = [v.strip() for v in values if v.strip()]
        if not non_empty:
            return "string"
        # check int
        if all(v.lstrip("-").isdigit() for v in non_empty):
            return "integer"
        # check float
        try:
            for v in non_empty:
                float(v)
            return "float"
        except ValueError:
            pass
        # check boolean
        if all(v.lower() in ["true", "false", "1", "0", "yes", "no"] for v in non_empty):
            return "boolean"
        return "string"
