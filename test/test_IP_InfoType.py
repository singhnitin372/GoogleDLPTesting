from utility import data_generator, response_to_list
from delayed_assert import expect, assert_expectations
import allure
import pytest
from utility.log import logger
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from request import DLPDataService

ipv4_list = list(data_generator.IPV4_generate())
ipv6_list = list(data_generator.IPV4_private_generate())
ipv6_private_list = list(data_generator.IPV6_generate())


@allure.title("To check google dlp can detect the IPV4 in the text for name {ipv4_address}")
@pytest.mark.parametrize("ipv4_address", ipv4_list)
def test_check_google_dlp_can_detect_ipv4_address(ipv4_address):
    try:
        response = DLPDataService.post_dlp_data_service(ipv4_address)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("IP_ADDRESS" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
           
            logger.info(
                f"To check google dlp can detect the IPV4 in the text for name {ipv4_address} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the IPV4 in the text for name {ipv4_address} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the IPV6 in the text for name {ipv6_address}")
@pytest.mark.parametrize("ipv6_address", ipv6_list)
def test_check_google_dlp_can_detect_ipv6_address(ipv6_address):
    try:
        response = DLPDataService.post_dlp_data_service(ipv6_address)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("IP_ADDRESS" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the IPV6 in the text for name {ipv6_address} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the IPV6 in the text for name {ipv6_address} test case is Failed ")

        assert False, e


@allure.title("To check google dlp can detect the IPV6 private address in the text for name {ipv6_private_address}")
@pytest.mark.parametrize("ipv6_private_address", ipv6_private_list)
def test_check_google_dlp_can_detect_ipv6_private_address(ipv6_private_address):
    try:
        response = DLPDataService.post_dlp_data_service(ipv6_private_address)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            logger.info(f'Google_DLP_Service response code is 200 and response is {response.text}')
            # get the json response from the api
            json_response = response.json()
            info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
            expect("IP_ADDRESS" in info_type_list)
            expect("POSSIBLE" in likelihood_list)
            assert_expectations()
            logger.info(
                f"To check google dlp can detect the IPV6 private address in the text for name {ipv6_private_address} test case is passed ")

    except Exception as e:
        logger.error(e)
        logger.error(
            f"To check google dlp can detect the IPV6 private address in the text for name {ipv6_address} test case is Failed ")

        assert False, e
