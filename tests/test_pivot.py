from src.pivot.agg import group_by_count

def test_group_counts():
    rows = [["Engineering"], ["Marketing"], ["Engineering"]]
    counts = group_by_count(rows, 0)
    assert counts["Engineering"] == 2 and counts["Marketing"] == 1
