import configparser
import os
from pathlib import Path
import allure

from utility.log import logger


# Generic function to get the base path of service
@allure.step('Getting the base url for api')
def get_base_uri():
    BASE_DIR = Path(__file__).resolve().parent.parent
    filename = os.path.join(BASE_DIR, 'resource/config.ini')

    logger.info(f"File name for config ini is: {filename}")
    # read the file using configparser
    config = configparser.ConfigParser()
    config.read(filename)
    # return the default section base url
    logger.info(f"Base url is: {str(config['DEFAULT']['base_url'])}")
    return config
