from src.merge.joiner import TableJoiner

def test_inner_join():
    h_a, r_a = ["id", "name"], [["1", "Alice"], ["2", "Bob"]]
    h_b, r_b = ["id", "dept"], [["1", "Eng"], ["3", "Sales"]]
    h_out, r_out = TableJoiner.inner_join(h_a, r_a, h_b, r_b, "id")
    assert h_out == ["id", "name", "dept"]
    assert len(r_out) == 1 and r_out[0] == ["1", "Alice", "Eng"]
