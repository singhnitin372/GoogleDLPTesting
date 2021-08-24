import allure

from utility.log import logger


# below method will take a api json response and will give two sorted list of info_type_list and likelihood_list
@allure.step('Create the Likelihood List and Info Type List from the json data {reponse_json_data}')
def get_data_list(reponse_json_data):
    logger.info(f'Converting the json to Info Type List and Likelihood list from {reponse_json_data}')
    info_type_list = []
    likelihood_list = []
    for i in reponse_json_data['result']['findings']:
        # iterate over the findings and add all the info type and likelihood data
        info_type_list.append(i['infoType']['name'])
        likelihood_list.append(i['likelihood'])
    logger.info(f'info_type_list: {info_type_list}')
    logger.info(f'likelihood_list: {likelihood_list}')
    # it will return two list of Info Type and Likelihood
    return sorted(info_type_list), sorted(likelihood_list)
