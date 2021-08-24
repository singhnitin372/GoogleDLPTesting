import allure

from utility.log import logger


@allure.step('Create the Likelihood List and Info Type List from the json data {reponse_json_data}')
def get_data_list(reponse_json_data):
    logger.info(f'Converting the json to Info Type List and Likelihood list from {reponse_json_data}')
    info_type_list = []
    likelihood_list = []
    for i in reponse_json_data['result']['findings']:
        info_type_list.append(i['infoType']['name'])
        likelihood_list.append(i['likelihood'])
    logger.info(f'info_type_list: {info_type_list}')
    logger.info(f'likelihood_list: {likelihood_list}')

    return sorted(info_type_list), sorted(likelihood_list)
