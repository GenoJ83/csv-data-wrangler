import csv
import io
from typing import Generator, List, Tuple
from src.dialect.detector import DialectDetector

class StreamTableReader:
    @staticmethod
    def read_rows(file_content: str, delimiter: str = None) -> Generator[List[str], None, None]:
        delim = delimiter or DialectDetector.detect_delimiter(file_content)
        stream = io.StringIO(file_content.strip())
        reader = csv.reader(stream, delimiter=delim)
        for row in reader:
            if row:
                yield [col.strip() for col in row]
