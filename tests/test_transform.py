from src.transform.cleaner import ColumnTransformer

def test_transformations():
    assert ColumnTransformer.fill_nulls(["a", "", "c"]) == ["a", "N/A", "c"]
    rows = [["1", "Alice"], ["2", "Bob"], ["3", "Charlie"]]
    filtered = ColumnTransformer.filter_by_column(rows, 0, lambda x: int(x) > 1)
    assert len(filtered) == 2
