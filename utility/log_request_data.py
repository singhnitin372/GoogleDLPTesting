import allure

from utility.log import logger


# Generic function to log all the request data in logger.
@allure.step('Log request Data for service {service_name}')
def from_request(url, header, service_name):
    logger.info(f'API url is: {url}')
    logger.info(f'API service name is: {service_name}')
    logger.info(f'API header is: {header}')
