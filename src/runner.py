import json
import logging
from pathlib import Path

from extractors.reddit_parser import RedditParser
from outputs.exporters import JsonExporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("runner")

def load_settings():
    cfg_path = Path(__file__).parent / "config" / "settings.example.json"
    with open(cfg_path, "r") as f:
        return json.load(f)

def main():
    settings = load_settings()
    logger.info("Settings loaded")

    parser = RedditParser()
    exporter = JsonExporter()

    sample_input_file = Path(__file__).parents[1] / "data" / "inputs.sample.txt"
    with open(sample_input_file, "r") as f:
        keywords = [line.strip() for line in f if line.strip()]

    results = []
    for kw in keywords:
        parsed = parser.parse_keyword(kw)
        results.extend(parsed)

    output_path = Path(__file__).parents[1] / "data" / "sample.json"
    exporter.export_json(results, output_path)

    logger.info(f"Exported {len(results)} items to {output_path}")

if __name__ == "__main__":
    main()