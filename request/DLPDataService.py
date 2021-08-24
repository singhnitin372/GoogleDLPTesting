from utility import log_request_data, read_json
from utility.base_utility import get_base_uri
import requests
import allure


# Calling delete_post service
@allure.step('Calling Google DLP POSTS API with id: {text} ')
def post_dlp_data_service(text):
    d = {'text': text}
    config = get_base_uri()
    base_url = config['DEFAULT']['base_url']
    key = config['DEFAULT']['key']
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    request_uri = base_url + "/v2/projects/qe-assignment/content:inspect?key=" + str(key)
    log_request_data.from_request(request_uri, headers, 'Google DLP Service')
    data = read_json.readfile("DLP_Post.json", d)
    response = requests.post(request_uri, headers=headers, data=data)
    return response
