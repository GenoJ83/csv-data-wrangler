from src.markdown_table.md import to_markdown_table

def test_markdown_table():
    tbl = to_markdown_table(["colA", "colB"], [["val1", "val2"]])
    assert "| colA | colB |" in tbl
    assert "| --- | --- |" in tbl
