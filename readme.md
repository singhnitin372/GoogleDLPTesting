**Steps to Run**

1. Install the Nodejs and Python in your machine.
2. Install allure report using (npm install -g allure)
3. Go to the root project root directory and run (pip3 install -r requirements.txt)
4. Activate the virtualenv using (source bin/activate)
5. Run the command (pytest --alluredir=results)
6. Run the next command (allure serve results/)
7. Browser will open automatically, and you will be seeing a html report

**Project Structure**

1. resource folder contains 'config.ini', which holds base url for the test
2. schemas folder contains schema for service schema validation
3. test folder contains all the test files
4. request folder contains individual service requests
5. utility folder contains all useful methods for test
6. Body folder contains all the post body for the test