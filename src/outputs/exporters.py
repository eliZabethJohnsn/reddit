import json
import logging
from pathlib import Path

logger = logging.getLogger("exporter")

class JsonExporter:
    def export_json(self, data, filepath: Path):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        logger.info(f"JSON exported to {filepath}")