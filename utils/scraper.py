from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import os


def init_scrapper() -> WebDriver:
    """ Initialize the selenium driver """
    project_dir = os.getcwd()
    drivers_dir = "drivers"
    driver_filename = "chromedriver"

    absolute_driver_path = os.path.join(
        project_dir,
        drivers_dir,
        driver_filename
    )

    driver = webdriver.Chrome(
        executable_path=absolute_driver_path
    )

    return driver
