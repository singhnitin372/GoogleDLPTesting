from utility import data_generator, response_to_list
from delayed_assert import expect, assert_expectations
import allure
import pytest
from utility.log import logger
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from request import DLPDataService

full_name_list = list(data_generator.full_name_generate())
last_name_list = list(data_generator.last_name_generate())
first_name_list = list(data_generator.first_name_generate())


@allure.title("To check google dlp can detect the Full Name in the text for name {full_name}")
@pytest.mark.parametrize("full_name", full_name_list)
def test_check_google_dlp_can_detect_full_name(full_name):
    try:
        response = DLPDataService.post_dlp_data_service(full_name)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            expect(json_response['result']['findings'][0]['infoType']['name'] == "PERSON_NAME")
            expect(json_response['result']['findings'][0]['likelihood'] == "POSSIBLE")
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the Full Name in the text for name {full_name} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the Full Name in the text for name {full_name} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the Last Name in the text for name {last_name}")
@pytest.mark.parametrize("last_name", last_name_list)
def test_check_google_dlp_can_detect_last_name(last_name):
    try:
        response = DLPDataService.post_dlp_data_service(last_name)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            expect(json_response['result']['findings'][0]['infoType']['name'] == "PERSON_NAME")
            expect(json_response['result']['findings'][0]['likelihood'] == "POSSIBLE")
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the last Name in the text for name {last_name} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the last Name in the text for name {last_name} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the First Name in the text for name {first_name}")
@pytest.mark.parametrize("first_name", first_name_list)
def test_check_google_dlp_can_detect_first_name(first_name):
    try:
        response = DLPDataService.post_dlp_data_service(first_name)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("PERSON_NAME" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the first Name in the text for name {first_name} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the first Name in the text for name {first_name} test case is Failed ")

        assert False, e
