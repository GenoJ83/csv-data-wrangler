from src.core.models import TableSchema

TYPE_SQL_MAP = {"integer": "INTEGER", "float": "NUMERIC", "boolean": "BOOLEAN", "string": "TEXT"}

class DDLGenerator:
    @staticmethod
    def generate_create_table(table_name: str, schema: TableSchema) -> str:
        cols = []
        for h in schema.headers:
            col_type = TYPE_SQL_MAP.get(schema.types.get(h, "string"), "TEXT")
            cols.append(f"    {h} {col_type}")
        cols_def = ",\n".join(cols)
        return f"CREATE TABLE {table_name} (\n{cols_def}\n);"
