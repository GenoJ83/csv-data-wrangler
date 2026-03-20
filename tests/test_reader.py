from src.reader.stream import StreamTableReader

def test_stream_reading():
    content = "col1;col2\nval1;val2\nval3;val4"
    rows = list(StreamTableReader.read_rows(content))
    assert len(rows) == 3
    assert rows[0] == ["col1", "col2"]
    assert rows[1] == ["val1", "val2"]
