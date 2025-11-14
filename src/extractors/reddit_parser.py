import logging
import time
from .utils_time import utc_now

logger = logging.getLogger("reddit_parser")

class RedditParser:
    """
    Simplified parser that simulates Reddit data extraction.
    """

    def parse_keyword(self, keyword: str):
        logger.info(f"Parsing keyword: {keyword}")

        # Simulated fake data for demonstration.
        results = [
            {
                "title": f"Sample post about {keyword}",
                "author": "demo_user",
                "permalink": f"/r/demo/{keyword}",
                "score": 42,
                "comments": 3,
                "timestamp": int(time.time()),
                "body": "",
                "replies": [],
                "retrieved_at": utc_now(),
            }
        ]
        return results