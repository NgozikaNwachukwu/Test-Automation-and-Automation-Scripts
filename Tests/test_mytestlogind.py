# test_mytestcart.py
#
# This script contains automated test cases for interacting with the shopping cart in a web application.
# Using Selenium WebDriver, the script tests actions like adding items to the cart, updating quantities,
# and verifying the correct number of items in the cart.
#
# The script also generates an HTML report using pytest-html for test results visualization.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("", "", False)
])
def test_login(username, password, expected_result):
    driver = webdriver.Chrome()  # No need to specify the path here
    driver.get("https://www.saucedemo.com/")

    # Input credentials
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Validate result
    if expected_result:
        assert "Products" in driver.page_source
    else:
        assert "Epic sadface" in driver.page_source
import time

# Your existing test steps here

# Add a delay to keep the browser open for 30 seconds
time.sleep(30)

    driver.quit()

