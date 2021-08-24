import allure
from schema import Schema

from utility.log import logger

# Schema for the Google DLP service
schema = Schema(
    {
        "result": {
            "findings": [
                {
                    "infoType": {
                        "name": str
                    },
                    "likelihood": str,
                    "location": {
                        "byteRange": {
                            "start": str,
                            "end": str
                        },
                        "codepointRange": {
                            "start": str,
                            "end": str
                        }
                    },
                    "createTime": str,
                    "findingId": str
                }
            ]
        }
    }
)

logger.info("Service name is: Google DLP service")
logger.info(f"Schema for service is: {str(schema)}")
