from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["data.csv", "--to", "jsonl", "--dedupe-col", "email"])
    assert opts.file == "data.csv"
    assert opts.to == "jsonl"
    assert opts.dedupe_col == "email"
    assert main(["--version"]) == 0
