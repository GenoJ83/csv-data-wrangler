from src.sql_gen.ddl import DDLGenerator
from src.core.models import TableSchema

def test_ddl_generation():
    schema = TableSchema(["id", "score"], {"id": "integer", "score": "float"})
    sql = DDLGenerator.generate_create_table("users", schema)
    assert "CREATE TABLE users" in sql
    assert "id INTEGER" in sql
    assert "score NUMERIC" in sql
