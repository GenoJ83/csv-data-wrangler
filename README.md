# csv-data-wrangler

High-throughput tabular data wrangler, dialect auto-detector, schema inferrer, column transformer, and multi-format exporter.

[![CI](https://github.com/GenoJ83/csv-data-wrangler/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/csv-data-wrangler/actions)

## Features
- **Auto Dialect Detection**: Automatically detects comma, tab, semicolon, or pipe delimiters
- **Dynamic Type Inferrer**: Accurately infers integer, float, boolean, and text types
- **Format Conversion**: Stream converts CSV/TSV to JSON array or JSON Lines
- **SQL DDL Synthesis**: Automatically generates `CREATE TABLE` DDL for Postgres and SQLite
- **Relational Hash Join**: Fast in-memory key joining across tables

## Quick Start
```python
from src.wrangler import CsvWrangler

w = CsvWrangler("id,name,score\n1,Alice,98.5\n2,Bob,88.0")
schema = w.get_schema()
print(schema.types)  # {'id': 'integer', 'name': 'string', 'score': 'float'}
```
