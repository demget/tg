import sys
import logging


logger = logging.getLogger("tg")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
