from src.sort.sorter import TableSorter

def test_sorting():
    rows = [["2", "Bob"], ["1", "Alice"], ["3", "Charlie"]]
    sorted_rows = TableSorter.sort_by_column(rows, 0)
    assert sorted_rows[0][1] == "Alice"
    assert sorted_rows[-1][1] == "Charlie"
