from src.stats.summary import ColumnSummarizer

def test_numeric_summary():
    stats = ColumnSummarizer.summarize_numeric([10.0, 20.0, 30.0, 40.0, 50.0])
    assert stats["min"] == 10.0
    assert stats["max"] == 50.0
    assert stats["mean"] == 30.0
    assert stats["median"] == 30.0
