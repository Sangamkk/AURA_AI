import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger("AURA")

from app.core.logger import logger

logger.info("Application Started")

logger.warning("No PDF Loaded")

logger.error("Gemini Error")