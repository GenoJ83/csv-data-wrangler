from src.wrangler import CsvWrangler
from src.export.json_export import JsonTableExporter
from src.markdown_table.md import to_markdown_table

def test_full_wrangler_pipeline():
    raw = "user_id,dept,salary\n101,Engineering,95000\n102,Marketing,75000\n103,Engineering,98000"
    w = CsvWrangler(raw)
    schema = w.get_schema()
    assert schema.row_count == 3
    json_str = JsonTableExporter.to_json_records(w.headers, w.rows)
    assert "Engineering" in json_str
    md = to_markdown_table(w.headers, w.rows)
    assert "| user_id |" in md
