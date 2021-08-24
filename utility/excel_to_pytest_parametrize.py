import os
from pathlib import Path

import allure
import pandas as pd

from utility.log import logger


# This method will take a csv file and will return an List of tuple
@allure.step('Get the parameterize data from file path {file_path}')
def get_data(file_path):
    logger.info("Started convert csv to tuple in list")
    BASE_DIR = Path(__file__).resolve().parent.parent
    # get the full path to the filename
    filename = os.path.join(BASE_DIR, f'Data/{file_path}')
    logger.info(f"File path: {file_path}")
    # create the dataframe
    dataframe = pd.read_csv(filename)
    result = []
    # iterate over the rows of the csv file
    for index, row in dataframe.iterrows():
        # Create the tuple with all the csv row data
        tuple = (
            string_empty_check(row['scenario']), string_empty_check(row['text']), string_empty_check(row['likelihood']),
            string_empty_check(row['infoType']))
        # add the tuple to the list
        result.append(tuple)
    logger.info(f"After reading file parameterize data is {result}")
    # contains the list of tuple
    return result


# This method will accept the string and check whether string is empty or not, if empty then return an empty response
def string_empty_check(data):
    if data:
        return data
    else:
        return ""
