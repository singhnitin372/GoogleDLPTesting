import re
from utility.log import logger
import allure


# takes whole text and takes finding_text to find start and end position of the text
@allure.step('Finding the Starting and Ending position for the text {text} and finding text {finding_text}')
def string_start_ending_position(text, finding_text):
    try:
        logger.info(f'Finding the Starting and Ending position for the text {text} and finding text {finding_text}')
        for match in re.finditer(finding_text, text):
            start = match.start(0)
            end = match.end(0)
        logger.info(f'Starting position for the text is {str(start)} and ending position is {str(end)}')

        if text == finding_text:
            logger.info("Make Start equal to end as both string are same")
            start = end
        logger.info(f'Final Starting position for the text is {str(start)} and ending position is {str(end)}')
        return start, end
    except Exception as e:
        logger.error(e)
