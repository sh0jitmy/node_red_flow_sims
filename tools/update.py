import sys
import logging

FILE_DEF="/Users/bluebird/node_red_work/tools/updatelog.txt"
logger = logging.getLogger("updateLogger")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=FILE_DEF)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logger.addHandler(handler)

for line in sys.stdin :
	logger.debug(f'Got inputs: {line.rstrip()}')
