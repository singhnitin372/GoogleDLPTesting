import pytest
import allure
from request import DLPDataService
from schemas import DLPData_schema
from utility import read_json, log_response_data, excel_to_pytest_parametrize, response_to_list, string_position
from utility.log import logger
from delayed_assert import expect, assert_expectations


# Parametrize data to check for status code is 200 OK
def parametrizeData():
    return ["My age is 25 years"]


# Parametrize Data to check whether DLP detect all important info_type
def single_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('Single_Detection.csv', ['scenario', 'text', 'likelihood', 'infoType'])


# Parametrize Data to check Negative detection for the DLP detection
def false_positive_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('false_detection.csv', ['scenario', 'text', 'likelihood', 'infoType'])


# Parametrize Data to check whether DLP detect multiple info_type
def multiple_detection_data_parametrize():
    return excel_to_pytest_parametrize.get_data('Multiple_Detection.csv',
                                                ['scenario', 'text', 'likelihood', 'infoType'])


# Parametrize Data to check whether DLP detect correct starting and ending positions of string
def string_correct_starting_ending_positions_parametrize():
    return excel_to_pytest_parametrize.get_data('String_Starting_Ending_Position.csv',
                                                ['scenario', 'text', 'find_text'])


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
        # log the whole error on the report
        logger.error(f'Error message is: {e}')
        # mark the test case as failed
        assert False, e


# Check Status Code is 400 for the Google DLP Service when the text data is empty
@allure.title("To verify that Google DLP service status code is 400 for empty text")
def test_google_dlp_status_code_400():
    try:
        # Text is blank
        text = ""
        # Calling the Google DLP service with empty text
        response = DLPDataService.post_dlp_data_service(text)
        # Log the whole response body in the logger and report
        log_response_data.from_reponse('Google_DLP_Service', response)
        # Assert the status code is 400
        assert response.status_code == 400
        # Once Status Code is passed then mark the test cases as passed
        logger.info('test_google_dlp_status_code_400 is Passed')
    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_google_dlp_status_code_400 is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Check whether Google DLP Service can detect multiple infoType from the text and length of detection is more than 1
@allure.title("To verify that Google DLP service, can detect multiple item from text ")
def test_google_dlp_detect_multiple_item_from_text():
    try:
        # text which is having more than one infoType
        text = "My mail is singhnitin372@gmail.com and having age is 24 and name is nitin singh"
        # calling the API with the above text
        response = DLPDataService.post_dlp_data_service(text)
        # log the whole response
        log_response_data.from_reponse('Google_DLP_Service', response)
        # if status code is 200, then check whether length is more than 1
        if response.status_code == 200:
            json_response = response.json()
            # log the test case as passed, when the length is more than 1
            if (len(json_response['result']['findings'])) > 1:
                logger.info('test_google_dlp_detect_multiple_item_from_text is Passed')
            else:
                # log the test case as failed, when the length is less than 1
                logger.error('test_google_dlp_detect_multiple_item_from_text is Failed')
        # else mark the test case failed
        else:
            logger.error('test_google_dlp_detect_multiple_item_from_text is Failed')
            assert False

    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_google_dlp_detect_mutiple_item_from_text is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Verify Google DLP service has proper schema
@allure.title("To verify schema for the Google DLP service")
@pytest.mark.parametrize("text", parametrizeData())
def test_google_dlp_verify_schema(text):
    try:
        # Calling the Google DLP Service with the parametrize text
        response = DLPDataService.post_dlp_data_service(text)
        # log the whole response in the logger
        log_response_data.from_reponse('Google_DLP_Service', response)
        # read the schema
        schema = DLPData_schema.schema
        try:
            # Validate the schema with the actual api json response body
            schema.validate(response.json())
            # once schema validation is passed, then mark the test case as passed
            assert True
            logger.info(f'test_get_all_post_verify_schema is Passed')
        except Exception as e:
            # if any exception is raised, then mark the test case as Failed
            logger.error(f'test_get_all_post_verify_schema is Failed')
            assert False, e
    except Exception as e:
        # Any exception is raised during whole test then mark the test as Failed
        logger.error(f'test_get_all_post_verify_schema is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Check Google DLP service can detect single info type and assert the likelihood for those detection
@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,likelihood,infoType", single_detection_data_parametrize())
def test_google_dlp_verify_scenario_single_detection(scenario, text, likelihood, infoType):
    try:
        # calling the service with the Text Data
        response = DLPDataService.post_dlp_data_service(text)
        # log the whole response in the report
        log_response_data.from_reponse('Google_DLP_Service', response)
        # If status code is 200, then check for the infoType and likelihood
        if response.status_code == 200:
            try:
                # get the json from the api response
                json_response = response.json()
                # check for the infoType and likelihood
                # expect will do an soft assert and even assertion will failed, it will not be stopped
                expect(json_response['result']['findings'][0]['infoType']['name'] == infoType)
                expect(json_response['result']['findings'][0]['likelihood'] == likelihood)
                # finally do the assert expectations
                assert_expectations()
                logger.info(f'{scenario} is Passed')
            except Exception as e:
                # log the exception
                logger.error(f'{scenario} is Failed')
                assert False, e
        else:
            # mark it as error, once the status code is not 200
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
            assert False, f"Status Code is {response.status_code} and response text is {response.text}"
    except Exception as e:
        # Fail the test case once any exception occurred
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Check Google DLP Service detect multiple infoType and likelihood
@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,likelihood,infoType", multiple_detection_data_parametrize())
def test_google_dlp_verify_scenario_multiple_detection(scenario, text, likelihood, infoType):
    try:
        # calling the service with the Text Data
        response = DLPDataService.post_dlp_data_service(text)
        # log the whole response in the logger
        log_response_data.from_reponse('Google_DLP_Service', response)
        # if response is 200, then check for infoType and likelihood
        if response.status_code == 200:
            try:
                # get the json response from the api
                json_response = response.json()
                # call the below method to get the infoTypeList and LikelihoodList
                info_type_list, likelihood_list = response_to_list.get_data_list(json_response)
                # convert the comma separated info Type string to list and then sort the list
                actual_info_type = sorted(infoType.split(","))
                # convert the comma separated likelihood string to list and then sort the list
                actual_likelihood_type = sorted(likelihood.split(","))
                # soft assert the infotypeList with the actual json response list
                expect(actual_info_type == info_type_list)
                # soft assert the likelihoodList with the actual json response list
                expect(actual_likelihood_type == likelihood_list)
                # finally do the assertion
                assert_expectations()
                logger.info(f'{scenario} is Passed')
            except Exception as e:
                # mark the test case as failed, if anything exception occurred
                logger.error(f'{scenario} is Failed')
                assert False, f"Status Code is {response.status_code} and response text is {response.text}"
        else:
            # if status code is not 200, then mark the test as Failed
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
            assert False, e
    except Exception as e:
        # mark the test case as failed, if any exception occurred during the test case execution
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Check for the False positive test case
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
            assert False, f"Status Code is {response.status_code} and response text is {response.text}"
    except Exception as e:
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


# Check the starting and ending positions of the Google DLP is correct.
@allure.title("{scenario}")
@pytest.mark.parametrize("scenario,text,find_text", string_correct_starting_ending_positions_parametrize())
def test_google_dlp_verify_starting_ending_positions_detection(scenario, text, find_text):
    try:
        response = DLPDataService.post_dlp_data_service(text)
        log_response_data.from_reponse('Google_DLP_Service', response)
        if response.status_code == 200:
            try:
                json_response = response.json()

                logger.info(
                    f'scenario is {scenario} and text is  {text} and finding text is {find_text}')
                start, end = string_position.string_start_ending_position(text=text, finding_text=find_text)
                logger.info(
                    f'Starting position of the {text} and finding text is {find_text} and starting position is {start}')
                logger.info(
                    f'Ending position of the {text} and ending text is {find_text} and ending position is {start}')
                if text == find_text:
                    expect((int(json_response['result']['findings'][0]['location']['byteRange']['end'])) == int(start))
                    expect(
                        (int(json_response['result']['findings'][0]['location']['codepointRange']['end'])) == int(end))
                    assert_expectations()
                    logger.info(f'{scenario} is Passed')
                else:
                    expect(
                        (int(json_response['result']['findings'][0]['location']['byteRange']['start'])) == int(start))
                    expect(
                        (int(json_response['result']['findings'][0]['location']['byteRange']['end'])) == int(end))
            except Exception as e:
                logger.error(f'{scenario} is Failed')
                assert False, e
        else:
            logger.error(f'Response Text is {response.text}')
            logger.error(f'{scenario} is Failed')
            assert False, f"Status Code is {response.status_code} and response text is {response.text}"
    except Exception as e:
        logger.error(f'{scenario} is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e
