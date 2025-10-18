import pytest
from selenium import webdriver

def get_driver(browser_name):

    if browser_name == 'chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    return driver

