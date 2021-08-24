import pytest
import allure
from request import DLPDataService
from schemas import DLPData_schema
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list
from utility.log import logger
from delayed_assert import expect, assert_expectations


# Parametrize data to check for status code is 200 OK
def parametrizeData():
    return ["My age is 25 years"]


# Parametrize Data to check whether DLP detect all important info_type
def single_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('Single_Detection.csv')


# Parametrize Data to check Negative detection for the DLP detection
def false_positive_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('false_detection.csv')


# Parametrize Data to check whether DLP detect multiple info_type
def multiple_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('Multiple_Detection.csv')

# Test case to check status code is 200 for the google dlp service
@allure.title("To verify that Google DLP service status code is 200")
@pytest.mark.parametrize("text", parametrizeData())
def test_google_dlp_status_code_200(text):
    try:
        # Calling the google dlp service
        response = DLPDataService.post_dlp_data_service(text)
        # Call the log response method to log all the data
        log_response_data.from_reponse('Google_DLP_Service', response)
        # Checking wheather status code is 200
        assert response.status_code == 200
        # Once assertion is passed then mark the test case as passed
        logger.info('test_google_dlp_status_code_200 is Passed')
    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_google_dlp_status_code_200 is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify that Google DLP service status code is 400 for empty text")
def test_google_dlp_status_code_400():
    try:
        text = ""
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        assert response.status_code == 400
        logger.info('test_google_dlp_status_code_400 is Passed')
    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_google_dlp_status_code_400 is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify that Google DLP service, can detect multiple item from text ")
def test_google_dlp_detect_multiple_item_from_text():
    try:
        text = "My mail is singhnitin372@gmail.com and having age is 24 and name is nitin singh"
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            json_response = response.json()
            if (len(json_response['result']['findings'])) > 1:
                logger.info('test_google_dlp_detect_multiple_item_from_text is Passed')
            else:
                logger.error('test_google_dlp_detect_multiple_item_from_text is Failed')
        else:
            logger.error('test_google_dlp_detect_mutiple_item_from_text is Failed')
            assert False

    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_google_dlp_detect_mutiple_item_from_text is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify schema for get all posts service")
@pytest.mark.parametrize("text", parametrizeData())
def test_google_dlp_verify_schema(text):
    try:
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        schema = DLPData_schema.schema
        try:
            schema.validate(response.json())
            assert True
            logger.info(f'test_get_all_post_verify_schema is Passed')
        except Exception as e:
            logger.error(f'test_get_all_post_verify_schema is Failed')
            assert False, e
    except Exception as e:
        logger.error(f'test_get_all_post_verify_schema is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,likelihood,infoType", single_detection_data_parametrize())
def test_google_dlp_verify_scenario_single_detection(scenario, text, likelihood, infoType):
    try:
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            try:
                json_response = response.json()
                expect(json_response['result']['findings'][0]['infoType']['name'] == infoType)
                expect(json_response['result']['findings'][0]['likelihood'] == likelihood)
                assert_expectations()
                logger.info(f'{scenario} is Passed')
            except Exception as e:
                logger.error(f'{scenario} is Failed')
                assert False, e
        else:
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
    except Exception as e:
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,likelihood,infoType", multiple_detection_data_parametrize())
def test_google_dlp_verify_scenario_multiple_detection(scenario, text, likelihood, infoType):
    try:
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            try:
                json_response = response.json()
                info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
                actual_info_type = sorted(infoType.split(","))
                actual_likelihood_type = sorted(likelihood.split(","))
                print(actual_likelihood_type, actual_info_type)
                expect(actual_info_type == info_type_list)
                expect(actual_likelihood_type == likelihood_list)
                assert_expectations()
                logger.info(f'{scenario} is Passed')
            except Exception as e:
                logger.error(f'{scenario} is Failed')
                assert False, e
        else:
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
    except Exception as e:
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,likelihood,infoType", false_positive_detection_data_parametrize())
def test_google_dlp_verify_scenario_false_positive_detection(scenario, text, likelihood, infoType):
    try:
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            try:
                json_response = response.json()
                expect(json_response['result']['findings'][0]['infoType']['name'] == infoType)
                expect(json_response['result']['findings'][0]['likelihood'] == likelihood)
                assert_expectations()
                logger.info(f'{scenario} is Passed')
            except Exception as e:
                logger.error(f'{scenario} is Failed')
                assert False, e
        else:
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
    except Exception as e:
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e
