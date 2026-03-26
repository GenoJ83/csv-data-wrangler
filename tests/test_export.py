import json
from src.export.json_export import JsonTableExporter

def test_json_export():
    headers = ["id", "val"]
    rows = [["1", "foo"], ["2", "bar"]]
    res = json.loads(JsonTableExporter.to_json_records(headers, rows))
    assert len(res) == 2
    assert res[0]["val"] == "foo"
    
    jsonl = JsonTableExporter.to_jsonl(headers, rows)
    assert len(jsonl.strip().split("\n")) == 2
