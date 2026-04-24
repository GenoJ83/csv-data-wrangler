from typing import List, Generator

def chunk_rows(rows: List[List[str]], chunk_size: int = 1000) -> Generator[List[List[str]], None, None]:
    for i in range(0, len(rows), chunk_size):
        yield rows[i:i + chunk_size]
