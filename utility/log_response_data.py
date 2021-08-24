import allure

from utility.log import logger


# Generic method to log all the response data in logger.
@allure.step('Log response Data for service {service_name}')
def from_reponse(service_name, response):
    status_code = response.status_code
    response_headers = response.headers
    logger.info(f"Service name is : {service_name}")
    logger.info(f"Service status code is : {status_code}")
    logger.info(f"Service response headers is : {response_headers}")

    try:
        response_json = response.json()
        logger.info(f"API response json for service is : {response_json}")
    except Exception as e:
        logger.error(f"API response error: str(response.text)")
