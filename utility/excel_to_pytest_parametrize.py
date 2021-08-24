import os
from pathlib import Path

import allure
import pandas as pd

from utility.log import logger


@allure.step('Get the parameterize data from file path {file_path}')
def get_data(file_path):
    logger.info("Started convert csv to tuple in list")
    BASE_DIR = Path(__file__).resolve().parent.parent
    filename = os.path.join(BASE_DIR, f'Data/{file_path}')
    logger.info(f"File path: {file_path}")
    dataframe = pd.read_csv(filename)
    result = []
    for index, row in dataframe.iterrows():
        print(row['scenario'])
        tuple = (
            string_empty_check(row['scenario']), string_empty_check(row['text']), string_empty_check(row['likelihood']),
            string_empty_check(row['infoType']))
        result.append(tuple)
    logger.info(f"After reading file parameterize data is {result}")
    return result


def string_empty_check(data):
    if data:
        return data
    else:
        return ""
