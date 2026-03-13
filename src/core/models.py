from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class TableSchema:
    headers: List[str]
    types: Dict[str, str]
    row_count: int = 0
    
@dataclass
class TableChunk:
    headers: List[str]
    rows: List[List[Any]]
