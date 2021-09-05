from utility import data_generator, response_to_list
from delayed_assert import expect, assert_expectations
import allure
import pytest
from utility.log import logger
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from request import DLPDataService

phone_number_list = list(data_generator.phone_number())


@allure.title("To check google dlp can detect the phone number in the text for name {phone_number}")
@pytest.mark.parametrize("phone_number", phone_number_list)
def test_check_google_dlp_can_detect_phone_number(phone_number):
    try:
        response = DLPDataService.post_dlp_data_service(phone_number)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("PHONE_NUMBER" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
           
            logger.info(
                f"To check google dlp can detect the Phone Number in the text for name {phone_number} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the Phone Number in the text for name {phone_number} test case is Failed ")

        assert False, e
