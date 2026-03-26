from typing import List, Dict, Any
from src.reader.stream import StreamTableReader
from src.infer.type_inferrer import TypeInferrer
from src.core.models import TableSchema

class CsvWrangler:
    def __init__(self, raw_content: str, delimiter: str = None):
        rows = list(StreamTableReader.read_rows(raw_content, delimiter=delimiter))
        if not rows:
            self.headers = []
            self.rows = []
        else:
            self.headers = rows[0]
            self.rows = rows[1:]
            
    def get_schema(self) -> TableSchema:
        types = {}
        for idx, h in enumerate(self.headers):
            col_vals = [r[idx] for r in self.rows if idx < len(r)]
            types[h] = TypeInferrer.infer_type(col_vals)
        return TableSchema(headers=self.headers, types=types, row_count=len(self.rows))
        
    def drop_duplicates(self, key_column: str = None) -> int:
        seen = set()
        unique = []
        key_idx = self.headers.index(key_column) if key_column and key_column in self.headers else None
        dropped = 0
        for r in self.rows:
            marker = r[key_idx] if key_idx is not None else tuple(r)
            if marker in seen:
                dropped += 1
            else:
                seen.add(marker)
                unique.append(r)
        self.rows = unique
        return dropped
