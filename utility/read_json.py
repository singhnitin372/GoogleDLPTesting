import os
from pathlib import Path
from string import Template
import allure

from utility.log import logger


# Generic file read function, it needs dict for Templating at runtime
@allure.step('reading the json from file : {filename} with dictionary: {d}')
def readfile(filename, d=None):
    BASE_DIR = Path(__file__).resolve().parent.parent
    filename = os.path.join(BASE_DIR, "body/" + filename)
    logger.info(f"Filename is: {filename}")
    with open(filename, 'r') as file_reader:
        s = file_reader.read()
        logger.info(f"File Text is: {s}")

    t = Template(s)
    final_text = t.substitute(d)
    logger.info(f"Final Text is: {final_text}")
    return final_text
