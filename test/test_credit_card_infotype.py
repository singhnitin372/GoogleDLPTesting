from utility import data_generator, response_to_list
from delayed_assert import expect, assert_expectations
import allure
import pytest
from utility.log import logger
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from request import DLPDataService

amex_credit_card_list = list(data_generator.amex_credit_card_generate())
master_credit_card_list = list(data_generator.master_credit_card_generate())
visa_credit_card_list = list(data_generator.visa_credit_card_generate())


@allure.title("To check google dlp can detect the amex credit card with number {amex_credit_card}")
@pytest.mark.parametrize("amex_credit_card", amex_credit_card_list)
def test_check_google_dlp_can_detect_amex_credit_card(amex_credit_card):
    try:
        response = DLPDataService.post_dlp_data_service(amex_credit_card)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("CREDIT_CARD_NUMBER" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the amex credit card with number {amex_credit_card} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the amex credit card with number {amex_credit_card} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the master credit card with number {master_credit_card}")
@pytest.mark.parametrize("master_credit_card", master_credit_card_list)
def test_check_google_dlp_can_detect_master_credit_card(master_credit_card):
    try:
        response = DLPDataService.post_dlp_data_service(master_credit_card)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("CREDIT_CARD_NUMBER" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the master credit card with number {master_credit_card} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the master credit card with number {master_credit_card} test case is Failed ")
        assert False, e


@allure.title("To check google dlp can detect the visa credit card with number {visa_credit_card}")
@pytest.mark.parametrize("visa_credit_card", visa_credit_card_list)
def test_check_google_dlp_can_detect_visa_credit_card(visa_credit_card):
    try:
        response = DLPDataService.post_dlp_data_service(visa_credit_card)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("CREDIT_CARD_NUMBER" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the visa credit card with number {visa_credit_card} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the visa credit card with number {visa_credit_card} test case is Failed ")
        assert False, e
