from utility import data_generator, response_to_list
from delayed_assert import expect, assert_expectations
import allure
import pytest
from utility.log import logger
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from request import DLPDataService

date_list = list(data_generator.date_generate())
date_time_list = list(data_generator.date_time_generate())


@allure.title("To check google dlp can detect the Date in the text for date {date}")
@pytest.mark.parametrize("date", date_list)
def test_check_google_dlp_can_detect_date(date):
    try:
        response = DLPDataService.post_dlp_data_service(date)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()

            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)

            expect("DATE" in info_type_list)
            expect("LIKELY" in likelihood_list)
            assert_expectations()
            
            logger.info(
                f"To check google dlp can detect the Date in the text for date {date} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the Date in the text for date {date} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the Datetime in the text for datetime {date_time}")
@pytest.mark.parametrize("date_time", date_time_list)
def test_check_google_dlp_can_detect_date_time(date_time):
    try:
        response = DLPDataService.post_dlp_data_service(date_time)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("TIME" in info_type_list)
            expect("LIKELY" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the Datetime in the text for datetime {date_time} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the Datetime in the text for datetime {date_time} test case is Failed ")

        assert False, e
