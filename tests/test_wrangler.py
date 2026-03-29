from src.wrangler import CsvWrangler

def test_wrangler_schema_and_dedupe():
    csv_data = "id,name,age\n1,Alice,30\n2,Bob,25\n1,Alice_Duplicate,30"
    w = CsvWrangler(csv_data)
    schema = w.get_schema()
    assert schema.headers == ["id", "name", "age"]
    assert schema.types["id"] == "integer"
    assert schema.types["age"] == "integer"
    
    dropped = w.drop_duplicates(key_column="id")
    assert dropped == 1
    assert len(w.rows) == 2
