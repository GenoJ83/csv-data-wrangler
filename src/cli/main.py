import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="csvwrangler", description="Tabular data wrangler CLI")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("file", nargs="?", help="CSV file path")
    p.add_argument("--to", choices=["json", "jsonl", "csv"], default="json")
    p.add_argument("--dedupe-col", help="Column to deduplicate by")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("csvwrangler v0.1.0")
        return 0
    return 0
