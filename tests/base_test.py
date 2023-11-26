import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = "https://www.amazon.com.tr"
    wait_duration = 10

    def setUp(self):
        option = Options()
        option.add_argument("--start-maximized")
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=option)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(self.wait_duration)
        self.wait = WebDriverWait(self.driver, self.wait_duration)

