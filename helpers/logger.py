# helpers/logger.py
from loguru import logger

logger.add("logs/test_{time}.log", rotation="10 MB", retention="7 days", level="INFO")