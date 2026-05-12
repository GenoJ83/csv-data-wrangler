from src.validator.table_validator import check_ragged_rows

def test_ragged_rows():
    headers = ["a", "b", "c"]
    rows = [["1", "2", "3"], ["1", "2"]]
    ragged = check_ragged_rows(headers, rows)
    assert ragged == [(2, 2)]
