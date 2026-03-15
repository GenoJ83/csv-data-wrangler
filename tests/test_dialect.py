from src.dialect.detector import DialectDetector

def test_delimiter_detection():
    csv_text = "id,name,role\n1,Alice,Dev\n2,Bob,QA"
    assert DialectDetector.detect_delimiter(csv_text) == ","
    
    tsv_text = "id\tname\trole\n1\tAlice\tDev\n2\tBob\tQA"
    assert DialectDetector.detect_delimiter(tsv_text) == "\t"
    
    pipe_text = "a|b|c\n1|2|3"
    assert DialectDetector.detect_delimiter(pipe_text) == "|"
