from src.split.partitioner import chunk_rows

def test_chunking():
    rows = [[str(i)] for i in range(10)]
    chunks = list(chunk_rows(rows, chunk_size=3))
    assert len(chunks) == 4
    assert len(chunks[0]) == 3 and len(chunks[-1]) == 1
