# test_mytestlogin.py
#
# This script contains automated test cases for logging into a web application.
# It uses Selenium WebDriver to interact with the web page and pytest for test execution.
# The tests involve navigating to the login page, entering valid credentials, and verifying
# that the user is successfully logged in.
#
# The script generates a detailed HTML report using pytest-html.


from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_cart():
    driver = webdriver.Chrome()  # No need to specify the path here
    driver.get("https://www.saucedemo.com/")

    # The Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # This adds an item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Validates the item in cart
    assert "Sauce Labs Backpack" in driver.page_source
import time

# Adds a delay to keep the browser open for 30 seconds
time.sleep(30)
    driver.quit()

