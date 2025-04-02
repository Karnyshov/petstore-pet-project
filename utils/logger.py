import logging
import os
from io import StringIO

LOG_FILE = os.path.join(os.path.dirname(__file__), "../test_logs.log")

# Ensure logs are flushed immediately
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),  # File logging
        logging.StreamHandler(stream=StringIO())  # Console logging
    ]
)

logger = logging.getLogger("global_logger")
