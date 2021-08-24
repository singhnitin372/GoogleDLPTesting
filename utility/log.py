import logging

# format of our log record.
# print url and id of record which was set in format()
__stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
__stream_handler.setFormatter(formatter)

logger = logging.getLogger('api_automation')

logger.setLevel(logging.DEBUG)
logger.addHandler(__stream_handler)
# Adding the file appender
fh = logging.FileHandler('api_automation.log')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
